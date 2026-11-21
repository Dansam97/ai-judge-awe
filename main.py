"""Write one slow, quiet text to /output/entry.txt."""

from pathlib import Path

FRAGMENTS = (
    "All night the rain talked to the roof and asked for nothing.",
    "The stars have shone since before there were eyes, and they are in no hurry.",
    "The moon pulls the sea without touching it, and lets it go.",
    "Snow settles on a pine branch until it bends, and slips away.",
)

OUT_PATH = Path("/output/entry.txt")
LIMIT = 280


def weave(parts):
    """Join the fragments into a single unhurried piece."""
    return " ".join(part.strip() for part in parts)


def check_piece(text):
    """Count Unicode code points and refuse anything out of bounds."""
    size = len(text)
    assert 1 <= size <= LIMIT, f"entry is {size} code points, must be 1-{LIMIT}"
    assert text.strip(), "entry must not be only whitespace"
    return size


def main():
    piece = weave(FRAGMENTS)
    size = check_piece(piece)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(piece, encoding="utf-8")
    print(f"wrote {size} characters to {OUT_PATH}")
    print(piece)


if __name__ == "__main__":
    main()
