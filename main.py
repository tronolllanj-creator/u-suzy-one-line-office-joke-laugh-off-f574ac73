#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes one original one-line office joke to /output/entry.txt.
Stdlib only: no network, no input files, no dependencies.
The joke is embedded below; the grader runs `python3 main.py`.
"""
import os

JOKE = "My expense report for three sad airport pretzels was rejected because I failed to itemize my dwindling will to live."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
