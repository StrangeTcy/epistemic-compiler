"""Arena Direct UI adapter.

Only the Direct route and visible names confirmed from the current public Arena
page/help are assumed. Controls are resolved by accessible role/name at runtime;
a missing or ambiguous control pauses for a human instead of falling back to
private APIs or guessed site-specific CSS selectors.
"""

from __future__ import annotations

import asyncio
import mimetypes
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse

from playwright.async_api import TimeoutError as PlaywrightTimeoutError

from runtime.browser.browser import BrowserController, BrowserPage
from runtime.models import (
    ExecutionResult,
    JobContext,
    RetryableJobError,
    WaitingForHuman,
)

ARENA_DIRECT_URL = "https://arena.ai/text/direct"


def _accepts_file_type(path: Path, token: str) -> bool:
    suffix = path.suffix.lower()
    mime, _ = mimetypes.guess_type(str(path))
    mime = mime.lower() if mime else None
    if token == "*/*":
        return True
    if token.startswith("."):
        return suffix == token
    if token.endswith("/*"):
        return bool(mime and mime.startswith(token[:-1]))
    return bool(mime and mime == token)


class ArenaAdapter:
    site = "arena"

    @staticmethod
    def _is_arena_url(url: str) -> bool:
        try:
            parsed = urlparse(url)
        except ValueError:
            return False
        hostname = (parsed.hostname or "").lower()
        return parsed.scheme == "https" and (
            hostname == "arena.ai" or hostname.endswith(".arena.ai")
        )

    async def execute(
        self, context: JobContext, browser: BrowserController
    ) -> ExecutionResult:
        page = await browser.new_page()
        prior_interaction = dict(context.job_state.get("interaction", {}))
        submission_state = context.job_state.get(
            "submission_state"
        ) or prior_interaction.get("submission_state")
        saved_url = context.job_state.get("current_url") or prior_interaction.get(
            "current_url"
        )
        current_model: str | None = None
        try:
            target_url = saved_url or ARENA_DIRECT_URL
            if not self._is_arena_url(target_url):
                await self._wait_for_human(
                    context,
                    page,
                    "The saved navigation target is not an HTTPS Arena URL; refusing to open it.",
                    stage="saved_url_invalid",
                    extra={"saved_url": target_url},
                )
            try:
                await page.goto(target_url)
            except PlaywrightTimeoutError as exc:
                # Navigation happens before any new prompt submission. Retrying this
                # specific timeout is safe; ambiguous interaction failures instead
                # remain waiting_for_human.
                raise RetryableJobError(
                    f"Arena navigation timed out before prompt interaction: {exc}"
                ) from exc
            await self._record_progress(context, page, stage="page_opened")
            body = await page.body_text()
            await self._check_human_gates(context, page, body, stage="page_opened")

            if submission_state in {"submitting", "submitted"}:
                # A crash can happen between a click and the state write. Never blindly
                # submit a second copy; inspect the saved conversation and wait instead.
                if not await self._prompt_is_visible(page, context.prompt_text):
                    await self._wait_for_human(
                        context,
                        page,
                        "This job may have submitted before the previous run stopped, but its prompt is not visible in the saved conversation. Inspect the Arena page, then resume; the runner will not resubmit automatically.",
                        stage="submission_uncertain",
                        extra={"submission_state": submission_state},
                    )
                current_model = await self._selected_model(page, context.job.model)
                if not current_model:
                    await self._wait_for_human(
                        context,
                        page,
                        "The saved conversation is visible, but the selected Arena model is not identifiable. Verify it manually before resuming.",
                        stage="submitted_model_unknown",
                        extra={
                            "submission_state": submission_state,
                            "controls": await page.control_inventory(),
                        },
                    )
                return await self._wait_and_extract(context, page, current_model)

            current_model = await self._ensure_model(context, page)
            body = await page.body_text()
            await self._check_human_gates(context, page, body, stage="before_composer")
            if context.input_paths:
                await self._attach_inputs(
                    context,
                    page,
                    previously_verified=bool(
                        prior_interaction.get("attachments_verified")
                    ),
                )
            body = await page.body_text()
            await self._check_human_gates(context, page, body, stage="before_submit")

            composer = await self._find_composer(context, page)
            try:
                await composer.fill(context.prompt_text)
            except Exception as exc:
                await self._wait_for_human(
                    context,
                    page,
                    f"Could not enter the prompt through the unique accessible chat textbox: {exc}",
                    stage="composer_fill",
                )
            await self._record_progress(
                context, page, stage="prompt_filled", model_name=current_model
            )
            send_button = await self._find_send_button(context, page, composer)
            # Persist an ambiguous state before clicking. If the process dies during the
            # click, resume will inspect the same conversation and will never double-send.
            context.update_progress(
                {
                    "stage": "submitting",
                    "submission_state": "submitting",
                    "current_url": page.url,
                    "model_selected": current_model,
                }
            )
            try:
                await send_button.click()
            except Exception as exc:
                await self._wait_for_human(
                    context,
                    page,
                    f"The send control could not be activated reliably: {exc}",
                    stage="send_ambiguous",
                    extra={"submission_state": "submitting"},
                )
            await self._record_progress(
                context,
                page,
                stage="waiting_for_response",
                submission_state="submitted",
                model_name=current_model,
            )
            return await self._wait_and_extract(context, page, current_model)
        except WaitingForHuman:
            raise
        except Exception as exc:
            await self._save_failure_diagnostics(context, page, exc)
            raise
        finally:
            await page.close()

    async def _check_human_gates(
        self, context: JobContext, page: BrowserPage, body: str, *, stage: str
    ) -> None:
        lowered = body.lower()
        if re.search(
            r"recaptcha|captcha|verify (?:that )?you are (?:a )?human|i am not a robot",
            lowered,
        ):
            await self._wait_for_human(
                context,
                page,
                "Arena is presenting a CAPTCHA/human verification. Complete it manually in the persistent browser profile, then resume this run.",
                stage=stage,
                extra={"human_gate": "captcha"},
            )
        if re.search(
            r"(?:sign|log) in to continue|session expired|authentication required",
            lowered,
        ):
            profile = context.job.profile or context.job.site
            await self._wait_for_human(
                context,
                page,
                f"Arena requires authentication. Run `python scripts/browser_login.py arena --profile {profile}`, sign in manually, then resume.",
                stage=stage,
                extra={"human_gate": "login"},
            )
        if not self._is_arena_url(page.url):
            await self._wait_for_human(
                context,
                page,
                f"Unexpected site after navigation ({page.url}); verify the page before continuing.",
                stage=stage,
                extra={"human_gate": "unexpected_site"},
            )

    async def _selected_model(
        self, page: BrowserPage, expected: str | None = None
    ) -> str | None:
        query = parse_qs(urlparse(page.url).query)
        slug = query.get("model_a", [None])[0]
        # The public Direct route currently resolves to model_a=max and visibly labels
        # this option “Max”. Other slugs are accepted only when exposed in the UI.
        if slug and slug.casefold() == "max":
            return "Max"
        labels = await page.visible_text(page.by_role("button"))
        if slug:
            normalized = slug.replace("_", "-").casefold()
            exact = [
                label for label in labels if label.strip().casefold() == slug.casefold()
            ]
            if len(exact) == 1:
                return exact[0]
            matching = [
                label
                for label in labels
                if normalized in label.casefold().replace("_", "-")
            ]
            if len(matching) == 1:
                return matching[0]
            expected_slug = (
                expected.casefold().replace("_", "-").replace(" ", "-")
                if expected
                else None
            )
            if expected_slug and expected_slug == normalized:
                return expected
            return None
        if expected:
            exact_expected = [
                label for label in labels if label.casefold() == expected.casefold()
            ]
            if len(exact_expected) == 1:
                return exact_expected[0]
        return None

    async def _ensure_model(self, context: JobContext, page: BrowserPage) -> str:
        requested = context.job.model
        selected = await self._selected_model(page, requested)
        if requested is None:
            if selected:
                context.update_progress(
                    {
                        "model_selected": selected,
                        "model_selection_source": "visible Direct URL/UI",
                    }
                )
                return selected
            await self._wait_for_human(
                context,
                page,
                "Could not determine the active Arena Direct model from the visible UI/URL. Select a model manually and resume, or set an explicit model in the mission YAML.",
                stage="model_unknown",
                extra={"controls": await page.control_inventory()},
            )

        if selected and selected.casefold() == requested.casefold():
            context.update_progress(
                {
                    "model_selected": selected,
                    "model_selection_source": "mission matches current UI",
                }
            )
            return selected

        # The current Direct page exposes its selected model in the model_a query and
        # its visible selector. Open only that uniquely named control; do not click a
        # guessed CSS path or choose the first available model.
        if not selected:
            await self._wait_for_human(
                context,
                page,
                "Arena's current selection is not identifiable. The model picker may have changed; inspect it manually and resume.",
                stage="model_selector_unknown",
                extra={
                    "model_requested": requested,
                    "controls": await page.control_inventory(),
                },
            )
        current_control = page.by_role(
            "button",
            re.compile(rf"^{re.escape(selected)}$", re.IGNORECASE),
            exact=False,
        )
        if await page.visible_count(current_control) != 1:
            await self._wait_for_human(
                context,
                page,
                f"Could not identify a unique accessible control for the currently selected model {selected!r}.",
                stage="model_selector_ambiguous",
                extra={
                    "model_requested": requested,
                    "model_selected": selected,
                    "controls": await page.control_inventory(),
                },
            )
        try:
            await current_control.click()
        except Exception as exc:
            await self._wait_for_human(
                context,
                page,
                f"Could not open the Arena model picker: {exc}",
                stage="model_picker_open",
                extra={"model_requested": requested, "model_selected": selected},
            )

        containers = []
        for role in ("listbox", "dialog"):
            locator = page.by_role(role)
            if await page.visible_count(locator) == 1:
                containers.append(locator.first)
        if len(containers) != 1:
            await self._wait_for_human(
                context,
                page,
                "The model picker did not expose one unambiguous accessible list/dialog. Choose the requested model manually and resume.",
                stage="model_picker_contents",
                extra={
                    "model_requested": requested,
                    "controls": await page.control_inventory(),
                },
            )
        container = containers[0]
        target = None
        target_role = None
        for role in ("option", "menuitem", "button", "link"):
            locator = container.get_by_role(
                role, name=re.compile(rf"^{re.escape(requested)}$", re.IGNORECASE)
            )
            if await page.visible_count(locator) == 1:
                target, target_role = locator.first, role
                break
        if target is None:
            await self._wait_for_human(
                context,
                page,
                f"The exact requested model {requested!r} is not uniquely available in Arena's current picker. Verify availability/plan and resume.",
                stage="model_unavailable",
                extra={
                    "model_requested": requested,
                    "controls": await page.control_inventory(),
                },
            )
        try:
            await target.click()
            await page.raw.wait_for_timeout(500)
        except Exception as exc:
            await self._wait_for_human(
                context,
                page,
                f"Could not select model {requested!r} through its accessible {target_role} entry: {exc}",
                stage="model_select",
                extra={"model_requested": requested},
            )
        selected_after = await self._selected_model(page, requested)
        if selected_after and selected_after.casefold() == requested.casefold():
            context.update_progress(
                {
                    "model_selected": selected_after,
                    "model_selection_source": "Arena Direct picker",
                }
            )
            return selected_after
        await self._wait_for_human(
            context,
            page,
            f"Arena did not confirm the requested model {requested!r} after selection. Verify the visible model and resume.",
            stage="model_selection_unconfirmed",
            extra={
                "model_requested": requested,
                "model_selected_after": selected_after,
                "current_url": page.url,
            },
        )

    async def _attach_inputs(
        self,
        context: JobContext,
        page: BrowserPage,
        *,
        previously_verified: bool,
    ) -> None:
        filenames = [path.name for path in context.input_paths]
        body = await page.body_text()
        visible_names = [name for name in filenames if name in body]
        if previously_verified:
            if len(visible_names) == len(filenames):
                await self._record_progress(
                    context,
                    page,
                    stage="attachments_verified",
                    attachments_verified=True,
                    attachments=filenames,
                )
                return
            if visible_names:
                await self._wait_for_human(
                    context,
                    page,
                    "Only some previously verified attachments are visible after resume. Resolve the attachment state manually before submitting.",
                    stage="attachment_state_ambiguous",
                    extra={
                        "visible_filenames": visible_names,
                        "expected_filenames": filenames,
                    },
                )
            await self._wait_for_human(
                context,
                page,
                "Attachments verified in the previous attempt are not visible after resume. Reattach them manually and resume; the runner will not risk duplicate uploads.",
                stage="attachments_missing_on_resume",
                extra={"expected_filenames": filenames},
            )
        if visible_names:
            await self._wait_for_human(
                context,
                page,
                "The current page already shows one or more requested filenames, but this run has no matching upload record. Verify the attachments manually.",
                stage="attachments_already_present",
                extra={
                    "visible_filenames": visible_names,
                    "expected_filenames": filenames,
                },
            )

        file_input = page.locator('input[type="file"]')
        count = await file_input.count()
        if count != 1:
            await self._wait_for_human(
                context,
                page,
                f"This Arena page exposes {count} native file inputs; the upload control is ambiguous. Attach the files manually and resume.",
                stage="file_input_unknown",
                extra={"input_paths": [str(path) for path in context.input_paths]},
            )
        accept = await file_input.get_attribute("accept") or ""
        allowed = [
            token.strip().lower() for token in accept.split(",") if token.strip()
        ]
        if allowed:
            unsupported = [
                path.name
                for path in context.input_paths
                if not any(_accepts_file_type(path, token) for token in allowed)
            ]
            if unsupported:
                await self._wait_for_human(
                    context,
                    page,
                    "Arena's visible file input does not advertise support for: "
                    + ", ".join(unsupported),
                    stage="file_type_unsupported",
                    extra={
                        "accept": accept,
                        "input_paths": [str(path) for path in context.input_paths],
                    },
                )
        try:
            await page.upload_files(context.input_paths)
            await page.raw.wait_for_timeout(750)
        except Exception as exc:
            await self._wait_for_human(
                context,
                page,
                f"Arena rejected or did not expose the requested attachment through its native file input: {exc}",
                stage="file_upload",
                extra={
                    "input_paths": [str(path) for path in context.input_paths],
                    "accept": accept,
                },
            )
        body = await page.body_text()
        missing = [name for name in filenames if name not in body]
        if missing:
            await self._wait_for_human(
                context,
                page,
                "Could not verify all uploaded file names in the Arena UI; confirm the attachments manually.",
                stage="file_upload_unverified",
                extra={"missing_filenames": missing},
            )
        await self._record_progress(
            context,
            page,
            stage="attachments_verified",
            attachments_verified=True,
            attachments=filenames,
        )

    async def _find_composer(self, context: JobContext, page: BrowserPage) -> Any:
        textboxes = page.by_role("textbox")
        count = await page.visible_count(textboxes)
        if count != 1:
            await self._wait_for_human(
                context,
                page,
                f"Expected one visible accessible chat textbox on Arena Direct; found {count}. Inspect the UI rather than selecting a field by guess.",
                stage="composer_ambiguous",
                extra={"controls": await page.control_inventory()},
            )
        return textboxes.first

    async def _find_send_button(
        self, context: JobContext, page: BrowserPage, composer: Any
    ) -> Any:
        for label in ("Send", "Send message", "Submit", "Start workflow"):
            locator = page.by_role(
                "button", re.compile(rf"^{re.escape(label)}$", re.IGNORECASE)
            )
            if await page.visible_count(locator) == 1:
                try:
                    if await locator.first.is_enabled():
                        return locator.first
                except Exception:
                    continue
        # A native submit button associated with the same chat form is a semantic,
        # non-site-specific fallback. No unlabeled arrow/icon is clicked by position.
        forms = page.locator("form")
        try:
            for form in await forms.all():
                if not await form.is_visible():
                    continue
                if await form.get_by_role("textbox").count() == 0:
                    continue
                submit = form.locator('button[type="submit"]')
                if (
                    await page.visible_count(submit) == 1
                    and await submit.first.is_enabled()
                ):
                    return submit.first
        except Exception:
            pass
        # The user may choose to submit manually in the same saved conversation.
        # Mark the state ambiguous before pausing so a later resume cannot double-send.
        context.update_progress(
            {
                "stage": "send_control_unknown",
                "submission_state": "submitting",
                "current_url": page.url,
            }
        )
        await self._wait_for_human(
            context,
            page,
            "The chat submit control has no unambiguous accessible name or native form-submit relationship. Inspect the saved conversation; if you manually submit it, resume will inspect for the prompt and will not send a second copy.",
            stage="send_control_unknown",
            extra={
                "controls": await page.control_inventory(),
                "prompt_sha256": context.prompt_sha256,
                "submission_state": "submitting",
            },
        )

    async def _prompt_is_visible(self, page: BrowserPage, prompt: str) -> bool:
        main = await page.main_text()
        body = main or await page.body_text()
        return prompt.strip() in body

    async def _wait_and_extract(
        self, context: JobContext, page: BrowserPage, model_name: str | None
    ) -> ExecutionResult:
        timeout = context.job.timeout_seconds
        deadline = asyncio.get_running_loop().time() + timeout
        previous: str | None = None
        stable = 0
        saw_candidate = False
        boundary_missing_polls = 0
        while asyncio.get_running_loop().time() < deadline:
            body = await page.body_text()
            await self._check_human_gates(
                context, page, body, stage="waiting_for_response"
            )
            main = await page.main_text()
            articles = page.by_role("article")
            article_count = await page.visible_count(articles)
            candidate, extraction_issue = await self._response_from_articles(
                page, context.prompt_text
            )
            if extraction_issue:
                await self._wait_for_human(
                    context,
                    page,
                    extraction_issue,
                    stage="response_extraction_ambiguous",
                    extra={"controls": await page.control_inventory()},
                )
            if article_count == 0 and (
                context.prompt_text.strip() in main
                or context.prompt_text.strip() in body
            ):
                boundary_missing_polls += 1
                if boundary_missing_polls >= 5:
                    await self._wait_for_human(
                        context,
                        page,
                        "Arena shows the submitted prompt but exposes no ARIA article boundary for isolating the response. Inspect the page manually; the runner will not slice unstructured page text.",
                        stage="response_message_boundary_unavailable",
                        extra={"article_count": article_count},
                    )
            else:
                boundary_missing_polls = 0
            if candidate is not None and candidate.strip():
                saw_candidate = True
            else:
                candidate = None
            stop_controls = page.by_role(
                "button", re.compile(r"stop|cancel|interrupt|generating", re.IGNORECASE)
            )
            busy = await page.visible_count(stop_controls) > 0
            composer = page.by_role("textbox")
            composer_enabled = False
            if await page.visible_count(composer) == 1:
                try:
                    composer_enabled = await composer.first.is_enabled()
                except Exception:
                    pass
            if candidate and not busy and composer_enabled:
                if candidate == previous:
                    stable += 1
                else:
                    previous = candidate
                    stable = 1
            else:
                previous = candidate
                stable = 0
            if stable >= 4:
                conversation_id = self._conversation_id(page.url)
                await self._record_progress(
                    context,
                    page,
                    stage="response_extracted",
                    submission_state="submitted",
                    conversation_id=conversation_id,
                    model_name=model_name,
                )
                return ExecutionResult(
                    response_text=candidate,
                    model_name=model_name,
                    conversation_id=conversation_id,
                    current_url=page.url,
                    metadata={
                        "completion_detection": "assistant article stable for 4 polls; composer enabled; no visible stop/cancel control",
                        "completion_detection_confidence": "local UI heuristic; not server-confirmed",
                        "response_extraction": "verbatim visible inner_text of the unique article immediately following the prompt-containing article",
                        "response_content_edits": False,
                        "outer_code_fence_removed": False,
                        "user_label_lines_removed": [],
                        "response_chars": len(candidate),
                    },
                )
            await page.raw.wait_for_timeout(1000)
        reason = "Arena response did not reach an unambiguous stable-complete state before timeout. The saved conversation was not resubmitted."
        await self._wait_for_human(
            context,
            page,
            reason,
            stage="response_completion_unknown",
            extra={
                "submission_state": "submitted",
                "response_candidate_seen": saw_candidate,
                "timeout_seconds": timeout,
                "model_selected": model_name,
            },
        )

    async def _response_from_articles(
        self, page: BrowserPage, prompt: str
    ) -> tuple[str | None, str | None]:
        """Extract only when ARIA article boundaries identify one exact assistant turn.

        We intentionally do not fall back to slicing an undifferentiated page-text
        tail: that could include controls or another message and would violate the
        response-verbatim requirement. An unsupported/changed UI is a human wait.
        """
        articles = page.by_role("article")
        try:
            visible_articles = []
            visible = []
            for article in await articles.all():
                if await article.is_visible():
                    visible_articles.append(article)
                    visible.append(await article.inner_text())
        except Exception:
            return None, None
        matches = [index for index, text in enumerate(visible) if prompt in text]
        if not matches:
            return None, None
        if len(matches) != 1:
            return (
                None,
                "Arena exposes multiple article regions containing the submitted prompt; the response boundary is ambiguous. Inspect the conversation manually.",
            )
        prompt_index = matches[0]
        after_count = len(visible) - prompt_index - 1
        if after_count == 0:
            return (
                None,
                None,
            )  # The response article may not exist until generation starts.
        if after_count != 1:
            return (
                None,
                "Arena exposes more than one article after the submitted prompt, so the assistant response cannot be isolated safely. Inspect the conversation manually.",
            )
        assistant_article = visible_articles[prompt_index + 1]
        try:
            nested_controls = assistant_article.get_by_role("button")
            if await page.visible_count(nested_controls) > 0:
                return (
                    None,
                    "The assistant article contains visible button controls, so its response text cannot be separated from UI labels without editing. Inspect it manually.",
                )
        except Exception:
            return (
                None,
                "The assistant article's controls could not be inspected safely. Inspect the response manually.",
            )
        candidate = visible[prompt_index + 1]
        if not candidate.strip():
            return None, None
        return candidate, None

    @staticmethod
    def _conversation_id(url: str) -> str | None:
        parsed = urlparse(url)
        query = parse_qs(parsed.query)
        for key in ("conversation_id", "chat_id", "thread_id"):
            if query.get(key):
                return query[key][0]
        parts = [part for part in parsed.path.split("/") if part]
        if len(parts) >= 3 and parts[-2] not in {"text", "direct"}:
            return parts[-1]
        return None

    async def _record_progress(
        self, context: JobContext, page: BrowserPage, *, stage: str, **extra: Any
    ) -> None:
        selected_model = extra.pop("model_name", None)
        updates: dict[str, Any] = {
            "stage": stage,
            "current_url": page.url,
        }
        conversation_id = self._conversation_id(page.url)
        if conversation_id:
            updates["conversation_id"] = conversation_id
        if selected_model:
            updates["model_selected"] = selected_model
        updates.update(extra)
        context.update_progress(updates)

    async def _wait_for_human(
        self,
        context: JobContext,
        page: BrowserPage,
        reason: str,
        *,
        stage: str,
        extra: dict[str, Any] | None = None,
    ) -> None:
        screenshot_rel = await self._screenshot(context, page, f"waiting-{stage}")
        details = {
            "stage": stage,
            "current_url": page.url,
            "screenshot": screenshot_rel,
            "submission_state": context.job_state.get("submission_state"),
        }
        if extra:
            details.update(extra)
        context.update_progress(details)
        raise WaitingForHuman(reason, details=details)

    async def _save_failure_diagnostics(
        self, context: JobContext, page: BrowserPage, exc: Exception
    ) -> None:
        try:
            screenshot_rel = await self._screenshot(
                context, page, f"failure-{type(exc).__name__}"
            )
            controls = await page.control_inventory()
            context.update_progress(
                {
                    "stage": "site_error",
                    "current_url": page.url,
                    "screenshot": screenshot_rel,
                    "last_error_type": type(exc).__name__,
                    "last_error": str(exc)[:1000],
                    "controls": controls,
                }
            )
        except Exception:
            # Diagnostics must not hide the original UI failure.
            return

    async def _screenshot(
        self, context: JobContext, page: BrowserPage, label: str
    ) -> str | None:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        target = context.job_dir / "screenshots" / f"{label}-{stamp}.png"
        try:
            await page.screenshot(target)
            return str(target.relative_to(context.run_dir))
        except Exception:
            return None
