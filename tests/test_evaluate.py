import copy
import json

import pytest

from exam_cheat_sheet.evaluate import FINAL_WEIGHTS, normalize_item_id, score_grading


def grading():
    return {"benchmark": "mit-6041-final", "group": "A", "items": [
        {"item_id": iid, "max_points": weight, "correct": i % 2 == 0,
         "rationale": "Synthetic scoring fixture.", "official_anchor": f"synthetic-key:item-{i + 1}"}
        for i, (iid, weight) in enumerate(FINAL_WEIGHTS.items())
    ]}


def test_strict_scoring_counts_and_weights_are_distinct(tmp_path):
    result = score_grading(grading(), tmp_path)
    assert result["correct_count"] == 6
    assert result["item_count"] == 11
    assert result["weighted_points"] == 55
    assert result["max_points"] == 105
    assert result["accuracy"] == pytest.approx(6 / 11)
    assert result["weighted_fraction"] == pytest.approx(55 / 105)
    assert json.loads((tmp_path / "score.json").read_text(encoding="utf-8")) == result
    assert "Official anchor: synthetic-key:item-1" in (tmp_path / "score.md").read_text(encoding="utf-8")


@pytest.mark.parametrize("incorrect_boolean", [0, 1, "true", "false", None])
def test_correct_requires_exact_boolean(incorrect_boolean):
    data = grading()
    data["items"][0]["correct"] = incorrect_boolean
    with pytest.raises(ValueError, match="exact boolean"):
        score_grading(data)


@pytest.mark.parametrize("field", ["rationale", "official_anchor"])
def test_missing_grading_justification_rejected(field):
    data = grading()
    data["items"][0][field] = " "
    with pytest.raises(ValueError, match=field):
        score_grading(data)


@pytest.mark.parametrize("change", ["item_count", "maximum", "duplicate"])
def test_final_benchmark_contract(change):
    data = grading()
    if change == "item_count":
        data["items"].pop()
    elif change == "maximum":
        data["items"][0]["max_points"] = 11
    else:
        data["items"][1]["item_id"] = "P1a"
    with pytest.raises(ValueError):
        score_grading(data)


def test_partial_credit_is_rejected_even_with_flag():
    data = grading()
    data["items"][1]["awarded_points"] = 4
    with pytest.raises(ValueError, match="partial credit"):
        score_grading(data)
    data["allow_partial"] = True
    with pytest.raises(ValueError, match="strict all-or-nothing"):
        score_grading(data)


def test_partial_credit_cannot_contradict_correctness():
    data = grading()
    data["items"][0]["awarded_points"] = 5
    with pytest.raises(ValueError, match="strict all-or-nothing"):
        score_grading(data)
    data = grading()
    data["items"][1]["awarded_points"] = 10
    with pytest.raises(ValueError, match="strict all-or-nothing"):
        score_grading(data)


@pytest.mark.parametrize("value", ["P1a", "P1(a)", "1a", "1(a)", "p1A", " P1 (a) "])
def test_final_item_id_normalization(value):
    assert normalize_item_id(value) == "P1a"


def test_normalized_alias_duplicates_are_rejected():
    data = grading()
    data["items"][0]["item_id"] = "P1a"
    data["items"][1]["item_id"] = "1(a)"
    with pytest.raises(ValueError, match="Duplicate normalized"):
        score_grading(data)


@pytest.mark.parametrize("invalid", [True, float("nan"), float("inf"), -1])
def test_invalid_points_rejected(invalid):
    data = grading()
    data["items"][0]["max_points"] = invalid
    with pytest.raises(ValueError):
        score_grading(data)


def test_both_groups_use_identical_scoring_without_improvement_claim():
    a = grading()
    b = copy.deepcopy(a)
    b["group"] = "B"
    assert score_grading(a)["weighted_points"] == score_grading(b)["weighted_points"]
    assert "no improvement" in score_grading(b)["interpretation"]


def test_final_weights_cannot_be_swapped_while_preserving_total():
    data = grading()
    data['items'][0]['max_points'] = 5
    data['items'][4]['max_points'] = 10
    with pytest.raises(ValueError, match='IDs and weights'):
        score_grading(data)
