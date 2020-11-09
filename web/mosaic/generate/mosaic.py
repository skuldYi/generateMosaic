from PIL import Image, ImageDraw
from io import BytesIO
from random import random
from .img_convert import fit_pattern, grid_pattern
from .color_convert import Lab2RGB, RGB2Lab

colors = []


def get_colors(step, color):
    colors = []
    color = RGB2Lab(color)
    l = color[0]
    a = color[1]
    b = color[2]

    s = min(15, 100 / step)
    bgn = l - step / 2 * s
    ls = list(map(lambda x: round(x * s + bgn), range(step)))
    offset = 0
    if ls[0] < 8:
        offset = 8 - ls[0]
    elif ls[-1] > 100:
        offset = 98 - ls[-1]

    # print(offset, ls)
    for l in ls:
        colors.append(Lab2RGB((l + offset, a, b)))
    return colors


def random_color_by_gray(g, colors):
    step = 1 / len(colors)
    width = step * 3
    bgn = (g / 255) * (1 - step * 2) + step - width / 2
    pos = random() * width + bgn

    for i in range(len(colors)):
        if pos < step * (i + 1):
            return colors[i]

    return colors[-1]


def drawMosaic(size, colors, pattern, line):
    # size: width, height, pixel
    # width_num/height_num: grid number per row/col
    # pixel: size of one grid (px)
    width = size['width']
    height = size['height']
    pixel = size['pixel']

    image = Image.new("RGB", (width * pixel, height * pixel))
    draw = ImageDraw.Draw(image)

    if (pattern):
        pattern = fit_pattern((width, height), pattern)
    else:
        pattern = grid_pattern((width, height))

    # start from (0, 0) => left-top point
    for h in range(height):
        hp = h * pixel
        for w in range(width):
            wp = w * pixel
            color = random_color_by_gray(pattern[w, h], colors)
            draw.rectangle([wp, hp, wp + pixel, hp + pixel], color)

    if line['width'] > 0:
        lw = line['width']
        lc = line['color']
        for hp in range(0, (height + 1) * pixel, pixel):
            draw.line((0, hp, width * pixel, hp), width=lw, fill=lc)
        for wp in range(0, (width + 1) * pixel, pixel):
            draw.line((wp, 0, wp, height * pixel), width=lw, fill=lc)

    return image


def mosaic(size, step, color, image, line):
    colors = get_colors(step, color)
    pattern = None
    if image:
        pattern = Image.open(image)
    imgByteArr = BytesIO()
    drawMosaic(size, colors, pattern, line).save(imgByteArr, format="PNG")
    return imgByteArr.getvalue()
