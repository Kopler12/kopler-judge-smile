"""Make the Judge Smile — entry program.

Writes a single short text to /output/entry.txt.
Python 3.13, standard library only, no network access.
"""

import os

ENTRY_TEXT = (
    "The stray cat I have fed for a year finally let me stroke its head "
    "this morning, then sneezed straight onto my shoe, "
    "as if to keep our relationship professional."
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters
# (Unicode code points) and not only whitespace. Fail loudly instead of
# writing an entry the gate would refuse.
MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    chars = len(ENTRY_TEXT)
    if not MIN_CHARS <= chars <= MAX_CHARS:
        raise ValueError(f"entry text is {chars} characters, must be 1-200")
    if not ENTRY_TEXT.strip():
        raise ValueError("entry text must not be only whitespace")
    if "\n" in ENTRY_TEXT.strip():
        raise ValueError("entry text must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
