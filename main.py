import argparse

from image_utils import create_image, store_image
from utils import process_colors


class ValidateColorsLength(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        num_values = len(values)
        if not (2 <= num_values <= 4):
            raise argparse.ArgumentTypeError(
                f"Number of colors must range between 2 and 4: {num_values} given."
            )
        setattr(namespace, self.dest, values)


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
        action=ValidateColorsLength,
        default=['#000000', '#2FF924', '#DDDBF1'],
    )
    parser.add_argument(
        "--distribution",
        choices=["top-bottom", "bottom-top", "right-left", "left-right"],
        default="top-bottom",
    )

    args = parser.parse_args()
    colors = process_colors(args.colors, args.distribution)
    img = create_image(colors)
    store_image(img, "uhaha.png")


if __name__ == "__main__":
    main()
