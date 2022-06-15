"""Manage Pylint output on worflow."""
import sys

from utils.github_actions.color import score_to_hex_color


if __name__ == '__main__':
    # SCORE_MIN can be changed safely depending on your needs.
    SCORE_MIN = 7.0
    SCORE_MAX = 10.0
    arg = sys.argv[1]
    score = float(arg.split('=')[1])

    if score < SCORE_MIN:
        raise ValueError(f'Pylint score {score} is lower than'
                         f'minimum ({SCORE_MIN})')

    print(score_to_hex_color(score, SCORE_MIN, SCORE_MAX))
