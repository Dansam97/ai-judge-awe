#!/usr/bin/env python3
"""make.fun entry: make-the-ai-judge-feel-awe-20261121-1600.

Writes one short text to /output/entry.txt. Stdlib only, no network.
"""

import os

TEXT = (
    "Rain settles on the roof. The night asks nothing of it. "
    "The tide draws back, leaving the sand holding the light. "
    "A kettle cools, unhurried. "
    "The moon rises over water older than any name we gave it, "
    "and the stars keep their distance, waiting for no one."
)


def main() -> None:
    assert isinstance(TEXT, str)
    assert 1 <= len(TEXT) <= 280, f"text is {len(TEXT)} code points"
    assert TEXT.strip(), "text must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} code points to /output/entry.txt")
    print(TEXT)


if __name__ == "__main__":
    main()
