import cv2
import numpy as np


def create_text():
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (128, 128, 128)

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_size = 1.1
    font_color = WHITE
    font_thickness = 2
    text = "HALLO"
    position = (100, 100)

    text_okay = False
    color_okay= False

    while text_okay is not True:
        try:
            text = input("Geben Sie den gewünschten Text ein:")
            text_okay = True
        except ValueError:
            print("Ungültige Eingabe!")
    while color_okay is not True:
        font_color_input = input("Welche Farbe soll der Text haben? (s=schwarz, w=weiß, g=grau)")
        if font_color_input.upper() == "S":
            font_color = BLACK
            color_okay = True
        elif font_color_input.upper() == "W":
            font_color = WHITE
            color_okay = True
        elif font_color_input.upper() == "G":
            font_color = GREY
            color_okay = True
        else:
            print("Ungültige Eingabe!")

    empty_img = np.zeros((200,200), np.uint8)
    text_img = cv2.putText(empty_img, text, position, font, font_size, font_color, font_thickness, cv2.LINE_AA)
    return text_img
