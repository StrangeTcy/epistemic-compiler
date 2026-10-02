#!/usr/bin/env python3
"""Open a persistent browser profile so the user can authenticate manually."""

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.browser.browser import BrowserController  # noqa: E402

SITES = {"arena": "https://arena.ai/"}


def _validate_site_url(site: str, value: str | None) -> str:
    if value is None:
        return SITES[site]
    parsed = urlparse(value)
    host = (parsed.hostname or "").lower()
    expected = urlparse(SITES[site]).hostname or ""
    if parsed.scheme != "https" or not (
        host == expected or host.endswith("." + expected)
    ):
        raise ValueError(f"--url must be an HTTPS URL on {expected}")
    if parsed.username or parsed.password:
        raise ValueError("--url must not contain embedded credentials")
    return value


async def _login(site: str, profile: str, target_url: str) -> int:
    browser = BrowserController(profile, headless=False)
    try:
        page = await browser.new_page()
        await page.goto(target_url)
        parsed = urlparse(target_url)
        print(
            f"Opened {parsed.scheme}://{parsed.netloc}{parsed.path} using persistent profile {profile!r}."
        )
        print(
            "Authenticate or complete any site verification manually in the Chromium window."
        )
        print(
            "The script does not inspect or print credentials; Chromium stores site session data in this local profile for reuse."
        )
        try:
            await asyncio.to_thread(
                input,
                "After the page is ready, press Enter here to close Chromium and save the profile: ",
            )
        except EOFError:
            print(
                "No interactive terminal input was available. Run this command from a terminal to keep the login window open."
            )
            return 2
        return 0
    finally:
        await browser.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", choices=sorted(SITES), help="site profile to open")
    parser.add_argument(
        "--profile", help="persistent profile identifier (defaults to the site name)"
    )
    parser.add_argument(
        "--url",
        help="optional saved page URL to inspect/complete manually (must be HTTPS on the selected site)",
    )
    args = parser.parse_args()
    try:
        target_url = _validate_site_url(args.site, args.url)
        return asyncio.run(_login(args.site, args.profile or args.site, target_url))
    except KeyboardInterrupt:
        return 130
    except Exception as exc:
        print(f"Browser login error: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
