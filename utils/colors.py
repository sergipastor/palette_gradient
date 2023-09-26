import re
import argparse


def extend_to_4_colors(colors: list) -> list:
    num_colors = len(colors)
    if num_colors == 2:
        colors = [colors[0], colors[0], colors[1], colors[1]]
    elif num_colors == 3:
        colors = [colors[0], colors[0], colors[1], colors[2]]

    if len(colors) != 4:
        raise Exception()

    return colors


def order_index_from_distribution(distribution: str) -> list:
    if distribution == "top-bottom":
        index = [0, 1, 2, 3]
    elif distribution == "bottom-top":
        index = [2, 3, 0, 1]
    elif distribution == "right-left":
        index = [2, 0, 3, 1]
    elif distribution == "left-right":
        index = [0, 2, 1, 3]
    else:
        raise Exception()

    return index


def process_colors(colors: list, distribution: str) -> list:
    colors = extend_to_4_colors(colors)
    order_index = order_index_from_distribution(distribution)

    return [colors [i] for i in order_index]


def is_valid_hex_color(color: str) -> bool:
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color)
    return match is not None


class ValidateColors(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        num_values = len(values)
        if not (2 <= num_values <= 4):
            raise argparse.ArgumentTypeError(
                f"Number of colors must range between 2 and 4: {num_values} given."
            )
        if not all([is_valid_hex_color(v) for v in values]):
            raise argparse.ArgumentTypeError(
                "Every value in colors must be a valid hexadecimal value."
            )

        setattr(namespace, self.dest, values)