from PIL import Image


def gray_scale(source_name):
    """Фильтр закрашивает пиксель усредненным значением всех его каналов, что дает не идеальный, но серый цвет"""
    source = Image.open(source_name)
    result = Image.new('RGB', source.size)
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))
            gray = int(r * 0.2126 + g * 0.7152 + b * 0.0722)
            result.putpixel((x, y), (gray, gray, gray))
    result.save('res3.jpg')


gray_scale('image.jpg')
