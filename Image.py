import cv2


class Image:
    def __init__(self, path, name="image"):
        self.__path = path
        self.__openCVData = cv2.imread(self.path, cv2.IMREAD_UNCHANGED)
        self.__size = self.openCVData.shape[0], self.openCVData.shape[1]
        self.__name = name

    def __str__(self):
        return f"Image: {self.path}, {self.openCVData}"
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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def show(self):
        cv2.imshow(self.name, self.openCVData)

    def close(self):
        cv2.destroyAllWindows()

    def save(self, path):
        cv2.imwrite(path, self.openCVData)