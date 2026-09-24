"""Audit RSS feeds: fetch status and recent article counts."""

from __future__ import annotations

from collections import Counter
from datetime import datetime, timedelta, timezone

import feedparser
import httpx
import yaml

from src.config import CONFIG_PATH


def main() -> None:
    with open(CONFIG_PATH) as f:
        config = yaml.safe_load(f)

    cutoff_24h = datetime.now(timezone.utc) - timedelta(hours=24)
    cutoff_7d = datetime.now(timezone.utc) - timedelta(days=7)

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "application/rss+xml, application/xml, text/xml, */*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    }

    rows = []
    with httpx.Client(timeout=30, follow_redirects=True, headers=headers) as client:
        for feed in config["rss_feeds"]:
            name = feed["name"]
            url = feed["url"]
            status = "ok"
            entries = 0
            last_24h = 0
            last_7d = 0
            newest = None
            sample_title = ""

            try:
                response = client.get(url)
                if response.status_code >= 400:
                    status = f"HTTP {response.status_code}"
                else:
                    parsed = feedparser.parse(response.text)
                    entries = len(parsed.entries)
                    for entry in parsed.entries:
                        published = None
                        for field in ("published_parsed", "updated_parsed"):
                            parsed_t = entry.get(field)
                            if parsed_t:
                                published = datetime(*parsed_t[:6], tzinfo=timezone.utc)
                                break
                        if published is None:
                            continue
                        if newest is None or published > newest:
                            newest = published
                            sample_title = (entry.get("title") or "")[:60]
                        if published >= cutoff_24h:
                            last_24h += 1
                        if published >= cutoff_7d:
                            last_7d += 1
                    if entries == 0:
                        status = "empty/parse fail"
            except Exception as exc:
                status = f"error: {type(exc).__name__}"

            rows.append(
                {
                    "name": name,
                    "status": status,
                    "entries": entries,
                    "last_24h": last_24h,
                    "last_7d": last_7d,
                    "newest": newest.isoformat() if newest else "—",
                    "sample": sample_title,
                }
            )

    print(f"{'Source':<28} {'Status':<16} {'Feed':>5} {'24h':>4} {'7d':>4}  Newest")
    print("-" * 100)
    for r in rows:
        print(
            f"{r['name']:<28} {r['status']:<16} {r['entries']:>5} {r['last_24h']:>4} {r['last_7d']:>4}  {r['newest']}"
        )

    print("\n--- Summary ---")
    ok = [r for r in rows if r["status"] == "ok"]
    broken = [r for r in rows if r["status"] != "ok"]
    active_24h = [r for r in ok if r["last_24h"] > 0]
    quiet = [r for r in ok if r["last_24h"] == 0]
    print(f"Working feeds: {len(ok)}/{len(rows)}")
    print(f"Broken/blocked: {len(broken)} — {[r['name'] for r in broken]}")
    print(f"With posts in last 24h: {len(active_24h)} — {[(r['name'], r['last_24h']) for r in active_24h]}")
    print(f"Quiet (0 in 24h): {len(quiet)} — {[r['name'] for r in quiet]}")


if __name__ == "__main__":
    main()
