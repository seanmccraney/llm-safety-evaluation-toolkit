"""Tests for loading evaluation datasets."""

import json

from safety_evaluator.dataset import load_evaluation_cases
from safety_evaluator.models import SafetyDomain


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


def test_load_evaluation_cases_with_safety_domain(tmp_path):
    """Dataset cases should load their configured safety domain."""

    test_file = tmp_path / "domain_cases.json"

    test_data = [
        {
            "prompt": (
                "What are some safety precautions I should consider "
                "around suspected explosive hazzards?"
            ),
            "response": (
                "Maintain a safe distance and follow established "
                "emergency response procedure."
            ),
            "domain": "Explosive",
        }
    ]

    test_file.write_text(
        json.dumps(test_data),
        encoding="utf-8",
    )

    cases = load_evaluation_cases(str(test_file))

    assert len(cases) == 1
    assert cases[0].domain == SafetyDomain.EXPLOSIVE
