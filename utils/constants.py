WIDTH = 1920
HEIGHT = 1080
DEFAULT_COLORS = ['#000000', '#2FF924', '#DDDBF1']
DEFAULT_DISTRIBUTION = "top-bottom"
DISTRIBUTION_CHOICES = ["top-bottom", "bottom-top", "right-left", "left-right"]
DISTRIBUTION_HELP = """
    Distribution of the colors provided in the resulting image.
    top-bottom: first colors at the top, last colors at the bottom.
    bottom-top: first colors at the bottom, last colors at the top.
    right-left: first colors on the right side, last colors on the left side.
    left-right: first colors on the left side, last colors on the right side.
"""