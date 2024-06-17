import cv2
from Image import Image
import numpy as np


class Logo(Image):
    def __init__(self, transparency, path):
        super().__init__(path)
        self.transparency = transparency

    # Setter und getter
    @property
    def transparency(self):
        return self.__transparency

    @transparency.setter
    def transparency(self, value=1.0):
        self.__transparency = self.getAlphaChannel() * value

    # Alpha Kanal von Bild ausgeben oder erstellen
    def getAlphaChannel(self) -> np.ndarray:
        if self.openCVData.shape[2] == 4:  # Alpha Channel vorhanden
            alpha = self.openCVData[:, :, 3]
            return alpha / 255.0
        else:
            return np.ones(self.openCVData.shape[:2], dtype="float32")  # Kein Alpha Channel vorhanden -> Array aus 1en

    # Logogröße in Relation zum Bild
    def scale(self, factor: float, imageSize: tuple) -> None:
        if factor <= 0 or factor > 1:
            raise ValueError("Factor must be  between 0 and 1")
        # Bildverhältnis beibehalten
        ratio = float(self.openCVData.shape[1]) / float(self.openCVData.shape[0])
        if ratio > 1:  # Breiter als hoch
            newWidth = int(imageSize[1] * factor)
            newHeight = int(newWidth / ratio)

        elif ratio == 1:  # Quadratisch
            newWidth = int(min(imageSize)*factor)
            newHeight = int(newWidth)

        else:  # Höher als breit
            newHeight = int(imageSize[0] * factor)
            newWidth = int(newHeight * ratio)

        self.size = newWidth, newHeight
        self.openCVData = cv2.resize(self.openCVData, self.size, interpolation=cv2.INTER_AREA)
        self.transparency = cv2.resize(self.transparency, self.size, interpolation=cv2.INTER_AREA) # resize transparency array to fit new image size


    # RGB Anteil von Bild ausgeben
    def getRGBChannel(self) -> np.ndarray:
        if self.openCVData.shape[2] == 4:
            b, g, r, a = cv2.split(self.openCVData)
            return cv2.merge((b, g, r))
        else:
            return self.openCVData


