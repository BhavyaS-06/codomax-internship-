# Prompt Testing Report

## Objective
Compare prompt styles and define a repeatable way to review their outputs.

## Test cases

| Test | Prompt approach | Expected behavior | Evaluation criteria |
|---|---|---|---|
| 1 | Zero-shot sentiment classification | Return a sentiment label without examples | Correctness, relevance |
| 2 | Few-shot sentiment classification | Follow labels shown in examples | Correctness, consistency |
| 3 | Role-based explanation | Explain a topic for a specified audience | Clarity, usefulness |
| 4 | Structured JSON request | Return the requested keys and valid JSON | Validity, completeness |
| 5 | Summarization template | Keep main ideas without adding unsupported facts | Faithfulness, brevity |
| 6 | Classification template | Choose only from supplied categories | Correctness, format |
| 7 | Coding/debugging prompt | Explain an issue and propose a correction | Correctness, testability |

## Evaluation scale
Score each criterion from 1 to 5:
- 1 = Poor
- 2 = Needs improvement
- 3 = Acceptable
- 4 = Good
- 5 = Excellent

## Results template

| Test | Accuracy (1-5) | Clarity (1-5) | Format followed (1-5) | Notes |
|---|---:|---:|---:|---|
| Zero-shot | ___ | ___ | ___ | ___ |
| Few-shot | ___ | ___ | ___ | ___ |
| Role-based | ___ | ___ | ___ | ___ |
| JSON | ___ | ___ | ___ | ___ |
| Summarization | ___ | ___ | ___ | ___ |
| Classification | ___ | ___ | ___ | ___ |
| Coding/debugging | ___ | ___ | ___ | ___ |

## Conclusion
A more specific prompt can help make the task and expected format clearer, but it does not guarantee factual correctness. Important outputs should be checked by a person. This repository demonstrates prompt design and evaluation; it does not connect to a live AI model.
