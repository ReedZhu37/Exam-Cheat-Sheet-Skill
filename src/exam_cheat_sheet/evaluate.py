"""Strict, anchor-backed scoring of supplied grading records."""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

FINAL_WEIGHTS = {**{f'P1{letter}': (5 if letter == 'e' else 10) for letter in 'abcdefgh'},
                 **{f'P2{letter}': 10 for letter in 'abc'}}

def _number(value: object, label: str) -> float | int:
    if type(value) not in (int, float) or not math.isfinite(value) or value < 0:
        raise ValueError(f"{label} must be a finite nonnegative number")
    return value


def normalize_item_id(value: str) -> str:
    """Normalize P1a, P1(a), and 1a to the canonical P1a identifier."""
    compact = re.sub(r"\s+", "", value).lower()
    match = re.fullmatch(r"p?([1-9][0-9]*)(?:([a-z])|\(([a-z])\))?", compact)
    if match is None:
        raise ValueError(f"Invalid final item ID: {value}")
    return "P" + match[1] + (match[2] or match[3] or "")


def score_grading(data: dict | str | Path, out: str | Path | None = None) -> dict:
    """Score one A/B group without inferring answers or comparative improvement."""
    if isinstance(data, (str, Path)):
        data = json.loads(Path(data).read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("group") not in {"A", "B"}:
        raise ValueError("Grading requires group A or B")
    if not isinstance(data.get("items"), list) or not data["items"]:
        raise ValueError("Grading requires a nonempty items list")
    allow_partial = data.get("allow_partial", False)
    if type(allow_partial) is not bool:
        raise ValueError("allow_partial must be an exact boolean")
    if allow_partial:
        raise ValueError("Partial credit is unsupported: this scoring protocol is strict all-or-nothing")
    items = []
    seen = set()
    for item in data["items"]:
        if not isinstance(item, dict):
            raise ValueError("Each grading item must be an object")
        iid = item.get("item_id")
        if not isinstance(iid, str) or not iid.strip() or iid in seen:
            raise ValueError("Every grading item requires a unique nonempty string item_id")
        if data.get("benchmark") == "mit-6041-final":
            iid = normalize_item_id(iid)
            if iid in seen:
                raise ValueError("Duplicate normalized final item ID: " + iid)
        seen.add(iid)
        if type(item.get("correct")) is not bool:
            raise ValueError(f"{iid}: correct must be an exact boolean")
        for field in ("rationale", "official_anchor"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                raise ValueError(f"{iid}: nonempty {field} is required")
        maximum = _number(item.get("max_points"), f"{iid}: max_points")
        if maximum <= 0:
            raise ValueError(f"{iid}: max_points must be positive")
        default_award = maximum if item["correct"] else 0
        award = _number(item.get("awarded_points", default_award), f"{iid}: awarded_points")
        if award > maximum:
            raise ValueError(f"{iid}: awarded_points exceeds max_points")
        if award != default_award:
            raise ValueError(f"{iid}: awarded_points must match strict all-or-nothing correctness; no partial credit")
        items.append({"item_id": iid, "max_points": maximum, "correct": item["correct"],
                      "awarded_points": award, "rationale": item["rationale"], "official_anchor": item["official_anchor"]})
    maximum = sum(item["max_points"] for item in items)
    if data.get("benchmark") == "mit-6041-final":
        if len(items) != 11 or maximum != 105:
            raise ValueError("mit-6041-final requires exactly 11 final items totaling 105 maximum points")
        if {item['item_id']: item['max_points'] for item in items} != FINAL_WEIGHTS:
            raise ValueError('Final item IDs and weights must match P1(a-h), P2(a-c); only P1e is worth 5 points')
    correct_count = sum(item["correct"] for item in items)
    weighted = sum(item["awarded_points"] for item in items)
    result = {"benchmark": data.get("benchmark"), "group": data["group"], "allow_partial": allow_partial,
              "correct_count": correct_count, "item_count": len(items), "accuracy": correct_count / len(items),
              "weighted_points": weighted, "max_points": maximum, "weighted_fraction": weighted / maximum,
              "items": items,
              "interpretation": "Descriptive score for the supplied grading records; no improvement or causal claim."}
    if out is not None:
        destination = Path(out)
        destination.mkdir(parents=True, exist_ok=True)
        (destination / "score.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        lines = [f"# Score — group {data['group']}", "", f"Correct items: {correct_count}/{len(items)}.",
                 f"Weighted points: {weighted:g}/{maximum:g}.", "", result["interpretation"], ""]
        for item in items:
            lines.extend([f"## Item {item['item_id']}",
                          f"Correct: {str(item['correct']).lower()}; points: {item['awarded_points']:g}/{item['max_points']:g}.",
                          "Rationale: " + item["rationale"], "Official anchor: " + item["official_anchor"], ""])
        (destination / "score.md").write_text("\n".join(lines), encoding="utf-8")
    return result
