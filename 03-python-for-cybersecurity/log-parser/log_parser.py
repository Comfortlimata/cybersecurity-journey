#!/usr/bin/env python3

"""Simple log parser placeholder."""

from pathlib import Path


def parse_log(file_path):
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with path.open("r", encoding="utf-8", errors="replace") as file:
        for line in file:
            print(line.strip())


if __name__ == "__main__":
    parse_log("example.log")
