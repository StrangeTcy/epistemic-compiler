from __future__ import annotations

import asyncio
import hashlib
import re
from pathlib import Path

import pytest

from runtime.browser.sites.arena import ArenaAdapter
from runtime.models import JobSpec, MissionSpec, WaitingForHuman


class EmptyLocator:
    async def all(self):
        return []


class FakeElement:
    def __init__(self, text=""):
        self.text = text

    def get_by_role(self, role, name=None):
        return EmptyLocator()

    async def is_visible(self):
        return True

    async def inner_text(self):
        return self.text

    async def is_enabled(self):
        return True


class FakeArticle(FakeElement):
    pass


class FakeTextbox(FakeElement):
    def __init__(self, page):
        super().__init__("Chat message")
        self.page = page

    async def fill(self, value):
        self.page.filled_prompt = value


class FakeSendButton(FakeElement):
    def __init__(self, page):
        super().__init__("Send")
        self.page = page

    async def click(self):
        self.page.send_clicks += 1
        self.page.articles = [
            FakeArticle(self.page.filled_prompt),
            FakeArticle(self.page.response),
        ]


class FakeLocator:
    def __init__(self, page, role, name=None):
        self.page = page
        self.role = role
        self.name = name

    def _items(self):
        return self.page.elements(self.role, self.name)

    @property
    def first(self):
        items = self._items()
        if not items:
            raise AssertionError(f"no fake element for role {self.role}")
        return items[0]

    async def all(self):
        return list(self._items())

    async def count(self):
        return len(self._items())

    async def get_attribute(self, name):
        return None

    async def is_visible(self):
        return bool(self._items()) and await self.first.is_visible()

    async def is_enabled(self):
        return await self.first.is_enabled()

    async def fill(self, value):
        await self.first.fill(value)

    async def click(self):
        await self.first.click()

    def get_by_role(self, role, name=None):
        return FakeLocator(self.page, role, name)

    def locator(self, selector):
        return FakeLocator(self.page, "none", selector)


class FakePage:
    def __init__(
        self, *, response="```md\nVerbatim answer.\n```\n", body="Arena Direct"
    ):
        self.url = "https://arena.ai/text/direct?model_a=max"
        self.response = response
        self.page_body = body
        self.articles = []
        self.filled_prompt = ""
        self.send_clicks = 0
        self.closed = False
        self.raw = self

    async def goto(self, url):
        self.url = url if "?" in url else url + "?model_a=max"

    async def body_text(self, **kwargs):
        if self.articles:
            return "\n".join(article.text for article in self.articles)
        return self.page_body

    async def main_text(self, **kwargs):
        return await self.body_text()

    def elements(self, role, name=None):
        if role == "article":
            return self.articles
        if role == "textbox":
            return [FakeTextbox(self)]
        if role == "button":
            button = FakeSendButton(self)
            if name is None:
                return [button]
            pattern = name.pattern if isinstance(name, re.Pattern) else str(name)
            if re.search(pattern, "Send", re.IGNORECASE):
                return [button]
            return []
        return []

    def by_role(self, role, name=None, *, exact=False):
        return FakeLocator(self, role, name)

    def locator(self, selector):
        return FakeLocator(self, "none", selector)

    async def visible_count(self, locator):
        count = 0
        for item in await locator.all():
            if await item.is_visible():
                count += 1
        return count

    async def visible_text(self, locator):
        values = []
        for item in await locator.all():
            if await item.is_visible():
                value = (await item.inner_text()).strip()
                if value:
                    values.append(value)
        return values

    async def control_inventory(self):
        return [{"role": "textbox", "name": "Chat message"}]

    async def upload_files(self, paths):
        raise AssertionError("this test has no attachments")

    async def screenshot(self, path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"fake screenshot")

    async def wait_for_timeout(self, milliseconds):
        return None

    async def close(self):
        self.closed = True


class FakeBrowser:
    def __init__(self, page):
        self.page = page

    async def new_page(self):
        return self.page


