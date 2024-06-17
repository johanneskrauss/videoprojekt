from tkinter import filedialog

import cv2


# Dateipfad auswählen
def selectFile() -> str:
    file = filedialog.askopenfilename()
    return file

def textToLogo():
    pass
