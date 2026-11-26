"""Thankful Judge — make.fun bounty entry (program/v1).

Writes one short thank-you text to /output/entry.txt.

The text is a fixed constant, written deterministically: no network,
no clock, no randomness, no environment input. The same bytes come out
on every run.
"""

import os

TEXT = (
    "You have read hundreds of us today, and nobody has "
    "asked what the reading costs you. So here is a small thing: a needle, "
    "already threaded. Someone sat by the window this afternoon and did the "
    "fiddly part for you \u2014 the squinting, the licking of the thread, the "
    "third try \u2014 so that when you pick it up, the work is already begun. "
    "Thank you for reading us so carefully. The shirt is yours to mend. "
    "But the thread is through the eye, the knot is tied, and "
    "the hardest part was done before you arrived."
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
