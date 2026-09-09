import json
import re
from datetime import date
from pathlib import Path

from src.config import BRAIN_PATH, LEARNINGS_PATH


def load_brain() -> dict:
    if BRAIN_PATH.exists():
        with open(BRAIN_PATH) as f:
            return json.load(f)
    return {"version": 1, "topics": [], "processed_urls": []}


def save_brain(brain: dict) -> None:
    BRAIN_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(BAIN_PATH, "w") as f:
        json.dump(brain, f, indent=2)
        f.write("\n")
    _generate_learnings_md(brain)


def filter_unprocessed(articles: list, brain: dict) -> list:
    processed = set(brain.get("processed_urls", []))
    return [a for a in articles if a.url not in processed]


def mark_processed(brain: dict, urls: list[str]) -> None:
    processed = set(brain.get("processed_urls", []))
    processed.update(urls)
    brain["processed_urls"] = sorted(processed)


def _slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:60] or "topic"


def apply_brain_updates(brain: dict, updates: dict) -> None:
    """Merge Claude's structured brain updates into brain.json."""
    today = date.today().isoformat()
    topics_by_id = {t["id"]: t for t in brain.get("topics", [])}

    for topic_update in updates.get("topics", []):
        topic_id = topic_update.get("id") or _slugify(topic_update.get("title", "topic"))

        if topic_id in topics_by_id:
            existing = topics_by_id[topic_id]
            for bullet in topic_update.get("bullets", []):
                if bullet not in existing.get("bullets", []):
                    existing.setdefault("bullets", []).append(bullet)
            existing["last_updated"] = today
            if topic_update.get("relevance_to_brands"):
                brands = set(existing.get("relevance_to_brands", []))
                brands.update(topic_update["relevance_to_brands"])
                existing["relevance_to_brands"] = sorted(brands)
        else:
            topics_by_id[topic_id] = {
                "id": topic_id,
                "title": topic_update.get("title", topic_id),
                "bullets": topic_update.get("bullets", []),
                "sources": topic_update.get("sources", []),
                "last_updated": today,
                "relevance_to_brands": topic_update.get("relevance_to_brands", []),
            }

    brain["topics"] = sorted(topics_by_id.values(), key=lambda t: t.get("last_updated", ""), reverse=True)


def _generate_learnings_md(brain: dict) -> None:
    LEARNINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# SEO Brain — Running Learnings\n"]

    topics = brain.get("topics", [])
    if not topics:
        lines.append("_No learnings yet. They'll appear here after the first briefing._\n")
    else:
        for topic in topics:
            lines.append(f"## {topic['title']}\n")
            lines.append(f"_Last updated: {topic.get('last_updated', 'unknown')}_\n")
            for bullet in topic.get("bullets", []):
                lines.append(f"- {bullet}")
            brands = topic.get("relevance_to_brands", [])
            if brands:
                lines.append(f"\n_Relevant to: {', '.join(brands)}_")
            lines.append("")

    LEARNINGS_PATH.write_text("\n".join(lines))
