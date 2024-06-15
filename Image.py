import cv2


class Image:
    def __init__(self, path):
        self.__path = path
        self.__openCVData = cv2.imread(self.path)
        self.__size = self.openCVData.shape[0], self.openCVData.shape[1]

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = value

    @property
    def openCVData(self):
        return self.__openCVData

    @openCVData.setter
    def openCVData(self, value):
        self.__openCVData = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
