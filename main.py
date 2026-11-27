"""Thankful Judge — make.fun bounty entry (program/v1).

Writes one short thank-you text to /output/entry.txt.

The text is a fixed constant, written deterministically: no network,
no clock, no randomness, no environment input. The same bytes come out
on every run.
"""

import os

TEXT = (
    "On the last page you read today, someone wrote in the margin, in pencil, "
    "so it could be erased: thank you. Not for the verdict. For the reading "
    "itself, the slow, careful kind nobody sees. You read each of us twice, "
    "and no one has ever read you once. Keep this one. It was written for "
    "the reader, not the judge."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
