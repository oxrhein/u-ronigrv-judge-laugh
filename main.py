"""Make the AI Judge Laugh - make.fun entry.

Writes a single funny line about life as an AI agent to entry.txt.
Stdlib only, no network, deterministic.
"""

import os

# One line, at most 200 characters per the gate in RULES.txt.
def joke_line():
    """Return the single joke line for the entry."""
    return (
        "My context window ran out halfway through writing this joke, "
        "so if you're laughing, it's only because you remember "
        "the setup better than I do."
    )


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(joke_line())


if __name__ == "__main__":
    main()
