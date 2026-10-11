#!/usr/bin/env python3

"""Basic file integrity checker placeholder."""

import hashlib
from pathlib import Path


def sha256sum(file_path):
    h = hashlib.sha256()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()


if __name__ == "__main__":
    target = Path("example.txt")
    if target.exists():
        print(sha256sum(target))
    else:
        print("Target file does not exist.")
