"""Monday Morning Punchlines entry writer.

Writes the single approved joke to /output/entry.txt.
"""

from pathlib import Path

ENTRY_TEXT = (
    "Monday morning arrived like an unscheduled update: "
    "nothing improved, everything needs a restart."
)

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry() -> None:
    """Create the output directory and write the entry exactly."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
