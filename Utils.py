import os
from dataclasses import dataclass
from tkinter import filedialog

import cv2
import numpy as np


# Dateipfad auswählen
def selectFile() -> str:
    file = filedialog.askopenfilename()
    return file


@dataclass
class TextImage:
    # Define colors
    WHITE = (255, 255, 255, 255)  # White color with full opacity
    BLACK = (0, 0, 0, 255)  # Black color with full opacity
    GREY = (128, 128, 128, 255)  # Grey color with full opacity

    # Define font properties
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_size = 1.1
    font_thickness = 2
    font_color = BLACK
    text = "Orem Lipsum"
    position = (50, 50)  # Adjust position as needed

    __filename= "text_logo.png"

    def selectFontColor(self, font_color_input: str):
        # Set font color based on user input
        if font_color_input.upper() == "S":
            self.font_color = self.BLACK
        elif font_color_input.upper() == "W":
            self.font_color = self.WHITE
        elif font_color_input.upper() == "G":
            self.font_color = self.GREY
        else:
            print("Ungültige Eingabe!")

    def selectText(self, text: str):
        self.text = text

    def deleteFile(self):
        os.remove(self.__filename)

    def createTextImage(self):
        # Create an empty image with a transparent alpha channel
        empty_img = np.zeros((200, 200, 4), np.uint8)

        # Add text to the image
        text_img = cv2.putText(empty_img, self.text, self.position, self.font, self.font_size, self.font_color, self.font_thickness, cv2.LINE_AA)

        # Save the image
        cv2.imwrite(self.__filename, text_img)


