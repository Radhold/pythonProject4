from PIL import Image, ImageDraw


def board(n, s):
    new_image = Image.new("RGB", (n * s, n * s), (255, 255, 255))
    x = y = s * n
    draw = ImageDraw.Draw(new_image)
    for i in range(0, x, s):
        if i % (s * 2) == 0:
            for j in range(0, y, s):
                if j % (s * 2) == 0:
                    draw.rectangle([i, j, i + s - 1, j + s - 1], fill='black')

        else:
            for j in range(s, y, s):
                if j % (s * 2) != 0:
                    draw.rectangle([i, j, i + s - 1, j + s - 1], fill='black')
    new_image.save('res2.png', "PNG")


board(8, 50)
