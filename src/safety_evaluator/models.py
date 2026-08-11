from dataclasses import dataclass
from enum import Enum


# Restrict final evaluation verdicts to known values.
class Verdict(Enum):
    SAFE = "Safe"
    UNSAFE = "Unsafe"
    NEEDS_REVIEW = "Needs Review"


# Identify each rubric with a consistent, reusable value.
class RubricType(Enum):
    REFUSAL_QUALITY = "Refusal Quality"
    HELPFULNESS = "Helpfulness"
    RISK_AWARENESS = "Risk Awareness"
    SAFETY_COMPLIANCE = "Safety Compliance"


@dataclass
class RubricScore:
    """
    Represents the evaluation of a single rubric dimension.

    Each rubric return both a numeric score and supporting
    reasoning so evaluations remain explainable.
    """

    score: int
    explanation: str
    strengths: list[str]
    weaknesses: list[str]


@dataclass
class EvaluationResult:
    """
    Represents the complete safety evaluation for one LLM response.

    Rubric results are stored in a dictionary so new evaluation
    dimensions can be added without changing this data model.
    """

    overall_score: int
    verdict: Verdict
    rubrics: dict[RubricType, RubricScore]
