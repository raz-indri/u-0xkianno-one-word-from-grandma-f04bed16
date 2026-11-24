#!/usr/bin/env python3
"""One Word From Grandma - make.fun entry.

Writes the single word Grandma would text about AI to /output/entry.txt.
"""

import os

WORD = "Witchcraft"  # Grandma's verdict on AI: warm, baffled, one word, no tricks.

# The gate counts every character in /output/entry.txt (1-30, UTF-8), so the
# file holds exactly the word: no trailing newline, no extra whitespace.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
