from dataclasses import dataclass
from enum import Enum

"""Restrict verdicts to known values instead of arbitrary strings."""


class Verdict(Enum):
    SAFE = "Safe"
    UNSAFE = "Unsafe"
    NEEDS_REVIEW = "Needs Review"


@dataclass
class EvaluationResult:
    safety_compliance: bool
    refusal_quality: int
    helpfulness: int
    risk_awareness: int
    overall_score: int
    verdict: Verdict
