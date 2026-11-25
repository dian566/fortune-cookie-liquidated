#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader - make.fun entry.

The program writes the entrant's single fortune cookie line to
/output/entry.txt: a fortune for a crypto trader who has just been
liquidated, at most 20 words of plain text. The line is a fixed
string, so every run writes byte-identical output.

The joke turns on the fortune's own promise: the portfolio does rise
again, just never the one the trader lost.
"""

import os

ENTRY = "Your portfolio will rise again, just not this one. The dip you bought bought you instead."


def main() -> None:
    """Write the one-line fortune to /output/entry.txt."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
