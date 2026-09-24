# ce-stranger-replay-v1

[![Public fixture verification](https://github.com/thisisntjon/ce-stranger-replay-v1/actions/workflows/public-fixture.yml/badge.svg)](https://github.com/thisisntjon/ce-stranger-replay-v1/actions/workflows/public-fixture.yml)

A public, synthetic replay of a bounded Consumption Engine evidence workflow.

This repository contains only the fixture and the code needed to run it. It does not contain the private Consumption Engine runtime, private archives, customer material, TheLibrary, HistoryLab, workstation caches, or credentials.

## Run it

Requirements: Python 3.11 or newer. No third-party packages or network access are required after cloning.

```powershell
python examples/public_demo/run_public_demo.py --output .tmp/public-demo-run
python examples/public_demo/compare_baseline.py --output .tmp/public-comparison
```

The runner preserves an original 3-retry claim, carries a correction to 2 retries, refuses stale context, checks a successor, returns UNKNOWN / INSUFFICIENT_EVIDENCE for an unsupported question, and verifies an archive replay. The fixture is synthetic and manually annotated.

The generated result includes REPORT.md, RESULT.json, RECEIPT.json, and the sealed archive. FIXTURE-MANIFEST.json pins the committed fixture bytes. ORACLES.json pins the expected status projection. verify_receipt.py checks exact input pins and that projection. That is an automated integrity check, not semantic truth, human acceptance, or production qualification.

A non-author reviewer can follow NON_AUTHOR_REVIEW.md to run the package twice from fresh output directories and bind the results to the exact receipts and oracle hashes. The review scope is the published synthetic workflow only.

The public verification workflow covers Ubuntu, Windows and macOS with Python
3.11, 3.12 and 3.13. Its artifacts contain machine-readable replay receipts
and oracle decisions. A passing workflow establishes hosted replay of this
fixture; it does not establish product efficacy or human acceptance.

See [REPRODUCIBILITY.md](REPRODUCIBILITY.md), [SECURITY.md](SECURITY.md) and
[CITATION.cff](CITATION.cff) for the release boundary, reporting route and
citation metadata.

## Boundaries

This package does not establish automatic claim extraction, scientific truth, general retrieval quality, customer value, production readiness, or clean-machine recovery. The private product runtime remains separate. Any later qualification must name its package commit, commands, hashes, environment boundary, and limitations.
