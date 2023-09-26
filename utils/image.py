import numpy as np
from PIL import ImageColor
import matplotlib.pyplot as plt

ARRWIDTH = 1920
ARRHEIGHT = 1080


def create_channel_image(values, width, height):
    (upperleft, upperright, lowerleft, lowerright) = values

    array = np.linspace(
        np.linspace(upperleft, upperright, width),
        np.linspace(lowerleft, lowerright, width), 
        height,
        dtype=int
    )
    return array[:, :, None]


def create_image(hex_colors: list):
    rgb_colors = [
        ImageColor.getcolor(colour, "RGB")
        for colour in hex_colors
    ]
    colors_by_channel = zip(*rgb_colors)
    channel_images = list(map(lambda x: create_channel_image(x, ARRWIDTH, ARRHEIGHT), colors_by_channel))
    img = np.concatenate(channel_images, axis=2)
    return img


def store_image(img, filename: str) -> None:
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.axis('off')

    fig.patch.set_alpha(0)
    ax.patch.set_alpha(0)

    ax.imshow(img, aspect='auto', interpolation='none')
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.savefig(filename, bbox_inches='tight', pad_inches=0, transparent=True)
    plt.clf()
    plt.close()
