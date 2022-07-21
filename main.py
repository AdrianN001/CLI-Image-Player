from PIL import Image
import time
import numpy as np

image = Image.open("sample_image.png")


def resize_image(image) -> Image:
    image_size_ratio = image.size[1]/image.size[0]
    if int(image_size_ratio) == 1:
        return image.resize((int(90 * image_size_ratio), 58), Image.Resampling.LANCZOS)
    else:
        return image.resize((200, 58), Image.Resampling.LANCZOS)


image = resize_image(image)


def image_to_pixels(image) -> list[tuple]:
    if type(list(image.getdata())[0]) == int: # there are a couple of extensions which won't give back tuples as their pixels
        image = image.convert("RGB")
    pixels = list(image.getdata())
    width, height = image.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    return pixels


def convert_pixels_to_symbol(pixels: list[tuple]) -> list[list]:
    def helper(pixel: tuple[int]) -> str:
        symbols = "0@#&;*,."

        pixel_vilagossaga: int = sum(pixel)  # max 3*255 lehet (765)
        # min 3*0
        return symbols[pixel_vilagossaga % len(symbols)]


    new_list_of_symbols = []

    for row in pixels:
        new_list_of_symbols.append(list(map(lambda x: helper(x), row)))
    return new_list_of_symbols


pixels: list[tuple] = convert_pixels_to_symbol(image_to_pixels(image))


def print_symbols(list_of_symbols: list[tuple]):
    for row in list_of_symbols:
        print(''.join(row), end="\n")


print_symbols(pixels)
