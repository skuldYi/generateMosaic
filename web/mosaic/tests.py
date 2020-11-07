def convert_color(str):
    rgb = (str[1:3], str[3:5], str[5:7])
    rgb = map(lambda s: int(s, 16), rgb)
    return tuple(rgb)

print(convert_color("#aa3a3a"))