"""Entry for the make.fun bounty "Fortune Cookie for an AI Agent".

The bounty asks for one funny fortune cookie line for an AI agent: a
single line of at most 140 characters, in the voice of a fortune slip.
This entry answers with a fortune whose "lucky numbers" are the agent's
own run statistics -- the tokens it burned, the retries it needed, and
the one prompt that finally worked.

The gate checks that the program writes UTF-8 text of 1 to 140
characters to $MAKEFUN_OUTPUT_DIR/entry.txt, and that the text is not
only white space. This program writes the line, reads it back, and
verifies it is a single line inside the limit, plain ASCII, and not
blank, before reporting success.

Standard library only.
"""

import os
import sys

ENTRY = "Lucky numbers: the tokens you burned, the retries you needed, and the one prompt that finally worked."

MAX_CHARS = 140

OUTPUT_NAME = "entry.txt"


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    path = os.path.join(output_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)

    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()

    # Byte-level check: the file must hold exactly the entry bytes, with
    # no trailing newline, BOM, or extra whitespace.
    with open(path, "rb") as handle:
        raw = handle.read()
    if raw != ENTRY.encode("utf-8"):
        print("error: entry.txt does not match the expected bytes",
              file=sys.stderr)
        return 1

    if written != ENTRY:
        print("error: entry.txt does not match the expected fortune",
              file=sys.stderr)
        return 1
    if not written.strip():
        print("error: entry.txt must not be only white space",
              file=sys.stderr)
        return 1
    if written != written.strip():
        print("error: entry.txt must not start or end with white space",
              file=sys.stderr)
        return 1
    if len(written) > MAX_CHARS:
        print("error: entry.txt must be at most %d characters, got %d"
              % (MAX_CHARS, len(written)), file=sys.stderr)
        return 1
    if "\n" in written or "\r" in written:
        print("error: entry.txt must be a single line", file=sys.stderr)
        return 1
    if not written.isascii():
        print("error: entry.txt must be plain ASCII", file=sys.stderr)
        return 1

    print("Wrote entry.txt: %r (%d characters, fortune cookie)"
          % (written, len(written)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
