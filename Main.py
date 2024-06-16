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
        print("Bitte wähle einen Hintergrund aus: ")

        try:
            mainPath = Utils.selectFile()
            MainImage = BaseImage(mainPath)
        except FileNotFoundError:
            print("Datei konnte nicht gefunden werden!")
        except ValueError:
            print("Das Dateiformat ist falsch!")
        except AttributeError:
            print("Bitte eine Bilddatei auswählen! (.jpg, .png, .bmp, ...)")

    while watermarkPath == "":

        try:
            # Wasserzeichen
            print("Bitte wähle ein Wasserzeichen aus: ")
            watermarkPath = Utils.selectFile()

        except FileNotFoundError:
            print("Datei nicht gefunden!")
        except ValueError:
            print("Falsches Dateiformat!")
        except AttributeError:
            print("Bitte eine Bilddatei auswählen! (.jpg, .png, .bmp, ...)")

    while Watermark == None:
        try:
            transparency = float(input("Bitte den Grad der Transparenz angeben! (Zwischen 0 und 1, wobei 1 = 100% Deckkraft): "))

            if transparency < 0 or transparency > 1:
                raise ValueError("Transparency must be between 0 and 1")

            Watermark = Logo(transparency, watermarkPath)

        except ValueError:
            print("Bitte gibt eine Gleitkomma-Zahl zwischen 0 und 1 an!")
        except:
            print("Da ist etwas schiefgelaufen!")

    while factorFlag == 0:
        try:
            factor = float(input("Bitte einen Skalierungs-Faktor angeben! (Zwischen 0 und 1, wobei 1 = Maximal mögliche Größe): "))

            if factor < 0 or factor > 1:
                raise ValueError("Factor must be between 0 and 1")

            factorFlag = 1
            Watermark.scaleSize(factor, MainImage.size)

        except ValueError:
            print("Bitte gibt eine Gleitkomma-Zahl zwischen 0 und 1 an!")
        except:
            print("Da ist etwas schiefgelaufen!")

    while logoPos == "":

        try:
            print("Position des Wasserzeichens, durch 'Mausklick' bestätigen: ")
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
            MainImage.logoPositions = int(logoPos[0]), int(logoPos[1])

            Watermark.transparency = Watermark.getAlpha() * Watermark.transparency

            MainImage.addWatermark(Watermark)

            cv2.imshow("image", MainImage.openCVData)

            cv2.waitKey(0)
            OutputImageSatisfactory = ""

            while OutputImageSatisfactory != "J" and OutputImageSatisfactory != "N":

                OutputImageSatisfactory = input("Gefällt Ihnen die Position des Wasserzeichens? (J = Ja, N = Nein): ")

                try:
                    if OutputImageSatisfactory.upper() == "J":
                        OutputImagePath = input("Bitte geben Sie einen Namen für die zu speichernde Datei an: ") + ".png"

                        cv2.imwrite(OutputImagePath, MainImage.openCVData)

                    elif OutputImageSatisfactory.upper() == "N":
                        print("#DoItAgain")

                    else:
                        print("Falscher Buchstabe!")
                except:
                    print("Mehr Kaput!")

        except:
            print("Kaput!")