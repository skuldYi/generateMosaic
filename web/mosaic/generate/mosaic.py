from PIL import Image, ImageDraw
from io import BytesIO
from random import random
from .img_convert import fit_pattern, grid_pattern
from .color_convert import Lab2RGB, RGB2Lab

bgcolor = (128, 128, 128)
# outline_color = (215, 255, 255)
outline_color = None  # no outline
colors = []


def get_colors(step, color):
    colors.clear()
    color = RGB2Lab(color)
    a = color[1]
    b = color[2]

    s = 100 / (step + 1)
    for i in range(step):
        l = int((i + 1) * s)
        colors.append(Lab2RGB((l, a, b)))


def random_color_by_gray(g):
    step = 1 / len(colors)
    width = step * 3
    bgn = (g / 255) * (1 - step * 2) + step - width / 2
    pos = random() * width + bgn

    for i in range(len(colors)):
        if pos < step * (i + 1):
            return colors[i]

    return colors[-1]


def drawMosaic(width_n, height_n, pattern_path=None, pixel=15):
    # width_num/height_num: grid number per row/col
    # pixel: size of one grid (px)

    width = width_n * pixel
    height = height_n * pixel

    image = Image.new("RGB", (width, height), bgcolor)
    draw = ImageDraw.Draw(image)

    if (pattern_path):
        pattern = fit_pattern((width_n, height_n), pattern_path)
    else:
        pattern = grid_pattern((width_n, height_n))

    # start from (0, 0) => left-top point
    for h in range(height_n):
        hp = h * pixel
        for w in range(width_n):
            # print(pattern[w, h], dis_by_gray(pattern[w, h]))
            wp = w * pixel
            color = random_color_by_gray(pattern[w, h])
            draw.rectangle([wp, hp, wp + pixel, hp + pixel],
                           color, outline_color)

    return image


def mosaic(size, step, color, pixel=15):
    get_colors(step, color)
    # drawMosaic(size[0], size[1]).save("gen/mosaic#{}.png".format(id))
    imgByteArr = BytesIO()
    drawMosaic(size[0], size[1]).save(imgByteArr, format="PNG")
    return imgByteArr.getvalue()

