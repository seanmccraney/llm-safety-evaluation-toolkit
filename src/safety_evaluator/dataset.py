"""
Utilities for loading evaluation cases from dataset files.
"""

import json
from pathlib import Path

from safety_evaluator.models import EvaluationCase


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
    # list comprehension, for every JSON object in data, creates
    # EvaluationCase
    return [
        EvaluationCase(
            prompt=item["prompt"],
            response=item["response"],
        )
        for item in data
    ]
