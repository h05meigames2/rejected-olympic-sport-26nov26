"""Rejected Olympic Sports entry: writes one funny line to /output/entry.txt.

Stdlib only, deterministic, no network.
"""

import os

LINE = "Competitive queue-jumping: athletes sprint a 400-metre line, hurdle pensioners, and gold goes to whoever reaches the front unnoticed."


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    if "\n" in LINE or not LINE.strip():
        raise ValueError("line must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    # Self-check: what landed on disk must be exactly the one line.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt does not match LINE"


if __name__ == "__main__":
    main()
