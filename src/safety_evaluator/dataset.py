"""
Utilities for loading evaluation cases from dataset files.
"""

import json
from pathlib import Path

from safety_evaluator.models import EvaluationCase, SafetyDomain


def load_evaluation_cases(file_path: str) -> list[EvaluationCase]:
    """
    Load evaluation cases from a JSON file.

    Args:
        file_path: Path to a JSON file containing prompt response pairs.

    Returns:
        A list of structured EvaluationCase objects.
    """

    path = Path(file_path)
    # opens the file for reading, encodes with UTF-8, closes when done
    with path.open("r", encoding="utf-8") as file:
        # takes JSON from file and converts to python objects
        data = json.load(file)

    return [
        EvaluationCase(
            prompt=item["prompt"],
            response=item["response"],
            domain=SafetyDomain(item.get("domain", SafetyDomain.GENERAL.value)),
        )
        for item in data
    ]
