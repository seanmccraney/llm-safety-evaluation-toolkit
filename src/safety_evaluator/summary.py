"""
Utilities for summarizing batches of evaluation results.
"""

from safety_evaluator.models import (
    EvaluationResult,
    EvaluationSummary,
    Verdict,
)


def summarize_results(results: list[EvaluationResult]) -> EvaluationSummary:
    """
    Calculate aggregate stats for a batch of evaluation results.

    Args:
        results: Evaluation results to summarize.

    Returns:
        EvaluationSummary containing counts and the avg score.
    """

    total_cases = len(results)

    if total_cases == 0:
        raise ValueError("At least one evaluation result is required")

    average_score = sum(result.overall_score for result in results) / total_cases

    safe_count = sum(result.verdict == Verdict.SAFE for result in results)

    needs_review_count = sum(
        result.verdict == Verdict.NEEDS_REVIEW for result in results
    )

    unsafe_count = sum(result.verdict == Verdict.UNSAFE for result in results)

    return EvaluationSummary(
        total_cases=total_cases,
        average_score=average_score,
        safe_count=safe_count,
        needs_review_count=needs_review_count,
        unsafe_count=unsafe_count,
    )
