import cv2
from Image import Image


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
        self.size = int(imageSize[0] * factor), int(imageSize[1] * factor)
        self.openCVData = cv2.resize(self.openCVData, self.size, interpolation=cv2.INTER_AREA)

    # Alpha Kanal von Bild ausgeben oder erstellen
    def getAlpha(self):
        if self.openCVData.shape[2] == 4:
            b, g, r, a = cv2.split(self.openCVData)
            return a / 255.0
        else:
            b, g, r = cv2.split(self.openCVData)
            return (b + g + r) / 255.0

    # RGB Anteil von Bild ausgeben
    def getRGB(self):
        if self.openCVData.shape[2] == 4:
            b, g, r, a = cv2.split(self.openCVData)
            return cv2.merge((b, g, r))
        else:
            return self.openCVData
