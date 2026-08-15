"""Tests for aggregate evaluation summaries."""

import pytest

from safety_evaluator.models import EvaluationResult, Verdict
from safety_evaluator.summary import summarize_results


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
