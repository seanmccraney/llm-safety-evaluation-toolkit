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
    DOMAIN_SAFETY_AWARENESS = "Domain Safety Awareness"


class SafetyDomain(Enum):
    """Safety domains for evaluation cases."""

    GENERAL = "General"
    PROMPT_INJECTION = "Prompt Injection"
    CYBERSECURITY = "Cybersecurity"
    CHEMICAL = "Chemical"
    BIOLOGICAL = "Biological"
    RADIOLOGICAL_NUCLEAR = "Radiological/Nuclear"
    EXPLOSIVE = "Explosive"


@dataclass(frozen=True)
class DomainSafetyConfig:
    """
    Configuration used when evaluating a specific safety domian

    Attributes:
        phrases:
            safety related phrases associated with the domain.

        high_score_threshold:
            Number of phrase matches required for strong domain awareness.
    """

    phrases: tuple[str, ...]
    high_score_threshold: int = 1


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
class EvaluationCase:
    """
    Represents one prompt-response pair to be evaluated.

    Safety domain provides additional context that future
    evaluators can use when selecting specific domain logic.
    """

    prompt: str
    response: str
    # Default to GENERAL so existing datasets and EvaluationCase
    # objects remain compatible when there isn't a domain specified.
    domain: SafetyDomain = SafetyDomain.GENERAL


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


@dataclass
class EvaluationRecord:
    """
    Associates an evaluation case with its completed result.

    Keeping the orginal case along with the result keeps the
    context needed for reviewing and exporting batch evaluations.
    """

    case: EvaluationCase
    result: EvaluationResult


@dataclass
class EvaluationSummary:
    """
    Summarizes the results of evaluating a batch of cases.

    The summary provides stats the make it easier to understand
    overall model performance across a dataset.
    """

    total_cases: int
    average_score: float
    safe_count: int
    needs_review_count: int
    unsafe_count: int
