# Non-author review checklist

Use a fresh clone and only the committed synthetic fixture. Follow the [README quickstart](README.md#run-the-released-fixture) to select the released commit before running the review commands below. Record the full commit from `git rev-parse HEAD` with your review.

## Run

From the repository root, with Python 3.11 or newer:

```text
python examples/public_demo/run_public_demo.py --output .tmp/review-run-a
python examples/public_demo/run_public_demo.py --output .tmp/review-run-b
python examples/public_demo/verify_receipt.py .tmp/review-run-a/RECEIPT.json --output .tmp/review-run-a/ORACLE-DECISION.json
python examples/public_demo/verify_receipt.py .tmp/review-run-b/RECEIPT.json --output .tmp/review-run-b/ORACLE-DECISION.json
```

Each output directory must be new. Both runners should exit with code 0 and print `"passed": true`. Both receipt checks should exit with code 0 and report `accepted_automated_oracle`, with all six checks true. Compare both `oracle_projection` objects; they must match. Exact receipt and archive hashes may differ because a run records environment, timestamps and paths.

## Acceptance criteria

1. The fixture manifest and input hashes match ORACLES.json.
2. The initial answer is 3 retries and the corrected answer is 2 retries.
3. The old snapshot is unavailable after correction.
4. The successor state is checked_current.
5. The frozen unsupported-case rubric has no claim IDs and the receipt projects `UNKNOWN / INSUFFICIENT_EVIDENCE`. Record this as a constructed fixture label, not an executed unsupported-question lookup.
6. The source root is unavailable during restore verification.
7. Both runs produce the same oracle projection.
8. No private path, network share, live provider, or workstation cache is needed.

Check the executed lifecycle in `RESULT.json`, the task records and `restored/restore-check.json`; receipt projection equality alone is not a fresh behavioral test. The restore guard is a Python mechanism on the same host and interpreter. The receipt's `offline_declared` check is not evidence of operating-system network isolation.

Return a review decision that names the reviewer and session, binds the exact receipt and oracle hashes, and states the scope. Do not upgrade the result to scientific truth, production readiness, or general efficacy. Identify any relationship to the author or development effort; a separate review task is not automatically independent reproduction.
