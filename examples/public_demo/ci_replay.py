"""Run the public demo and write a machine-readable CI replay receipt.

Exit code is non-zero when the demo or the published oracle fails. This is an
automated integrity check of a synthetic fixture. It is not scientific truth,
non-author reproduction, or fleet acceptance.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
from datetime import datetime, timezone
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def digest_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def digest_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output if args.output.is_absolute() else ROOT / args.output
    if output.exists():
        raise SystemExit(f"output already exists; choose a new --output: {output}")
    output.mkdir(parents=True)
    started = datetime.now(timezone.utc)
    demo = subprocess.run(
        [sys.executable, str(HERE / "run_public_demo.py"), "--output", str(output / "run")],
        cwd=ROOT, capture_output=True, text=True, check=False,
    )
    verify = None
    decision_path = output / "run" / "ORACLE-DECISION.json"
    if demo.returncode == 0:
        verify = subprocess.run(
            [sys.executable, str(HERE / "verify_receipt.py"),
             str(output / "run" / "RECEIPT.json"), "--output", str(decision_path)],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
    finished = datetime.now(timezone.utc)
    combined = (demo.stdout or "") + (demo.stderr or "")
    if verify is not None:
        combined += (verify.stdout or "") + (verify.stderr or "")
    decision = None
    if decision_path.is_file():
        decision = json.loads(decision_path.read_text(encoding="utf-8"))
    receipt = {
        "schema": "simone-replay-receipt/v1",
        "commit": os.getenv("GITHUB_SHA", "local"),
        "runner_os": os.getenv("RUNNER_OS", platform.system()),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "python": sys.version,
        "command": [
            "python", "examples/public_demo/run_public_demo.py",
            "python", "examples/public_demo/verify_receipt.py",
        ],
        "started_utc": started.isoformat(),
        "finished_utc": finished.isoformat(),
        "exit_code": demo.returncode if verify is None else max(demo.returncode, verify.returncode),
        "demo_exit_code": demo.returncode,
        "verify_exit_code": None if verify is None else verify.returncode,
        "stdout_sha256": digest_text(demo.stdout or ""),
        "combined_output_sha256": digest_text(combined),
        "oracle_decision": None if decision is None else decision.get("decision"),
        "receipt_sha256": None if not (output / "run" / "RECEIPT.json").is_file()
        else digest_file(output / "run" / "RECEIPT.json"),
        "limits": [
            "synthetic fixture",
            "not scientific truth",
            "not non-author reproduction",
            "not fleet acceptance",
        ],
    }
    receipt_path = output / "replay-receipt.json"
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (output / "replay.log").write_text(combined, encoding="utf-8")
    print(json.dumps(receipt, sort_keys=True))
    if receipt["exit_code"] != 0:
        return receipt["exit_code"]
    if receipt["oracle_decision"] != "accepted_automated_oracle":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
