import io
import sys

import Utils
import cv2

from BaseImage import BaseImage
from Logo import Logo

# Dateipfade
mainPath = ""
watermarkPath = ""
transparency = 0
factor = 0
logoPos = ""
Watermark = None
factorFlag = 0


if __name__ == "__main__":

    while mainPath == "":

        # Hintergrundbild
        print("Hauptbild: ")

        try:
            mainPath = Utils.selectFile()
            MainImage = BaseImage(mainPath)
        except FileNotFoundError:
            print("Datei konnte nicht gefunden werden!")
        except ValueError:
            print("Das Dateiformat ist falsch!")

    while watermarkPath == "":

        try:
            # Wasserzeichen
            print("Wasserzeichen: ")
            watermarkPath = Utils.selectFile()

        except FileNotFoundError:
            print("Datei nicht gefunden!")
        except ValueError:
            print("Falsches Dateiformat!")

    while Watermark == None:
        try:
            transparency = float(input("Transparenz: "))

            if transparency < 0 or transparency > 1:
                raise ValueError("Transparency must be between 0 and 1")

            Watermark = Logo(transparency, watermarkPath)
            Watermark.transparency = Watermark.getAlphaChannel() * Watermark.transparency

        except ValueError:
            print("Bitte gibt eine Gleitkomma-Zahl zwischen 0 und 1 an!")
        except Exception as e:
            print("Da ist was schiefgelaufen! ", e)

    while factorFlag == 0:
        try:
            factor = float(input("Faktor: "))

            if factor < 0 or factor > 1:
                raise ValueError("Factor must be between 0 and 1")

            factorFlag = 1
            Watermark.scale(factor, MainImage.size)

        except ValueError:
            print("Bitte gibt eine Gleitkomma-Zahl zwischen 0 und 1 an!")
        except Exception as e:
            print("Da ist was schiefgelaufen! ", e)

    while logoPos == "":

        try:
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
            MainImage.logoPosition = int(logoPos[0]), int(logoPos[1])


            MainImage.addWatermark(Watermark)

            cv2.imshow("image", MainImage.openCVData)
            cv2.waitKey(0)

        except Exception as e:
            print("Kaputt!: ", e)