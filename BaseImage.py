import cv2
import numpy as np

from Logo import Logo
from Image import Image


class BaseImage(Image):

    def __init__(self, path):
        super().__init__(path)
        self.__logoPosition = [0, 0]

    def __str__(self):
        return f"BaseImage: {self.path}, {self.size}, {self.logoPosition}, {self.openCVData.shape}"

    @property
    def logoPosition(self):
        return self.__logoPosition

    @logoPosition.setter
    def logoPosition(self, value):
        self.__logoPosition = value

    def alignLogo(self, logo: Logo):
        # Check if the number of channels in the base image and logo are the same
        if self.openCVData.shape[2] != logo.openCVData.shape[2]:
            # If the base image has 3 channels and the logo has 4 channels
            if self.openCVData.shape[2] == 3 and logo.openCVData.shape[2] == 4:
                # Convert the base image to 4 channels
                self.openCVData = cv2.cvtColor(self.openCVData, cv2.COLOR_BGR2BGRA)
            # If the base image has 4 channels and the logo has 3 channels
            elif self.openCVData.shape[2] == 4 and logo.openCVData.shape[2] == 3:
                # Convert the logo to 4 channels
                logo.openCVData = cv2.cvtColor(logo.openCVData, cv2.COLOR_BGR2BGRA)

    def addWatermark(self, logo: Logo):
        y, x = self.logoPosition
        h, w = logo.size

        borders = self.openCVData[y:y + h, x:x + w]  # Bereich, in dem das Logo liegen würde

        # Wasserzeichen in Bild zurückschieben, falls es über den Bildrand hinausragt
        if borders.shape[0] != h:
            y -= h - borders.shape[0]

        if borders.shape[1] != w:
            x -= w - borders.shape[1]

        roi = self.openCVData[y:y + h, x:x + w]  # Bereich, wo das Logo jetzt liegen soll
        # Wasserzeichen hinzufügen
        for c in range(0, logo.openCVData.shape[2]):
            roi[:, :, c] = roi[:, :, c] * (1 - logo.transparency) + logo.openCVData[:, :, c] * logo.transparency

        self.openCVData[y:y + h, x:x + w] = roi

    def setLogoPosition(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.logoPosition = [y,x]
            print("Position des Wasserzeichens: ", self.logoPosition)
            print("Drücke eine beliebige Taste, um fortzufahren!")
