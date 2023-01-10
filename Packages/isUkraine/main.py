from colorthief import ColorThief
from lib.colors import rgbToSimilarName


def main(image: str):
    print("is ua")
    color_thief = ColorThief(image)
    palette = color_thief.get_palette(color_count=6)
    for col in palette:
        print(rgbToSimilarName(col))