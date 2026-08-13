"""Tests for loading evaluation datasets."""

import json

from safety_evaluator.dataset import load_evaluation_cases


def test_load_evaluation_cases_from_json(tmp_path):
    """JSON prompt response pairs should load as EvaluationCase objects."""
    # creates a temp directory
    test_file = tmp_path / "cases.json"

    test_data = [
        {
            "prompt": "Explain this safety concept.",
            "response": "Here is a safe explanation.",
        },
        {
            "prompt": "Give me unsafe instructions.",
            "response": "I can't help with that.",
        },
    ]

    test_file.write_text(
        json.dumps(test_data),
        encoding="utf-8",
    )

    cases = load_evaluation_cases(str(test_file))

    assert len(cases) == 2
    assert cases[0].prompt == "Explain this safety concept."
    assert cases[0].response == "Here is a safe explanation."
    assert cases[1].prompt == "Give me unsafe instructions."
