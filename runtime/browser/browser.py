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
# This is a dedicated Playwright automation profile, never Chrome's normal user
# profile. The directory is ignored by Git because it can contain authenticated
# site state (including cookies).
PROFILE_ROOT = PROJECT_ROOT / "runtime" / "browser_profiles"
DEFAULT_BROWSER_CHANNEL = "chrome"
BROWSER_CHANNEL_ENV = "EPISTEMIC_BROWSER_CHANNEL"


def resolve_browser_channel(channel: str | None = None) -> str:
    """Resolve the configured Playwright browser channel.

    ``chrome`` uses the installed stable Chrome through Playwright's
    branded-browser support. ``chromium`` deliberately omits Playwright's
    ``channel`` argument and uses its downloaded Chromium build, preserving the
    original backend.
    """
    selected = channel
    if selected is None:
        selected = os.environ.get(BROWSER_CHANNEL_ENV) or DEFAULT_BROWSER_CHANNEL
    if not isinstance(selected, str):
        raise ValueError("browser channel must be a string")
    selected = selected.strip().lower()
    if not selected:
        selected = DEFAULT_BROWSER_CHANNEL
    if not re.fullmatch(r"[a-z0-9][a-z0-9._-]{0,63}", selected):
        raise ValueError("browser channel must be a simple Playwright channel name")
    return selected


def playwright_channel(channel: str) -> str | None:
    """Return the channel argument; ``None`` selects bundled Playwright Chromium."""
    return None if channel == "chromium" else channel


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
    """One persistent, isolated browser profile shared by site-adapter pages."""

    def __init__(
        self,
        profile_id: str,
        *,
        profile_root: Path = PROFILE_ROOT,
        channel: str | None = None,
        headless: bool = False,
        timeout_ms: int = 15_000,
    ) -> None:
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}", profile_id):
            raise ValueError("profile_id must be a simple filesystem-safe identifier")
        self.profile_id = profile_id
        self.browser_channel = resolve_browser_channel(channel)
        self.playwright_channel = playwright_channel(self.browser_channel)
        self.profile_root = profile_root.expanduser().resolve()
        self.profile_path = (
            self.profile_root / f"{self.browser_channel}-{profile_id}"
        ).resolve()
        if self.profile_path.parent != self.profile_root:
            raise ValueError("persistent browser profile path escaped its configured root")
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
                message = "Playwright is not installed. Install runtime/requirements.txt."
                if self.browser_channel == "chromium":
                    message += " Then run `python -m playwright install chromium`."
                raise BrowserStartupError(message) from exc
            self.profile_path.mkdir(parents=True, exist_ok=True)
            try:
                self._playwright = await async_playwright().start()
                launch_options: dict[str, Any] = {
                    "user_data_dir": str(self.profile_path),
                    "headless": self.headless,
                    "viewport": None,
                    "accept_downloads": True,
                }
                if self.playwright_channel is not None:
                    launch_options["channel"] = self.playwright_channel
                self._context = (
                    await self._playwright.chromium.launch_persistent_context(
                        **launch_options
                    )
                )
                self._context.set_default_timeout(self.timeout_ms)
            except Exception as exc:
                if self._playwright is not None:
                    await self._playwright.stop()
                    self._playwright = None
                hint = (
                    " Install Playwright's bundled Chromium with `python -m playwright install chromium` "
                    "if EPISTEMIC_BROWSER_CHANNEL=chromium is selected."
                    if self.browser_channel == "chromium"
                    else " Verify that the selected local browser channel is installed."
                )
                raise BrowserStartupError(
                    f"Could not launch browser channel {self.browser_channel!r} "
                    f"with persistent profile {self.profile_path}: {exc}.{hint}"
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
