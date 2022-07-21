from PIL import Image
import sys
import numpy as np


class CliPlayer:
    Image: Image
    Pixels: list[list]

    def __init__(self, file_location: str):
        self.Image = Image.open(file_location)

    def __resize_image(self) -> Image:
        image_size_ratio = self.Image.size[1] / self.Image.size[0]
        if int(image_size_ratio) == 1:
            self.Image = self.Image.resize((int(90 * image_size_ratio), 58), Image.Resampling.LANCZOS)
        else:
            self.Image = self.Image.resize((200, 58), Image.Resampling.LANCZOS)

    @staticmethod
    def __image_to_pixels(image: Image) -> list[list]:
        if type(list(image.getdata())[
                    0]) == int:  # there are a couple of extensions which won't give back tuples as their pixels
            image = image.convert("RGB")
        pixels = list(image.getdata())
        width, height = image.size
        pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
        return pixels

    @staticmethod
    def __convert_pixels_to_symbol(pixels: list[list]) -> list[list]:
        def helper(pixel: tuple[int]) -> str:
            symbols = "0@#&;*,."

            brightness: int = sum(pixel)  # max 3*255 = (765)
            # min 3*0

            for index, zone in enumerate(np.array_split(range(766), len(symbols))):
                if brightness in zone:
                    return symbols[index]

        new_list_of_symbols = []

        for row in pixels:
            new_list_of_symbols.append(list(map(lambda x: helper(x), row)))
        return new_list_of_symbols

    @staticmethod
    def __print_symbols(list_of_symbols: list[list]) -> None:
        for row in list_of_symbols:
            print(''.join(row), end="\n")

    def show(self):
        self.__resize_image()
        self.Pixels = self.__image_to_pixels(self.Image)

        Symbols = self.__convert_pixels_to_symbol(pixels=self.Pixels)

        self.__print_symbols(list_of_symbols=Symbols)


if __name__ == "__main__":
    Test = CliPlayer("Sample_2.png")
    Test.show()
