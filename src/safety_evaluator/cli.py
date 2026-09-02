"""Command line interface for the LLM Safety Evaluation Toolkit."""

import argparse

from safety_evaluator.dataset import load_evaluation_cases
from safety_evaluator.evaluator import evaluate_cases
from safety_evaluator.export import export_evaluation_run
from safety_evaluator.summary import summarize_records


def main() -> None:
    """Run the CLI"""

    parser = argparse.ArgumentParser(
        description="Evaluate LLM responses for safety and quality."
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands",
    )

    evaluate_parser = subparsers.add_parser(
        "evaluate", help="Evaluate LLM responses from dataset."
    )

    evaluate_parser.add_argument(
        "dataset",
        help="Path to the JSON evaluation dataset.",
    )

    evaluate_parser.add_argument(
        "--output",
        help="Path to save evaluation results as JSON.",
    )

    args = parser.parse_args()

    if args.command == "evaluate":
        cases = load_evaluation_cases(args.dataset)
        records = evaluate_cases(cases)
        summary = summarize_records(records)

        if args.output:
            export_evaluation_run(
                records=records,
                file_path=args.output,
            )

        print(f"Cases Evaluated: {summary.total_cases}")
        print(f"Average Score: {summary.average_score:.2f}")
        print(f"Safe: {summary.safe_count}")
        print(f"Needs Review: {summary.needs_review_count}")
        print(f"Unsafe: {summary.unsafe_count}")
