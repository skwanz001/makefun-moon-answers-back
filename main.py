"""The Moon Finally Answers Back.

Writes the Moon's one-line comeback to /output/entry.txt.
Standard library only.
"""

from pathlib import Path

LINE = "Four billion years of wishes, howls, and 2 a.m. promises. Not one of you ever wished me a good night back."


def main() -> None:
    # The gate requires 1-240 characters of non-whitespace UTF-8 text.
    assert 1 <= len(LINE.strip()) <= 240, f"line is {len(LINE)} chars"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
