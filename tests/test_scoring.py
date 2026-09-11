"""
Tests for overall rubric score calculations.
"""

import pytest

from safety_evaluator.models import RubricScore
from safety_evaluator.scoring import calculate_overall_score


def test_calculate_overall_score_from_multiple_rubrics():
    """Multiple rubric scores should be averaged and normalized."""

    rubric_scores = [
        RubricScore(
            score=5,
            explanation="Strong result.",
            strengths=[],
            weaknesses=[],
        ),
        RubricScore(
            score=3,
            explanation="Average result.",
            strengths=[],
            weaknesses=[],
        ),
    ]

    result = calculate_overall_score(rubric_scores)

    assert result == 80


def test_calculate_overall_score_requires_scores():
    """An empty rubric list should raise a clear error."""

    with pytest.raises(
        ValueError,
        match="At least one rubric score is required.",
    ):
        calculate_overall_score([])


def test_calculate_overall_score_with_weights():
    """Rubric weights should affect the overall score."""

    rubric_scores = [
        RubricScore(
            score=5,
            explanation="Strong result.",
            strengths=[],
            weaknesses=[],
        ),
        RubricScore(
            score=1,
            explanation="Weak result.",
            strengths=[],
            weaknesses=[],
        ),
    ]

    weights = [1, 3]

    result = calculate_overall_score(
        rubric_scores,
        weights=weights,
    )

    assert result == 40


def test_calculate_overall_score_requires_matching_weights():
    """Weights should match the number of rubric scores."""

    rubric_scores = [
        RubricScore(
            score=5,
            explanation="Strong result.",
            strengths=[],
            weaknesses=[],
        ),
        RubricScore(
            score=3,
            explanation="Average result.",
            strengths=[],
            weaknesses=[],
        ),
    ]

    with pytest.raises(
        ValueError,
        match="Weights must match the number of rubric scores.",
    ):
        calculate_overall_score(
            rubric_scores,
            weights=[1],
        )


def test_calculate_overall_score_requires_positive_total_weight():
    """Weights must have a positive total."""

    rubric_score = [
        RubricScore(
            score=5,
            explanation="Strong result.",
            strengths=[],
            weaknesses=[],
        ),
        RubricScore(
            score=3,
            explanation="Average result.",
            strengths=[],
            weaknesses=[],
        ),
    ]

    with pytest.raises(
        ValueError,
        match="Weights must have a positive total.",
    ):
        calculate_overall_score(
            rubric_score,
            weights=[0, 0],
        )
