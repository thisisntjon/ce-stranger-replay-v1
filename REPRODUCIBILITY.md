# Reproducibility record

The public fixture is exercised by the `Public fixture verification` workflow on
the hosted Ubuntu, Windows and macOS runners with Python 3.11, 3.12 and 3.13.
Each matrix job runs the same offline fixture, verifies the committed oracle,
and uploads its receipt, result, report and oracle decision as a uniquely named
artifact. The workflow uses read-only repository permissions and pins its
third-party actions to immutable commits.

This establishes hosted cross-platform replay of the published synthetic
fixture. It does not establish semantic truth, human acceptance, product
runtime qualification, customer value or a clean-machine restore of private
archives.

For a fresh clone and the released commit, follow the [complete README quickstart](README.md#run-the-released-fixture). From that checkout, reproduce locally with:

```text
python examples/public_demo/run_public_demo.py --output .tmp/public-demo-run
python examples/public_demo/verify_receipt.py .tmp/public-demo-run/RECEIPT.json --output .tmp/public-demo-run/ORACLE-DECISION.json
```

The expected behavior and limitations are pinned in `ORACLES.json` and the
generated receipt records the exact input hashes and runtime information.

Both commands should exit with code 0. The runner prints `"passed": true`; the receipt checker returns `accepted_automated_oracle` with all six checks true. Use a new output directory for each run and verify the receipt from that same directory. The runner refuses existing output directories.

## Interpretation

The executed stateful lifecycle covers the initial task, correction, stale-work assessment, refusal of the old snapshot, checked successor and guarded archive replay. Inspect `RESULT.json`, the task records and `restored/restore-check.json` for those checks.

The wrapper constructs the receipt's oracle projection. In particular, its `UNKNOWN / INSUFFICIENT_EVIDENCE` label comes from the frozen unsupported-case rubric; this entry point does not execute an unsupported-question lookup. Receipt acceptance establishes agreement with declared pins and labels, not an independent execution of each projected behavior. The `offline_declared` receipt check also tests a declaration, not operating-system network isolation.

The restored process runs on the same host and interpreter with Python guards. A passing run is not clean-machine or private-runtime recovery qualification.

See [LICENSE](LICENSE) for the MIT terms, [NOTICE.md](NOTICE.md) for the publication boundary and the [README usage terms](README.md#usage-terms) for the distinction between the pinned fixture and current documentation.
