"""Entry for make.fun: The Best Advice I Ever Got.

Writes one sentence of hard-earned advice to entry.txt.

A single sentence, the way the advice was originally given.
"""
import os

LINE = "My grandfather said: never lend money you need back, never argue hungry, and always leave a party while you are still having fun."
MAX_CHARS = 200


def main():
    assert LINE.strip(), "entry must not be empty"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds max chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
