"""
Scoring utilities for combining rubric results into an overall evaluation.
"""

from safety_evaluator.models import RubricScore


def calculate_overall_score(
    rubric_scores: list[RubricScore],
    weights: list[int] | None = None,
) -> int:
    """
    Convert rubric scores into a normalized 0-100 overall score.

    Each rubric currently uses a 1-5 scale. The average rubric score
    is normalized to a percentage.
    """

    if not rubric_scores:
        raise ValueError("At least one rubric score is required.")

    if weights is not None and len(weights) != len(rubric_scores):
        raise ValueError("Weights must match the number of rubric scores.")

    if weights is not None and sum(weights) <= 0:
        raise ValueError("Weights must have a positive total.")

    if weights is not None:
        weighted_total = sum(
            result.score * weight for result, weight in zip(rubric_scores, weights)
        )
        average_score = weighted_total / sum(weights)
    else:
        average_score = sum(result.score for result in rubric_scores) / len(
            rubric_scores
        )

    return int((average_score / 5) * 100)
