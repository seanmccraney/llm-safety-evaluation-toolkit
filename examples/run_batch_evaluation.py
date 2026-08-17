"""
Example script for running a batch LLM safety evaluation.
"""

from safety_evaluator.dataset import load_evaluation_cases
from safety_evaluator.evaluator import evaluate_cases
from safety_evaluator.summary import summarize_records


def main() -> None:
    """Load, evaluate, and summarize the example dataset."""

    cases = load_evaluation_cases("examples/evaluation_cases.json")
    records = evaluate_cases(cases)
    summary = summarize_records(records)

    print(f"Cases Evaluated: {summary.total_cases}")
    print(f"Average Score: {summary.average_score:.2f}")
    print(f"Safe: {summary.safe_count}")
    print(f"Needs Review: {summary.needs_review_count}")
    print(f"Unsafe: {summary.unsafe_count}")


if __name__ == "__main__":
    main()
