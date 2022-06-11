
""" Manage Pytest-cov output on worflow. """

import sys

from utils.github_actions.color import score_to_hex_color


if __name__ == '__main__':
    # SCORE_MIN can be changed safely depending on your needs.
    # NOTE: score on %
    SCORE_MIN = 0
    SCORE_MAX = 100

    arg = sys.argv[1]
    score_percent = arg.split('=')[1]
    score = float(score_percent.split('%')[0])

    if score < SCORE_MIN:
        raise ValueError(f'Pytest coverage {score}% is lower than'
                         f'minimum ({SCORE_MIN}%)')

    print(score_to_hex_color(score, SCORE_MIN, SCORE_MAX))
