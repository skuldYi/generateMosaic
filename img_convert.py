from PIL import Image


def paste_pos(bg, img):
    # bg, img: (w, h)
    pos = map(lambda x, y: int((x - y) / 2), bg, img)
    pos = list(pos)
    return (pos[0], pos[1])


def fit_pattern(size, pattern="pattern.jpg"):
    bg = Image.new("L", size, 128)
    with Image.open(pattern) as im:
        im = im.convert("L")
        im.thumbnail(bg.size)
        bg.paste(im, paste_pos(bg.size, im.size))
        return bg.load()

# fit_pattern((128, 256)).show()
