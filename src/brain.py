import json
import re
from datetime import date

from src.config import BRAIN_PATH, LEARNINGS_PATH

MAX_ACTION_ITEMS = 5


def load_brain() -> dict:
    if BRAIN_PATH.exists():
        with open(BRAIN_PATH) as f:
            brain = json.load(f)
        _normalize_topics(brain)
        return brain
    return {"version": 1, "topics": [], "processed_urls": []}


def _normalize_topics(brain: dict) -> None:
    """Migrate legacy `bullets` into `action_items` and drop unused fields."""
    for topic in brain.get("topics", []):
        if "action_items" not in topic:
            topic["action_items"] = topic.pop("bullets", [])
        else:
            topic.pop("bullets", None)
        topic.pop("sources", None)
        topic.pop("relevance_to_brands", None)


def save_brain(brain: dict) -> None:
    _normalize_topics(brain)
    BRAIN_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(BRAIN_PATH, "w") as f:
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
    """Replace the brain with Claude's revised actionable playbook.

    Each run returns the complete revised brain for topics worth keeping.
    We replace action_items (and the topic set) rather than appending forever.
    Topics Claude omits are dropped — used to prune non-actionable FYI residue.
    """
    today = date.today().isoformat()
    revised_topics = updates.get("topics") or []
    if not revised_topics:
        # No revision payload — leave brain unchanged
        return

    new_topics = []
    for topic_update in revised_topics:
        topic_id = topic_update.get("id") or _slugify(topic_update.get("title", "topic"))
        items = [
            i.strip()
            for i in (topic_update.get("action_items") or topic_update.get("bullets") or [])
            if i and str(i).strip()
        ][:MAX_ACTION_ITEMS]
        if not items:
            continue

        new_topics.append(
            {
                "id": topic_id,
                "title": topic_update.get("title") or topic_id,
                "action_items": items,
                "last_updated": today,
            }
        )

    brain["topics"] = sorted(
        new_topics,
        key=lambda t: (t.get("title") or "").lower(),
    )

def _generate_learnings_md(brain: dict) -> None:
    LEARNINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# SEO Brain — Running Learnings\n"]
    lines.append(
        "Condensed action playbook. Revised each morning — bullets are updated in place, not appended forever.\n"
    )

    topics = sorted(brain.get("topics", []), key=lambda t: (t.get("title") or "").lower())
    if not topics:
        lines.append("_No learnings yet. They'll appear here after the first briefing._\n")
    else:
        for topic in topics:
            lines.append(f"## {topic['title']}\n")
            items = topic.get("action_items") or []
            if not items:
                lines.append("- _(no action items yet)_")
            else:
                for item in items:
                    lines.append(f"- {item}")
            lines.append("")

    LEARNINGS_PATH.write_text("\n".join(lines))
