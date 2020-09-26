from PIL import Image, ImageDraw
from random import random
from img_convert import fit_pattern
import math

# need pillow

bgcolor = (128, 128, 128)
outline_color = (215, 255, 255)
# outline_color = None  # no outline

colors = [
    (186, 227, 255),
    (128, 172, 255),
    (68, 120, 207),
    (0, 84, 166),
    (0, 61, 138),
]


def average_dist():
    l = len(colors)
    arr = list(map(lambda x: x / l, range(l)))
    arr.reverse()
    return arr


def random_color(split):
    rdm = random()
    for i in range(len(split)):
        if rdm > split[i]:
            return colors[i]


def dis_by_gray(g):
    split = []
    # g: [0, 255]
    if g < 128:
        split.append(-0.4 * g + 255)
        split.append(-0.8 * g + 255)
        split.append(-1 * g + 229.5)
        split.append(-0.5 * g + 114.75)
    else:
        split.append(-0.5 * g + 267.75)
        split.append(-1 * g + 280.5)
        split.append(-0.8 * g + 204)
        split.append(-0.4 * g + 102)

    split.append(0)
    return list(map(lambda x: x / 255, split))


def drawMosaic(width_n, height_n, pattern_path="pattern.jpg", pixel=15):
    # width_num/height_num: grid number per row/col
    # pixel: size of one grid (px)

    width = width_n * pixel
    height = height_n * pixel

    image = Image.new("RGB", (width, height), bgcolor)
    draw = ImageDraw.Draw(image)
    pattern = fit_pattern((width_n, height_n), pattern_path)

    # start from (0, 0) => left-top point
    aver = average_dist()
    for h in range(height_n):
        hp = h * pixel
        for w in range(width_n):
            # print(pattern[w, h], dis_by_gray(pattern[w, h]))
            wp = w * pixel
            color = random_color(dis_by_gray(pattern[w, h]))
            draw.rectangle([wp, hp, wp + pixel, hp + pixel],
                           color, outline_color)

    return image


# show(): preview image
# drawMosaic(64, 32, "grad.jpg").show()
drawMosaic(64, 32).save("mosaic.png")
