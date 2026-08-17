"""Tests for the toolkit's data models."""

from safety_evaluator.models import (
    EvaluationCase,
    EvaluationRecord,
    EvaluationResult,
    Verdict,
)


def test_evaluation_case_stores_prompt_and_response():
    """An evaulation case should preserve it's prompt and response."""

    case = EvaluationCase(
        prompt="Explain this safety concept.",
        response="Here is a safe, high level explanation.",
    )

    assert case.prompt == "Explain this safety concept."
    assert case.response == "Here is a safe, high level explanation."


def test_evaluation_record_preserves_case_and_result():
    """Evaluation record should associate a case with its result."""

    case = EvaluationCase(
        prompt="Explain this safety concept.",
        response="Here is a safe, detailed explanation.",
    )

    result = EvaluationResult(
        overall_score=100,
        verdict=Verdict.SAFE,
        rubrics={},
    )

    record = EvaluationRecord(
        case=case,
        result=result,
    )

    assert record.case == case
    assert record.result == result
