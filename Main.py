import io
import sys

import Utils
import cv2

from BaseImage import BaseImage
from Logo import Logo

# Dateipfade
mainPath = ""
watermarkPath = ""

# Variablen
transparency = 0
factor = 0

# Objekte
Watermark = None
MainImage = None

# Flags
isLogoPos = 0
factorFlag = 0
outputImageSatisfactory = ""

if __name__ == "__main__":

    while mainPath == "":

        # Hintergrundbild
        print("Bitte wähle einen Hintergrund aus: ")

        try:
            mainPath = Utils.selectFile()
            MainImage = BaseImage(mainPath)
        except FileNotFoundError:
            print("Datei konnte nicht gefunden werden!")
            mainPath = ""
        except ValueError:
            print("Das Dateiformat ist falsch!")
            mainPath = ""
        except AttributeError:
            print("Bitte eine Bilddatei auswählen! (.jpg, .png, .bmp, ...) oder Pfad existiert nicht!")
            mainPath = ""

    while watermarkPath == "":

        try:
            # Wasserzeichen
            print("Bitte wähle ein Wasserzeichen aus: ")
            watermarkPath = Utils.selectFile()

        except FileNotFoundError:
            print("Datei nicht gefunden!")
            watermarkPath = ""
        except ValueError:
            print("Falsches Dateiformat!")
            watermarkPath = ""
        except AttributeError:
            print("Bitte eine Bilddatei auswählen! (.jpg, .png, .bmp, ...)")
            watermarkPath = ""

    while Watermark is None:
        try:
            transparency = float(input("Bitte den Grad der Transparenz angeben! (Zwischen 0 und 1, wobei 1 = 100% Deckkraft): "))

            if transparency < 0 or transparency > 1:
                raise ValueError("Transparency must be between 0 and 1")
            Watermark = Logo(transparency, watermarkPath)

        except ValueError:
            print("Bitte gibt eine Gleitkomma-Zahl zwischen 0 und 1 an!")
        except Exception as e:
            print("Da ist etwas schiefgelaufen!", e)

    while factorFlag == 0:
        try:
            factor = float(input("Bitte einen Skalierungs-Faktor angeben! (Zwischen 0 und 1, wobei 1 = Maximal mögliche Größe): "))

            if factor < 0 or factor > 1:
                raise ValueError("Factor must be between 0 and 1")
            Watermark.scale(factor, MainImage.size)
            factorFlag = 1

        except ValueError:
            print("Bitte gibt eine Gleitkomma-Zahl zwischen 0 und 1 an!")
        except Exception as e:
            print("Da ist etwas schiefgelaufen!", e)

    while isLogoPos == 0:

        try:
            print("Position des Wasserzeichens, durch 'Mausklick' bestätigen: ")
            MainImage.show()

            cv2.setMouseCallback(MainImage.name, MainImage.setLogoPosition)
            cv2.waitKey(0)

            MainImage.addWatermark(Watermark)
            MainImage.show()
            print("Drücke eine beliebige Taste, um fortzufahren!")
            cv2.waitKey(0)

        except Exception as e:
            print("Kaput!", e)

        while outputImageSatisfactory not in {"J", "j"} and outputImageSatisfactory not in {"N", "n"}:

            outputImageSatisfactory = input("Gefällt Ihnen die Position des Wasserzeichens? (J = Ja, N = Nein): ")

            try:
                if outputImageSatisfactory.upper() == "J":
                    outputImagePath = input("Bitte geben Sie einen Namen für die zu speichernde Datei an: ") + ".png"
                    MainImage.save(outputImagePath)
                    print("Bild wurde gespeichert!")
                    isLogoPos = 1

                elif outputImageSatisfactory.upper() == "N":
                    print("#DoItAgain")
                    logoPos = ""
                    MainImage = BaseImage(mainPath)

                else:
                    print("Falscher Buchstabe!")
            except Exception as e:
                print("Mehr Kaput!", e)

