import io
import sys

import Utils
import cv2

from Image import Image
from Logo import Logo

if __name__ == "__main__":

    #Hintergrundbild
    print("Hauptbild")
    baseImgPath = Utils.selectFile()
    MainImage = Image(cv2.imread(baseImgPath))
    cv2.imshow("image", MainImage.baseImage)

    #Wasserzeichen
    print("Wasserzeichen: ")
    watermarkPath = Utils.selectFile()

    transparency = float(input("Transparenz: "))
    Watermark = Logo(transparency,  watermarkPath)

    factor = float(input("Faktor: "))
    Watermark.scaleSize(factor, MainImage.size)

    print("Position des Wasserzeichens: ")
    # Create a new stream to capture the output
    output = io.StringIO()

    # Redirect standard output to the new stream
    sys.stdout = output

    cv2.setMouseCallback("image", Image.getMousePosition)

    # Reset standard output to the console
    cv2.waitKey(0)
    sys.stdout = sys.__stdout__
    print(output.getvalue())
    logoPos = output.getvalue()
    logoPos = logoPos.strip("\n").split(" ")
    print(logoPos)
    MainImage.logoPositions = int(logoPos[0]), int(logoPos[1])


    WatermarkWithoutAlpha, mask = Watermark.splitRGBAChannels()
    mask = mask * Watermark.transparency

    MainImage.addWatermark(Watermark,mask)

    cv2.imshow("image", MainImage.baseImage)
    cv2.waitKey(0)

