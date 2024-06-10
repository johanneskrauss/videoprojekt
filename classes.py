import cv2 as cv

class Image:
    def __init__ (self, name):
        self.name = name
        self.shape = None
        self.color = None
        self.size = None

    def __str__(self):
        print(self.name+"is a picture in format"+self.shape)


