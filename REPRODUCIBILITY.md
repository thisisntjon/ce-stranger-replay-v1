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

To reproduce locally:

```text
python examples/public_demo/run_public_demo.py --output .tmp/public-demo-run
python examples/public_demo/verify_receipt.py .tmp/public-demo-run/RECEIPT.json --output .tmp/public-demo-run/ORACLE-DECISION.json
```

The expected behavior and limitations are pinned in `ORACLES.json` and the
generated receipt records the exact input hashes and runtime information.

The repository does not currently grant a software license. Review and reuse
permissions should be obtained from the author before redistributing the
fixture or incorporating it into another project.
