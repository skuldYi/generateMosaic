leng = 7

step = 1 / leng
# width = step * 3
# bgn = (g / 255) * (1 - step * 2) + step - width / 2
# pos = random() * width + bgn

# print('{}\t{}'.format(g, pos))

for i in range(leng):
    print(step * (i + 1))