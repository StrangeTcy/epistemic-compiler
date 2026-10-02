from __future__ import annotations

import asyncio
import sys
from types import ModuleType
from pathlib import Path

from runtime.browser.browser import (
    BROWSER_CHANNEL_ENV,
    PROFILE_ROOT,
    PROJECT_ROOT,
    BrowserController,
)


class FakeContext:
    def __init__(self):
        self.default_timeout = None
        self.closed = False

    def set_default_timeout(self, timeout):
        self.default_timeout = timeout

    async def close(self):
        self.closed = True


class FakeChromium:
    def __init__(self):
        self.options = None
        self.context = FakeContext()

    async def launch_persistent_context(self, **options):
        self.options = options
        return self.context


class FakePlaywright:
    def __init__(self):
        self.chromium = FakeChromium()
        self.stopped = False

    async def stop(self):
        self.stopped = True


class FakePlaywrightStarter:
    def __init__(self, playwright):
        self.playwright = playwright

    async def start(self):
        return self.playwright


def install_fake_playwright(monkeypatch):
    playwright = FakePlaywright()
    starter = FakePlaywrightStarter(playwright)
    package = ModuleType("playwright")
    package.__path__ = []
    async_api = ModuleType("playwright.async_api")
    async_api.async_playwright = lambda: starter
    monkeypatch.setitem(sys.modules, "playwright", package)
    monkeypatch.setitem(sys.modules, "playwright.async_api", async_api)
    return playwright


def test_default_profile_uses_isolated_chrome_directory_and_is_shared_by_login_and_run(
    monkeypatch,
):
    monkeypatch.delenv(BROWSER_CHANNEL_ENV, raising=False)
    login = BrowserController("arena", headless=False)
    runner = BrowserController("arena", headless=True)

    expected_root = PROJECT_ROOT / "runtime" / "browser_profiles"
    expected_profile = expected_root / "chrome-arena"
    assert PROFILE_ROOT == expected_root
    assert login.browser_channel == "chrome"
    assert login.playwright_channel == "chrome"
    assert login.profile_path == expected_profile
    assert runner.profile_path == login.profile_path
    assert login.headless is False
    assert runner.headless is True


def test_environment_can_select_playwright_bundled_chromium(tmp_path, monkeypatch):
    monkeypatch.setenv(BROWSER_CHANNEL_ENV, "chromium")
    controller = BrowserController("arena", profile_root=tmp_path)

    assert controller.browser_channel == "chromium"
    assert controller.playwright_channel is None
    assert controller.profile_path == tmp_path / "chromium-arena"


def test_explicit_browser_channel_overrides_environment(tmp_path, monkeypatch):
    monkeypatch.setenv(BROWSER_CHANNEL_ENV, "chromium")
    controller = BrowserController(
        "arena", profile_root=tmp_path, channel="chrome-beta"
    )

    assert controller.browser_channel == "chrome-beta"
    assert controller.playwright_channel == "chrome-beta"
    assert controller.profile_path == tmp_path / "chrome-beta-arena"


def test_default_launch_uses_installed_chrome_and_separate_profile(
    tmp_path, monkeypatch
):
    monkeypatch.delenv(BROWSER_CHANNEL_ENV, raising=False)
    fake_playwright = install_fake_playwright(monkeypatch)
    controller = BrowserController("arena", profile_root=tmp_path, headless=False)

    async def start_and_close():
        await controller.start()
        await controller.close()

    asyncio.run(start_and_close())

    options = fake_playwright.chromium.options
    assert options is not None
    assert options["channel"] == "chrome"
    assert options["user_data_dir"] == str(tmp_path / "chrome-arena")
    assert options["headless"] is False
    assert options["viewport"] is None
    assert options["accept_downloads"] is True
    assert "executable_path" not in options
    assert fake_playwright.chromium.context.default_timeout == 15_000
    assert fake_playwright.chromium.context.closed
    assert fake_playwright.stopped


def test_bundled_chromium_launch_omits_branded_channel_and_executable_override(
    tmp_path, monkeypatch
):
    fake_playwright = install_fake_playwright(monkeypatch)
    controller = BrowserController(
        "arena", profile_root=tmp_path, channel="chromium", headless=False
    )

    async def start_and_close():
        await controller.start()
        await controller.close()

    asyncio.run(start_and_close())

    options = fake_playwright.chromium.options
    assert options is not None
    assert "channel" not in options
    assert options["user_data_dir"] == str(tmp_path / "chromium-arena")
    assert "executable_path" not in options
