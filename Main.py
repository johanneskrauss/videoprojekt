import io
import sys

import Utils
import cv2

from BaseImage import BaseImage
from Logo import Logo

# Dateipfade
mainPath = ""
watermarkPath = ""

if __name__ == "__main__":
    # Hintergrundbild
    print("Hauptbild")
    mainPath = Utils.selectFile()
    MainImage = BaseImage(mainPath)

    # Wasserzeichen
    print("Wasserzeichen: ")
    watermarkPath = Utils.selectFile()

    transparency = float(input("Transparenz: "))
    Watermark = Logo(transparency, watermarkPath)

    factor = float(input("Faktor: "))
    Watermark.scaleSize(factor, MainImage.size)

    print("Position des Wasserzeichens: ")
    cv2.imshow("image", MainImage.openCVData)

    # Create a new stream to capture the output
    output = io.StringIO()

    # Redirect standard output to the new stream
    sys.stdout = output

    cv2.setMouseCallback("image", Utils.getMousePosition)

    # Reset standard output to the console
    cv2.waitKey(0)
    sys.stdout = sys.__stdout__
    logoPos = output.getvalue()

    logoPos = logoPos.strip("\n").split(" ")
    print(logoPos)
   #MainImage.logoPositions = int(logoPos[0]), int(logoPos[1])
    MainImage.logoPositions = (0,0)

    #WatermarkWithoutAlpha, mask = Watermark.splitRGBAChannels()
    Watermark.transparency = Watermark.getAlpha() * Watermark.transparency

    MainImage.addWatermark(Watermark)

    cv2.imshow("image", MainImage.openCVData)
    cv2.waitKey(0)
