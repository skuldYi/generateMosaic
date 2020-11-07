from PIL import Image, ImageDraw


def paste_pos(bg, img):
    # bg, img: (w, h)
    pos = map(lambda x, y: int((x - y) / 2), bg, img)
    pos = list(pos)
    return (pos[0], pos[1])


def fit_pattern(size, pattern):
    bg = Image.new("L", size, 128)
    with Image.open(pattern) as im:
        im = im.convert("L")
        im.thumbnail(bg.size)
        bg.paste(im, paste_pos(bg.size, im.size))
        return bg.load()


def grid_pattern(size):
    bg = Image.new("L", size, 128)
    draw = ImageDraw.Draw(bg)
    step = 255 / size[1]
    for i in range(size[1]):
        color = int(255 - i * step)
        draw.line((0, i, size[0], i), fill=color, width=1)

    # bg.save("pattern.jpg")
    return bg.load()

# grid_pattern((64, 64))