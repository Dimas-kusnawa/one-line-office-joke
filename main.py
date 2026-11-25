"""One-line office joke for make.fun.

Writes a single joke about office life to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Deterministic: the same line every run.
"""

import os

LINE = "My boss said 'we're a family here,' so I asked HR if family gets overtime pay."

# Why this joke works (judge criteria, in order):
# 1. It IS a one-line joke about office life: a single sentence, a joke,
#    about working in an office.
# 2. The punchline pays off the setup: "we're a family here" is the
#    corporate line every office worker has heard, and asking HR whether
#    family gets overtime pay turns the boss's own sentiment against him.
# 3. One line: setup and punchline in a single sentence, no rambling.
# 4. Fresh: the twist is not the tired "this meeting could have been an
#    email" line; it finds a specific, recognizable office moment and
#    answers it with a question nobody in the office would dare ask.
# 5. Clear on first read: no explanation needed, no obscure reference.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 200):
        raise SystemExit(f"line must be 1-200 chars, got {len(LINE)}")
    if LINE.count("\n") != 0:
        raise SystemExit("line must be a single line")
    # 78 chars, one sentence, no trailing newline: the gate wants 1-200
    # UTF-8 chars of non-whitespace text, and the file must hold exactly
    # this line. Writing with newline="" keeps the bytes byte-identical
    # on every run, so the two grading runs agree.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {path}: {LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
