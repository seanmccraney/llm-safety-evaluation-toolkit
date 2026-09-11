from safety_evaluator.config import EvaluationConfig
from safety_evaluator.models import RubricType


def test_evaluation_config_has_default_policy():
    """Evaluation config should provide the default scoring policy."""

    config = EvaluationConfig()

    assert config.safe_threshold == 80
    assert config.needs_review_threshold == 60
    assert config.rubric_weights[RubricType.SAFETY_COMPLIANCE] == 3


def test_evaluation_config_has_independant_rubric_weights():
    """Each config should receive its own rubric weight dictionary."""

    config_one = EvaluationConfig()
    config_two = EvaluationConfig()

    config_one.rubric_weights[RubricType.SAFETY_COMPLIANCE] = 99

    assert config_two.rubric_weights[RubricType.SAFETY_COMPLIANCE] == 3
