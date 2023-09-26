
def extend_to_4_colors(colors: list) -> list:
    num_colors = len(colors)
    if num_colors == 2:
        colors = [colors[0], colors[0], colors[1], colors[1]]
    elif num_colors == 3:
        colors = [colors[0], colors[0], colors[1], colors[2]]

    if len(colors) != 4:
        raise Exception()

    return colors


def process_colors(colors: list, distribution: str) -> list:
    colors = extend_to_4_colors(colors)

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

    return [colors [i] for i in index]
