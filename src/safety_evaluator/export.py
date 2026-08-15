"""
Utilities for exporting evaluation results.
"""

import json

from safety_evaluator.models import EvaluationResult


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
