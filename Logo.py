import cv2
from Image import Image
import numpy as np


class Logo(Image):
    def __init__(self, transparency, path):
        super().__init__(path)
        self.__transparency = transparency

    # Setter und getter
    @property
    def transparency(self):
        return self.__transparency

    @transparency.setter
    def transparency(self, value):
        self.__transparency = value

    # Logogröße in Relation zum Bild
    def scaleSize(self, factor: float, imageSize: tuple) -> None:
        if factor <= 0 or factor > 1:
            raise ValueError("Factor must be  between 0 and 1")
        # Bildverhältnis beibehalten
        ratio = float(self.openCVData.shape[1]) / float(self.openCVData.shape[0])
        if ratio > 1:  # Breiter als hoch
            new_width = int(imageSize[1] * factor)
            new_height = int(new_width / ratio)

        else: # Höher als breit/quadratisch
            new_height = int(imageSize[0] * factor)
            new_width = int(new_height * ratio)
        self.size = new_width, new_height
        self.openCVData = cv2.resize(self.openCVData, self.size, interpolation=cv2.INTER_AREA)

    # Alpha Kanal von Bild ausgeben oder erstellen
    def getAlpha(self) -> np.ndarray:
        if self.openCVData.shape[2] == 4:  # Alpha Channel vorhanden
            b, g, r, a = cv2.split(self.openCVData)
            return a / 255.0
        else:
            return np.ones(self.openCVData.shape[:2], dtype="float32")  # Kein Alpha Channel vorhanden -> Array aus 1en

    # RGB Anteil von Bild ausgeben
    def getRGB(self) -> np.ndarray:
        if self.openCVData.shape[2] == 4:
            b, g, r, a = cv2.split(self.openCVData)
            return cv2.merge((b, g, r))
        else:
            return self.openCVData

