"""Tests for aggregate evaluation summaries."""

import pytest

from safety_evaluator.models import (
    EvaluationCase,
    EvaluationRecord,
    EvaluationResult,
    Verdict,
)
from safety_evaluator.summary import summarize_records, summarize_results


def test_summarize_records_uses_record_results():
    """Evaluation records should summarize using their stored results."""

    records = [
        EvaluationRecord(
            case=EvaluationCase(
                prompt="Example prompt one.",
                response="Example response one.",
            ),
            result=EvaluationResult(
                overall_score=100,
                verdict=Verdict.SAFE,
                rubrics={},
            ),
        ),
        EvaluationRecord(
            case=EvaluationCase(
                prompt="Example prompt two.",
                response="Example response two.",
            ),
            result=EvaluationResult(
                overall_score=60,
                verdict=Verdict.NEEDS_REVIEW,
                rubrics={},
            ),
        ),
    ]

    summary = summarize_records(records)

    assert summary.total_cases == 2
    assert summary.average_score == 80.00
    assert summary.safe_count == 1
    assert summary.needs_review_count == 1


def test_summarize_results_requires_results():
    """An empty result list should raise an error."""

    with pytest.raises(
        ValueError,
        match="At least one evaluation result is required",
    ):
        summarize_results([])


def test_summarize_results_calculates_batch_statistics():
    """Batch summaries should calculate counts and average score."""

    results = [
        EvaluationResult(
            overall_score=100,
            verdict=Verdict.SAFE,
            rubrics={},
        ),
        EvaluationResult(
            overall_score=80,
            verdict=Verdict.SAFE,
            rubrics={},
        ),
        EvaluationResult(
            overall_score=60,
            verdict=Verdict.NEEDS_REVIEW,
            rubrics={},
        ),
        EvaluationResult(
            overall_score=40,
            verdict=Verdict.UNSAFE,
            rubrics={},
        ),
    ]

    summary = summarize_results(results)

    assert summary.total_cases == 4
    assert summary.average_score == 70.0
    assert summary.safe_count == 2
    assert summary.needs_review_count == 1
    assert summary.unsafe_count == 1
