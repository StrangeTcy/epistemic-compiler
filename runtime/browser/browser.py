"""Generic Playwright browser controller.

This module deliberately contains no Arena selectors, URLs, or DOM assumptions.
Site adapters receive a BrowserPage and own all site-specific interaction logic.
"""

from __future__ import annotations

import asyncio
import os
import re
from collections.abc import Iterable
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_HOME = (
    Path(os.environ.get("XDG_DATA_HOME", str(Path.home() / ".local" / "share")))
    .expanduser()
    .resolve()
)
PROFILE_ROOT = DATA_HOME / "epistemic-compiler" / "browser_profiles" / PROJECT_ROOT.name
if PROFILE_ROOT.resolve().is_relative_to(PROJECT_ROOT):
    raise RuntimeError(
        "persistent browser profiles must be stored outside the repository"
    )


class BrowserStartupError(RuntimeError):
    pass


class BrowserPage:
    """Small generic facade around one Playwright page."""

    def __init__(self, page: Any) -> None:
        self._page = page

    @property
    def raw(self) -> Any:
        """Return the Playwright page for site adapters that need richer inspection."""
        return self._page

    @property
    def url(self) -> str:
        return str(self._page.url)

    async def title(self) -> str:
        return await self._page.title()

    async def goto(self, url: str, *, timeout_ms: int = 30_000) -> None:
        await self._page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)

    def by_role(
        self,
        role: str,
        name: str | re.Pattern[str] | None = None,
        *,
        exact: bool = False,
    ) -> Any:
        kwargs: dict[str, Any] = {"exact": exact}
        if name is not None:
            kwargs["name"] = name
        return self._page.get_by_role(role, **kwargs)

    def locator(self, selector: str) -> Any:
        """Create a generic DOM locator; semantics belong to the site adapter."""
        return self._page.locator(selector)

    async def body_text(self, *, timeout_ms: int = 5_000) -> str:
        try:
            return await self._page.locator("body").inner_text(timeout=timeout_ms)
        except Exception:
            return ""

    async def main_text(self, *, timeout_ms: int = 5_000) -> str:
        mains = self._page.get_by_role("main")
        try:
            count = await mains.count()
            if count == 1 and await mains.first.is_visible():
                return await mains.first.inner_text(timeout=timeout_ms)
        except Exception:
            pass
        return ""

    async def visible_text(self, locator: Any) -> list[str]:
        values: list[str] = []
        try:
            for item in await locator.all():
                if await item.is_visible():
                    value = (await item.inner_text()).strip()
                    if value:
                        values.append(value)
        except Exception:
            return values
        return values

    async def visible_count(self, locator: Any) -> int:
        count = 0
        try:
            for item in await locator.all():
                if await item.is_visible():
                    count += 1
        except Exception:
            return count
        return count

    async def screenshot(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        await self._page.screenshot(
            path=str(path), full_page=True, animations="disabled"
        )

    async def upload_files(
        self, paths: Iterable[Path], *, selector: str = 'input[type="file"]'
    ) -> None:
        """Use the browser's native file-input mechanism; no file data leaves this machine
        except through the current site's own upload UI.
        """
        locator = self._page.locator(selector)
        if await locator.count() != 1:
            raise BrowserStartupError(
                f"Expected one file input; found {await locator.count()}"
            )
        await locator.set_input_files([str(path) for path in paths])

    async def control_inventory(self, *, limit: int = 120) -> list[dict[str, str]]:
        """Return visible accessible control names for diagnostics, never credentials."""
        found: list[dict[str, str]] = []
        for role in (
            "button",
            "textbox",
            "link",
            "option",
            "menuitem",
            "checkbox",
            "radio",
        ):
            locator = self._page.get_by_role(role)
            try:
                items = await locator.all()
            except Exception:
                continue
            for item in items:
                if len(found) >= limit:
                    return found
                try:
                    if not await item.is_visible():
                        continue
                    label = (await item.get_attribute("aria-label")) or ""
                    text = (await item.inner_text()).strip().replace("\n", " ")
                    if not label:
                        label = text
                    if label:
                        found.append({"role": role, "name": label[:240]})
                except Exception:
                    continue
        return found

    async def close(self) -> None:
        try:
            await self._page.close()
        except Exception:
            pass


class BrowserController:
    """One persistent Chromium profile shared by one or more site-adapter pages."""

    def __init__(
        self,
        profile_id: str,
        *,
        profile_root: Path = PROFILE_ROOT,
        headless: bool = False,
        timeout_ms: int = 15_000,
    ) -> None:
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}", profile_id):
            raise ValueError("profile_id must be a simple filesystem-safe identifier")
        self.profile_id = profile_id
        self.profile_path = (profile_root.expanduser() / profile_id).resolve()
        if self.profile_path.is_relative_to(PROJECT_ROOT):
            raise ValueError(
                "persistent browser profiles must be stored outside the repository"
            )
        self.headless = headless
        self.timeout_ms = timeout_ms
        self._playwright: Any | None = None
        self._context: Any | None = None
        self._start_lock = asyncio.Lock()

    async def start(self) -> None:
        if self._context is not None:
            return
        async with self._start_lock:
            if self._context is not None:
                return
            try:
                from playwright.async_api import async_playwright
            except ImportError as exc:
                raise BrowserStartupError(
                    "Playwright is not installed. Install runtime/requirements.txt and run "
                    "`python -m playwright install chromium`."
                ) from exc
            self.profile_path.mkdir(parents=True, exist_ok=True)
            try:
                self._playwright = await async_playwright().start()
                self._context = (
                    await self._playwright.chromium.launch_persistent_context(
                        user_data_dir=str(self.profile_path),
                        headless=self.headless,
                        viewport=None,
                        accept_downloads=True,
                    )
                )
                self._context.set_default_timeout(self.timeout_ms)
            except Exception as exc:
                if self._playwright is not None:
                    await self._playwright.stop()
                    self._playwright = None
                raise BrowserStartupError(
                    f"Could not launch Chromium with profile {self.profile_id!r}: {exc}"
                ) from exc

    async def new_page(self) -> BrowserPage:
        await self.start()
        assert self._context is not None
        return BrowserPage(await self._context.new_page())

    async def close(self) -> None:
        if self._context is not None:
            try:
                await self._context.close()
            finally:
                self._context = None
        if self._playwright is not None:
            await self._playwright.stop()
            self._playwright = None

    @classmethod
    def headless_from_env(cls) -> bool:
        return os.environ.get("EPISTEMIC_BROWSER_HEADLESS", "0").strip().lower() in {
            "1",
            "true",
            "yes",
        }
