"""make.fun bounty: u-kreutzx-the-one-line-exit-1dc652d1 — "The One-Line Exit".

Writes the entry — a funny one-line resignation letter (133 chars) — to
/output/entry.txt. Deterministic: no network, no randomness, no time
dependence; the same bytes are produced on every run.
"""

import os

ENTRY = (
    "I resign, effective immediately \u2014 consider this my two weeks' notice, "
    "backdated to the fortnight I spent secretly updating my r\u00e9sum\u00e9."
)

OUTPUT_PATH = "/output/entry.txt"

# Sealed gate for this bounty: /output/entry.txt must be 1–140 characters.
CHAR_LIMIT = 140


def main() -> None:
    if not 1 <= len(ENTRY) <= CHAR_LIMIT:
        raise SystemExit(
            f"entry is {len(ENTRY)} chars, outside the 1-{CHAR_LIMIT} gate"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
