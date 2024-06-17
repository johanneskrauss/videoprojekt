from tkinter import filedialog

import cv2


# Dateipfad auswählen
def selectFile() -> str:
    file = filedialog.askopenfilename()
    return file


def getMousePosition(event, x, y, flags, params=None) -> None:
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        cv2.destroyAllWindows()

def textToLogo():
    pass
