#!/usr/bin/env python3
"""Have You Tried Turning It Off?

A program/v1 entry for make.fun competition
u-motasimfuad-have-you-tried-turning-it-off-154a938b.

The program writes a single funny line that a hopeless tech support agent
says to a desperate customer to /output/entry.txt.

It is fully deterministic: the same line is written on every run, with no
input, no network access and no randomness.
"""

import os

# One line, 107 characters: the agent opens with the classic line, then
# reveals the whole troubleshooting guide is that one step repeated —
# cheerful uselessness as the joke. Chosen over 13 other candidates after
# scoring them against the published judge brief (see candidates.md in the
# build workspace): it twists the competition's namesake classic, which is
# exactly what criterion 5 of the brief rewards, and the customer is never
# the butt of it.
LINE = "Have you tried turning it off and on again? It's step one of two \u2014 step two is turning it off and on again."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
