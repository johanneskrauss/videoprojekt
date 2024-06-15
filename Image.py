import cv2
import numpy as np
import Utils
from Logo import Logo


class Image:

    logoPos = (0,0)
    def __init__ (self,baseImage):
        self.__size = baseImage.shape[0],baseImage.shape[1]
        self.__baseImage = baseImage
        self.__logoPositions = (0,0)
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def baseImage(self):
        return self.__baseImage

    @baseImage.setter
    def baseImage(self, value):
        self.__baseImage = value

    @property
    def logoPositions(self):
        return self.__logoPositions

    @logoPositions.setter
    def logoPositions(self, value):
        self.__logoPositions = value

    def getMousePosition(event, x, y, flags, params = None) -> None:
        if event == cv2.EVENT_LBUTTONDOWN:
            print(x, y)

    def addWatermark(self, logo: Logo, mask) -> None:
        x,y = self.logoPositions
        w,h = logo.size
        roi = self.baseImage[y:y + h, x:x + w]

        # Wasserzeichen hinzufügen
        for c in range(0, 3):
            roi[:, :, c] = roi[:, :, c] * (1 - mask) + logo.logoImage[:, :, c] * mask

        self.baseImage[y:y + h, x:x + w] = roi




