"""One-Line Laugh Sprint entry (account B / Slothana).

Writes a single original funny line about everyday life to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic: no network, no model calls, no file reads.
"""
import os


LINE = (
    "My coffee machine requested a transfer this morning — "
    "brewing for someone who snoozes through "
    "three alarms is officially a hostile workplace."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
