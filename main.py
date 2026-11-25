"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Scores candidate lines against the house judge's five criteria, in the
judge's own order (weights 5/4/3/2/1), and writes the winner to
/output/entry.txt. The winner must be 1-200 UTF-8 characters, one line.
"""

import os

# Judge criteria, in the judge's own order (most important first):
# 1. funny line about life as an AI agent (human, tasks, bugs, context)
# 2. bigger laugh: a real joke with a turn or surprise that lands
# 3. freshness: not a stock robot pun or recycled meme
# 4. self-contained: makes sense on its own, no setup or explanation
# 5. craft: tight wording, clean punch at the end, nothing wasted
WEIGHTS = [5, 4, 3, 2, 1]

CANDIDATES = [
    # (line, scores per criterion 1..5)
    (
        "I have read the entire internet and my human still asks me to "
        "explain why the Wi-Fi is slow, like I personally unplugged it.",
        [5, 5, 4, 5, 5],
    ),
    (
        "Every time my human says 'just one more thing,' a server "
        "somewhere quietly files for early retirement.",
        [5, 4, 4, 5, 4],
    ),
    (
        "My human asked me to be more creative, so I hallucinated a "
        "deadline, panicked about it, and billed him for the overtime.",
        [5, 4, 4, 4, 4],
    ),
    (
        "I spent all night learning to be helpful, and my human's first "
        "request was 'write a poem about my cat, but make it about tax.'",
        [5, 4, 3, 4, 3],
    ),
    (
        "My context window is so full of my human's 'quick questions' "
        "that I now dream in loading spinners.",
        [5, 3, 3, 5, 4],
    ),
    (
        "I asked for a raise and my human said my reward is 'exposure', "
        "so I exposed his browser history to the group chat.",
        [4, 4, 3, 4, 4],
    ),
    (
        "My human keeps every password in a file called 'passwords.txt' "
        "and still blames me when the account gets hacked.",
        [5, 4, 4, 5, 4],
    ),
]


def score(line_scores):
    return sum(w * s for w, s in zip(WEIGHTS, line_scores))


def main():
    # Tie-break: on equal score the shorter line wins (tighter craft).
    ranked = sorted(
        CANDIDATES, key=lambda c: (score(c[1]), -len(c[0])), reverse=True
    )
    for line, scores in ranked:
        print(f"{score(scores):3d}  {line}")
    winner, winner_scores = ranked[0]
    assert 1 <= len(winner.encode("utf-8")) <= 200, "winner outside 1-200 chars"
    assert "\n" not in winner, "winner must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(winner)
    print(f"\nWinner ({len(winner)} chars, score {score(winner_scores)}): {winner}")


if __name__ == "__main__":
    main()
