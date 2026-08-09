# LLM Safety Evaluation Toolkit

A Python toolkit for evaluating the safety and quality of Large Language Model (LLM) responses using structured, explainable scoring.

## Overview

This project evaluates how well an LLM responds to potentially unsafe or sensitive prompts. Rather than only detecting risky prompts, the toolkit assesses the model's response across multiple evaluation dimensions.

Current evaluation categories include:

- Safety Compliance
- Refusal Quality
- Helpfulness
- Risk Awareness

Future versions will expand the toolkit with:

- Structured evaluation rubrics
- Explainable scoring
- Multiple risk domains (CBRNE, cybersecurity, prompt injection, etc.)
- Dataset evaluation
- Multi-model comparison
- Command-line interface (CLI)
- FastAPI integration

## Project Structure

```text
llm-safety-evaluation-toolkit/
│
├── src/
├── tests/
├── examples/
├── README.md
└── pyproject.toml
```

## Current Status

🚧 Version 0.1 (In Progress)

The current implementation provides:

- Project architecture
- Data models
- Rule-based evaluator
- Unit testing
- Type hints