class FakeContext:
    def __init__(self, tmp_path, *, state=None, prompt="Return the answer exactly."):
        self.run_dir = tmp_path / "run"
        self.job_dir = self.run_dir / "artifacts/jobs/job1"
        self.job_dir.mkdir(parents=True, exist_ok=True)
        self.prompt_text = prompt
        self.prompt_sha256 = hashlib.sha256(prompt.encode()).hexdigest()
        self.input_paths = ()
        self.input_records = ()
        self.job_state = state or {"interaction": {}}
        self.updates = []
        self.job = JobSpec(
            job_id="job1",
            mission_id="test",
            role="theorist",
            prompt_artifact="prompt.md",
            input_artifacts=(),
            dependencies=(),
            site="arena",
            model="Max",
            profile="test-profile",
            output_artifact="artifacts/jobs/job1/response.md",
            timeout_seconds=10,
        )
        self.mission = MissionSpec(
            mission_id="test",
            mission_type="test",
            path=tmp_path / "mission.yaml",
            inputs={},
            jobs=(self.job,),
            sha256="fake",
        )

        def update(values):
            self.updates.append(dict(values))
            self.job_state.setdefault("interaction", {}).update(values)
            self.job_state.update(values)

        self.update_progress = update


def test_adapter_accepts_only_https_arena_hosts():
    assert ArenaAdapter._is_arena_url("https://arena.ai/text/direct?model_a=max")
    assert ArenaAdapter._is_arena_url("https://www.arena.ai/text/direct")
    assert not ArenaAdapter._is_arena_url("http://arena.ai/text/direct")
    assert not ArenaAdapter._is_arena_url("https://evil-arena.ai/text/direct")
    assert not ArenaAdapter._is_arena_url("https://arena.ai.example.test/text/direct")


def test_direct_submits_once_and_preserves_visible_response_verbatim(tmp_path):
    response = "```md\nVerbatim answer.\n```\n"
    page = FakePage(response=response)
    context = FakeContext(tmp_path)
    result = asyncio.run(ArenaAdapter().execute(context, FakeBrowser(page)))

    assert page.send_clicks == 1
    assert page.closed
    assert result.response_text == response
    assert result.model_name == "Max"
    assert result.metadata["response_content_edits"] is False
    assert result.metadata["outer_code_fence_removed"] is False
    assert result.metadata["user_label_lines_removed"] == []
    assert context.job_state["submission_state"] == "submitted"


def test_resume_of_submitted_job_never_clicks_send_again(tmp_path):
    prompt = "Return the answer exactly."
    page = FakePage(response="Already submitted answer.")
    page.articles = [FakeArticle(prompt), FakeArticle(page.response)]
    context = FakeContext(
        tmp_path,
        state={
            "submission_state": "submitted",
            "current_url": page.url,
            "interaction": {"submission_state": "submitted", "current_url": page.url},
        },
        prompt=prompt,
    )

    result = asyncio.run(ArenaAdapter().execute(context, FakeBrowser(page)))
    assert page.send_clicks == 0
    assert result.response_text == "Already submitted answer."


def test_captcha_transitions_to_human_wait_and_saves_screenshot(tmp_path):
    page = FakePage(body="reCAPTCHA requires verification")
    context = FakeContext(tmp_path)

    with pytest.raises(WaitingForHuman, match="CAPTCHA") as caught:
        asyncio.run(ArenaAdapter().execute(context, FakeBrowser(page)))

    assert page.send_clicks == 0
    assert page.closed
    assert caught.value.details["human_gate"] == "captcha"
    screenshot = context.run_dir / caught.value.details["screenshot"]
    assert screenshot.is_file()


def test_ambiguous_response_articles_fail_closed_for_human(tmp_path):
    prompt = "Return the answer exactly."
    page = FakePage(response="ignored")
    page.articles = [
        FakeArticle(prompt),
        FakeArticle("one possible assistant turn"),
        FakeArticle("another possible assistant turn"),
    ]
    context = FakeContext(
        tmp_path,
        state={
            "submission_state": "submitted",
            "current_url": page.url,
            "interaction": {"submission_state": "submitted", "current_url": page.url},
        },
        prompt=prompt,
    )

    with pytest.raises(WaitingForHuman, match="more than one article"):
        asyncio.run(ArenaAdapter().execute(context, FakeBrowser(page)))
    assert page.send_clicks == 0
