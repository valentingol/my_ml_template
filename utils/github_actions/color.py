
""" Color utils for GitHub actions. """

from colorsys import hsv_to_rgb


def score_to_hex_color(score, score_min, score_max):
    """ Convert score to hex color red > brightgreen. """
    norm_score = max(0, (score - score_min) / (score_max - score_min))
    hsv = (1/3 * norm_score, 1, 1)
    rgb = hsv_to_rgb(*hsv)
    rgb = tuple(int(255 * value) for value in rgb)
    hex_color = f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'
    return hex_color
