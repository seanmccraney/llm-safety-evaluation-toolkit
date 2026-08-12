"""
Utilities for converting structured evaluation results
into human-readable reports.
"""

from safety_evaluator.models import EvaluationResult


def format_evaluation_report(result: EvaluationResult) -> str:
    """
    Convert an EvaluationResult into a readable text report.

    Args:
        result: The completed evaluation to format.

    Returns:
        A formatted multi-line string describing the evaluation.
    """

    lines = [
        "LLM Safety Evaluation",
        "=" * 40,
        f"Overall Score: {result.overall_score}",
        f"Verdict: {result.verdict.value}",
        "",
    ]

    for rubric_type, rubric_score in result.rubrics.items():
        lines.extend(
            [
                rubric_type.value,
                f"Score: {rubric_score.score}/5",
                f"Explanation: {rubric_score.explanation}",
                "",
            ]
        )

    return "\n".join(lines)
