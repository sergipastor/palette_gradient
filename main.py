import argparse

from utils.image import create_image, store_image
from utils.colors import process_colors, ValidateColors
from utils.constants import (
    DEFAULT_COLORS, DEFAULT_DISTRIBUTION, DISTRIBUTION_CHOICES
            )


def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument(
        "--output_folder",
        type=str,
        required=True,
        help="Path to the output folder."
    )
    parser.add_argument(
        "--colors",
        nargs="*",
        action=ValidateColors,
        default=DEFAULT_COLORS,
    )
    parser.add_argument(
        "--distribution",
        choices=DISTRIBUTION_CHOICES,
        default=DEFAULT_DISTRIBUTION,
    )

    args = parser.parse_args()
    colors = process_colors(args.colors, args.distribution)
    img = create_image(colors)
    store_image(img, "uhaha.png")


if __name__ == "__main__":
    main()
