import cv2
from Logo import Logo
from Image import Image


class BaseImage(Image):

    def __init__(self, path):
        super().__init__(path)
        self.__logoPositions = (0, 0)

    @property
    def logoPositions(self):
        return self.__logoPositions

    @logoPositions.setter
    def logoPositions(self, value):
        self.__logoPositions = value

    def addWatermark(self, logo: Logo):
        x, y = self.logoPositions
        w, h = logo.size

        borders = self.openCVData[y:y + h, x:x + w]

        # Wasserzeichen anpassen, falls es über den Bildrand hinausragt
        if borders.shape[0] != h:
            y -= h - borders.shape[0]

        if borders.shape[1] != w:
            x -= w - borders.shape[1]

        roi = self.openCVData[y:y + h, x:x + w]

        # Wasserzeichen hinzufügen
        for c in range(0, 3):
            roi[:, :, c] = roi[:, :, c] * (1 - logo.transparency) + logo.openCVData[:, :, c] * logo.transparency

        self.openCVData[y:y + h, x:x + w] = roi
