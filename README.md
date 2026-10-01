# ce-stranger-replay-v1

[![Public fixture verification](https://github.com/thisisntjon/ce-stranger-replay-v1/actions/workflows/public-fixture.yml/badge.svg)](https://github.com/thisisntjon/ce-stranger-replay-v1/actions/workflows/public-fixture.yml)

A public, synthetic replay of a bounded Consumption Engine evidence workflow.

Follow one synthetic policy from an initial answer of 3 retries to a corrected answer of 2. Inspect the retained evidence, refusal of stale work, checked successor and guarded archive replay.

This repository contains the manually annotated fixture and the code needed to run it. No model or agent call is made. The private product runtime, research corpora and customer material are excluded.

## Released fixture and research boundary

The released fixture tag `v1.0.0-fixture` identifies commit `8374bb6ee93edef37f57f284532d9487d5fd2e2d`. [Recorded CI run 36072442061](https://github.com/thisisntjon/ce-stranger-replay-v1/actions/runs/36072442061) passed nine OS/Python jobs at that commit. This is hosted synthetic replay, not reproduction of private CE procedure studies. See the separate [research record](https://github.com/thisisntjon/consumption-demo) for dated results and limits.

## Run the released fixture

Requirements: Git and Python 3.11 or newer. No third-party Python packages or network access are required after cloning. Use a new clone directory and run these commands in order:

```powershell
git clone https://github.com/thisisntjon/ce-stranger-replay-v1.git
cd ce-stranger-replay-v1
git checkout 8374bb6ee93edef37f57f284532d9487d5fd2e2d
python examples/public_demo/run_public_demo.py --output .tmp/public-demo-run
python examples/public_demo/verify_receipt.py .tmp/public-demo-run/RECEIPT.json --output .tmp/public-demo-run/ORACLE-DECISION.json
```

On systems where Python is named `python3`, substitute it for `python`. The checkout selects the released fixture, not the latest branch. A detached-HEAD notice is expected. The newer documentation on `main` does not change this release pin.

Both Python commands should exit with code 0. The runner prints `"passed": true`. The receipt checker prints `"decision": "accepted_automated_oracle"`, with all six entries in `checks` set to `true`.

**To run again, choose a new output directory**, such as `.tmp/public-demo-run-2`, and use that same path in the verification command. The runner refuses an existing output directory so an earlier result is not overwritten.

## Inspect the result

Open the files under `.tmp/public-demo-run/`:

| File | What to inspect |
| --- | --- |
| `REPORT.md` | The evidence, correction, successor and restore narrative. |
| `RESULT.json` | Executed lifecycle checks, restore status and limitations. |
| `RECEIPT.json` | Input hashes, environment details and the declared oracle projection. |
| `ORACLE-DECISION.json` | The six receipt checks and the exact receipt/oracle hashes. |
| `restored/restore-check.json` | Preserved-file checks and the same-host Python guard checks. |
| `completed-work.zip` | The archive used for the guarded replay. |

[`FIXTURE-MANIFEST.json`](examples/public_demo/FIXTURE-MANIFEST.json) pins committed fixture bytes. [`ORACLES.json`](examples/public_demo/ORACLES.json) defines the expected receipt projection. The receipt checker compares those declared values and input pins; it does not independently rerun or establish the meaning of every reported behavior.

### Executed behavior and declared labels

[`stateful_demo.py`](examples/stateful_demo.py) executes the initial task, applies a correction, assesses the earlier work as stale, refuses the old snapshot, checks the successor and replays the archived state. Its assertions are recorded in `RESULT.json`. Recovery runs in a fresh Python process on the same host, with Python guards against specified original/cache reads and network access. This is not operating-system isolation or clean-machine qualification.

**The `UNKNOWN / INSUFFICIENT_EVIDENCE` label is a constructed fixture label in this entry point.** [`run_public_demo.py`](examples/public_demo/run_public_demo.py) reads the frozen unsupported-case rubric, appends a report label and writes the expected oracle projection. The stateful lifecycle does not issue a separate unsupported-question lookup. An accepted receipt therefore does not establish an executed abstention test. Review the underlying lifecycle records separately from the receipt's declared labels.

A non-author reviewer can follow [NON_AUTHOR_REVIEW.md](NON_AUTHOR_REVIEW.md) to run the package twice from fresh output directories and bind a review to exact receipts and hashes. The scope remains this published synthetic workflow.

## Optional comparison

```text
python examples/public_demo/compare_baseline.py --output .tmp/public-comparison
```

This writes `COMPARISON.md` and `COMPARISON.json`, with a nested fixture run. The comparator deliberately reads the first matching text and keeps reusing it after a correction. It illustrates the effects of those chosen rules; it does not measure superiority over a well-maintained retrieval system, model quality, customer value, speed or cost. Its unsupported-case label has the same construction limit described above. Use a new output directory for every comparison run.

## Reproduction and reporting

The public verification workflow covers Ubuntu, Windows and macOS with Python
3.11, 3.12 and 3.13. Its artifacts contain machine-readable replay receipts
and oracle decisions. A passing workflow establishes hosted replay of this
fixture; it does not establish product efficacy or human acceptance.

See [REPRODUCIBILITY.md](REPRODUCIBILITY.md), [SECURITY.md](SECURITY.md) and
[CITATION.cff](CITATION.cff) for the release boundary, reporting route and
citation metadata.

## Usage terms

The original code and documentation in this public fixture are available under the [MIT License](https://github.com/thisisntjon/ce-stranger-replay-v1/blob/main/LICENSE), copyright 2026 Jonathan Simone. Preserve the copyright and permission notice when sharing copies or substantial portions. [NOTICE.md](NOTICE.md) describes the publication boundary; the license does not grant access to the private product runtime or private corpora.

The pinned fixture commit predates the license file. The link above points to the current license on `main`; the replay commands continue to select the same released fixture code.

## Boundaries

This package does not establish automatic claim extraction, scientific truth, general retrieval quality, customer value, production readiness, or clean-machine recovery. The private product runtime remains separate. Any later qualification must name its package commit, commands, hashes, environment boundary, and limitations.
