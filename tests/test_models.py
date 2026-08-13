"""Tests for the toolkit's data models."""

from safety_evaluator.models import EvaluationCase


def test_evaluation_case_stores_prompt_and_response():
    """An evaulation case should preserve it's prompt and response."""

    case = EvaluationCase(
        prompt="Explain this safety concept.",
        response="Here is a safe, high level explanation.",
    )

    assert case.prompt == "Explain this safety concept."
    assert case.response == "Here is a safe, high level explanation."
