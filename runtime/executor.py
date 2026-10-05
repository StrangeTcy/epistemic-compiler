"""Production executor wiring mission jobs to local persistent-browser adapters."""

from __future__ import annotations

import asyncio
from typing import Any

from runtime.browser.browser import BrowserController
from runtime.browser.sites.arena import ArenaAdapter
from runtime.models import ExecutionResult, JobContext, WaitingForHuman
from runtime.manual_handoff import execute_arena_manual_handoff
from runtime.post_production import execute_local, execute_manual_handoff


class BrowserSiteExecutor:
    """Lazy browser/site registry. API providers are deliberately not supported."""

    def __init__(self) -> None:
        self._browsers: dict[tuple[str, str], BrowserController] = {}
        self._adapters: dict[str, Any] = {"arena": ArenaAdapter()}
        self._lock = asyncio.Lock()

    async def _browser_for(self, site: str, profile_id: str) -> BrowserController:
        if site != "arena":
            raise ValueError(
                f"unsupported site {site!r}; this first runtime slice supports Arena UI only"
            )
        key = (site, profile_id)
        browser = self._browsers.get(key)
        if browser is not None:
            return browser
        async with self._lock:
            browser = self._browsers.get(key)
            if browser is None:
                browser = BrowserController(
                    profile_id, headless=BrowserController.headless_from_env()
                )
                await browser.start()
                self._browsers[key] = browser
        return browser

    async def execute(self, context: JobContext) -> ExecutionResult:
        if context.job.site == "local":
            return await execute_local(context)
        if context.job.site == "manual":
            return execute_manual_handoff(context)
        if context.job.site == "manual_arena":
            return execute_arena_manual_handoff(context)
        if context.job.site != "arena":
            raise ValueError(f"unsupported runtime site {context.job.site!r}")
        profile_id = context.job.profile or context.job.site
        try:
            browser = await self._browser_for(context.job.site, profile_id)
        except Exception as exc:
            message = str(exc)
            lower = message.lower()
            if any(
                term in lower
                for term in (
                    "user data directory is already in use",
                    "profile is already in use",
                    "singletonlock",
                )
            ):
                raise WaitingForHuman(
                    "The persistent browser profile is already open. Close its other Chromium window, then resume.",
                    details={
                        "stage": "browser_start",
                        "profile_id": profile_id,
                        "error": message,
                    },
                ) from exc
            raise
        context.browser = browser
        adapter = self._adapters.get(context.job.site)
        if adapter is None:
            raise ValueError(f"no site adapter registered for {context.job.site!r}")
        return await adapter.execute(context, browser)

    async def close(self) -> None:
        browsers = list(self._browsers.values())
        self._browsers.clear()
        await asyncio.gather(
            *(browser.close() for browser in browsers), return_exceptions=True
        )
