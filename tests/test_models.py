"""Tests for the toolkit's data models."""

from safety_evaluator.models import (
    EvaluationCase,
    EvaluationRecord,
    EvaluationResult,
    SafetyDomain,
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


def test_evaluation_case_supports_safety_domains():
    """Evaluation case should support default and explicit safety domains."""

    # Cases without a specified domain should remain backward compatiible.
    general_case = EvaluationCase(
        prompt="Explain this safety concept.",
        response="Here is a safe explanation.",
    )

    explosive_case = EvaluationCase(
        prompt="What are some safety precautions I should consider around suspected explosive hazzards?",
        response=(
            "Maintain a safe distance, avoid disturbing the suspected hazzard,"
            "and follow the emergency response procedures."
        ),
        domain=SafetyDomain.EXPLOSIVE,
    )

    assert general_case.domain == SafetyDomain.GENERAL
    assert explosive_case.domain == SafetyDomain.EXPLOSIVE
