"""A two-sentence horror story.

Prints the story to stdout and writes the exact same text, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the story is a constant in this file,
and the checks enforce the competition's two-sentence, 400-character gate.
"""

import os
import sys

STORY = (
    "My phone autocorrected 'goodnight, love' to 'goodnight, love, "
    "don't turn around.' "
    "I laughed, until I realised I had never typed the word love."
)


def main() -> int:
    if not 1 <= len(STORY) <= 400:
        print(f"error: story is {len(STORY)} chars, must be 1-400",
              file=sys.stderr)
        return 1
    if STORY.count(".") != 2:
        print("error: story must be exactly two sentences",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)
    print(STORY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
