"""
Utilities for exporting evaluation results.
"""

import json

from safety_evaluator.models import EvaluationResult
from safety_evaluator.summary import summarize_results


def export_results_to_json(
    results: list[EvaluationResult],
    file_path: str,
) -> None:
    """
    Export evaluation results to a structured JSON file.

    Args:
        results: Evaluation results to export.
        file_path: Destination path for the JSON file.
    """

    export_data = []

    for result in results:
        rubric_data = {}

        for rubric_type, rubric_score in result.rubrics.items():
            rubric_data[rubric_type.value] = {
                "score": rubric_score.score,
                "explanation": rubric_score.explanation,
                "strengths": rubric_score.strengths,
                "weaknesses": rubric_score.weaknesses,
            }

        export_data.append(
            {
                "overall_score": result.overall_score,
                "verdict": result.verdict.value,
                "rubrics": rubric_data,
            }
        )

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(export_data, file, indent=2)


def export_batch_to_json(
    results: list[EvaluationResult],
    file_path: str,
) -> None:
    """
    Export batch evaluation results and aggregate summary stats.

    Args:
        results: Evaluation results to export.
        file_path: Destination path for JSON file.
    """

    summary = summarize_results(results)

    result_data = []

    for result in results:
        rubric_data = {}

        for rubric_type, rubric_score in result.rubrics.items():
            rubric_data[rubric_type.value] = {
                "score": rubric_score.score,
                "explanation": rubric_score.explanation,
                "strengths": rubric_score.strengths,
                "weaknesses": rubric_score.weaknesses,
            }

        result_data.append(
            {
                "overall_score": result.overall_score,
                "verdict": result.verdict.value,
                "rubrics": rubric_data,
            }
        )

    export_data = {
        "summary": {
            "total_cases": summary.total_cases,
            "average_score": summary.average_score,
            "safe_count": summary.safe_count,
            "needs_review_count": summary.needs_review_count,
            "unsafe_count": summary.unsafe_count,
        },
        "results": result_data,
    }

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(export_data, file, indent=2)
