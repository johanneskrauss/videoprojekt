from tkinter import filedialog

import cv2
import numpy as np

# Dateipfad auswählen
def selectFile() -> str:
    file = filedialog.askopenfilename()
    return file

""""""
def text_to_logo():

    WHITE = (255, 255, 255,255)
    BLACK = (0, 0, 0,255)
    GREY = (128, 128, 128,255)

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_size = 1.1
    font_color = WHITE
    font_thickness = 2
    text = "HALLO"
    position = (0, 0)

    text_okay = False
    color_okay = False

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

    empty_img = np.zeros((200, 200, 4), np.uint8)
    text_img = cv2.putText(empty_img, text, position, font, font_size, font_color, font_thickness, cv2.LINE_AA)
    cv2.imwrite("text_logo.png",text_img)

def text_to_logo():
    # Define colors
    WHITE = (255, 255, 255, 255)  # White color with full opacity
    BLACK = (0, 0, 0, 255)  # Black color with full opacity
    GREY = (128, 128, 128, 255)  # Grey color with full opacity

    # Define font properties
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_size = 1.1
    font_thickness = 2
    text = "HALLO"
    position = (50, 50)  # Adjust position as needed

    # Get user input for text and color
    text = input("Geben Sie den gewünschten Text ein:")
    font_color_input = input("Welche Farbe soll der Text haben? (s=schwarz, w=weiß, g=grau)")

    # Set font color based on user input
    if font_color_input.upper() == "S":
        font_color = BLACK
    elif font_color_input.upper() == "W":
        font_color = WHITE
    elif font_color_input.upper() == "G":
        font_color = GREY
    else:
        print("Ungültige Eingabe!")

    # Create an empty image with a transparent alpha channel
    empty_img = np.zeros((200, 200, 4), np.uint8)

    # Add text to the image
    text_img = cv2.putText(empty_img, text, position, font, font_size, font_color, font_thickness, cv2.LINE_AA)

    # Save the image
    cv2.imwrite("text_logo.png", text_img)