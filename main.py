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


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
