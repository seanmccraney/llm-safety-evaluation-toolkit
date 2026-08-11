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
