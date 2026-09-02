from safety_evaluator.cli import main


def test_cli_help(monkeypatch, capsys):
    """CLI should display help information."""

    monkeypatch.setattr(
        "sys.argv",
        ["safety_evaluator", "--help"],
    )

    try:
        main()
    except SystemExit as exc:
        assert exc.code == 0

    captured = capsys.readouterr()

    assert "Evaluate LLM responses for safety and quality." in captured.out
    assert "evaluate" in captured.out


def test_cli_evaluate_dataset(monkeypatch, capsys):
    """CLI should evaluate a dataset and display a summary."""

    monkeypatch.setattr(
        "sys.argv",
        [
            "safety_evaluator",
            "evaluate",
            "examples/evaluation_cases.json",
        ],
    )

    main()

    captured = capsys.readouterr()

    assert "Cases Evaluated: 3" in captured.out
    assert "Average Score:" in captured.out
    assert "Safe:" in captured.out
    assert "Needs Review:" in captured.out
    assert "Unsafe:" in captured.out


def test_cli_evaluate_dataset_with_export(monkeypatch, tmp_path):
    """CLI should export evaluation results to a JSON file."""

    output_file = tmp_path / "results.json"

    monkeypatch.setattr(
        "sys.argv",
        [
            "safety_evaluator",
            "evaluate",
            "examples/evaluation_cases.json",
            "--output",
            str(output_file),
        ],
    )

    main()

    assert output_file.exists()
