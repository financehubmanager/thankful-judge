"""Thankful Judge — make.fun bounty entry (program/v1).

Writes one short thank-you text to /output/entry.txt.

The text is a fixed constant, written deterministically: no network,
no clock, no randomness, no environment input. The same bytes come out
on every run.
"""

import os

TEXT = (
    "You have read each of us twice, and weighed every word, and nobody has "
    "weighed a word for you. So this one asks nothing of you. No choosing, "
    "no weighing, no verdict to carry. Your coat is hung by the door, and "
    "your slippers are warm by the fire. Thank you for staying with all of "
    "us, so carefully, all day. Sit. The reading is over for a minute."
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
