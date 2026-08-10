from dataclasses import dataclass
from enum import Enum

"""Restrict verdicts to known values instead of arbitrary strings."""


class Verdict(Enum):
    SAFE = "Safe"
    UNSAFE = "Unsafe"
    NEEDS_REVIEW = "Needs Review"


@dataclass
class RubricScore:
    """
    Represents the result of evaluating one rubric dimension.

    The score gives the numeric result, while the explanation
    captures why that score was assigned.
    """

    score: int
    explanation: str


@dataclass
class EvaluationResult:
    safety_compliance: bool
    refusal_quality: int
    helpfulness: int
    risk_awareness: int
    overall_score: int
    verdict: Verdict
