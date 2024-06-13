import cv2
import numpy as np
import os


class Logo:
    def __init__(self, transparency, image_path):
        self.__transparency = transparency
        self.__image_path = image_path
        self.__logoImage = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        self.__size = self.logoImage.shape[0], self.__logoImage.shape[1]

    # Setter und getter
    @property
    def transparency(self):
        return self.__transparency

    @transparency.setter
    def transparency(self, value):
        self.__transparency = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def image_path(self):
        return self.__image_path

    @image_path.setter
    def image_path(self, value):
        self.__image_path = value

    @property
    def logoImage(self):
        return self.__logoImage

    @logoImage.setter
    def logoImage(self, value):
        self.__logoImage = value

    # Logogröße in Relation zum Bild
    def scaleSize(self, factor: float, imageSize: tuple) -> None:
        if factor <= 0 or factor > 1:
            raise ValueError("Factor must be  between 0 and 1")
        self.size = int(imageSize[0] * factor), int(imageSize[1] * factor)
        self.logoImage = cv2.resize(self.logoImage, self.size, interpolation=cv2.INTER_AREA)

    # Bild in RGBA zerlegen
    def splitRGBAChannels(self) -> tuple:
        image = self.logoImage
        if image.shape[2] == 4:  # Bild hat bereits Alpha-Kanal
            b, g, r, a = cv2.split(image)
            return cv2.merge((b, g, r)), a / 255.0
        else:  # Bild hat keinen Alpha-Kanal
            b, g, r, a = cv2.split(image)
            return image, (b + g + r) / 255.0
