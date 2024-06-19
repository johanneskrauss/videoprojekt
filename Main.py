import io
import sys

import Utils
import cv2
from Utils import TextImage

from BaseImage import BaseImage
from Logo import Logo

# Dateipfade
mainPath = ""
watermarkPath = ""

# Variablen
transparency = 0
factor = 0

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
        except FileNotFoundError as e:
            print("Datei konnte nicht gefunden werden!", e)
            mainPath = ""
        except ValueError as e:
            print("Das Dateiformat ist falsch!", e)
            mainPath = ""
        except AttributeError as e:
            print("Bitte eine Bilddatei auswählen! (.jpg, .png, .bmp, ...) oder Pfad existiert nicht!", e)
            mainPath = ""

    while watermarkPath == "":
        TextImage = TextImage()

        text_oder_bild = input("Möchten Sie Text oder ein Bild einfügen? (t=Text, b=Bild)")

        if text_oder_bild.lower() == "t":

            TextImage.selectText(input("Bitte geben Sie den Text ein: "))
            TextImage.selectFontColor(input("Bitte geben Sie die Schriftfarbe an (S=Schwarz, W=Weiß, G=Grau): "))
            TextImage.createTextImage()
            watermarkPath = "text_logo.png"
            break
        elif text_oder_bild.lower() == "b":
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

    while isWatermark == 0:
        try:
            transparency = float(input("Bitte den Grad der Transparenz angeben! (Zwischen 0 und 1, wobei 1 = 100% Deckkraft): "))

            if transparency < 0 or transparency > 1:
                raise ValueError("Transparency must be between 0 and 1")

            Watermark = Logo(transparency, watermarkPath)
            TextImage.deleteFile()
            MainImage.alignLogo(Watermark)

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
            except ValueError as e:
                print("Bitte gibt eine Gleitkomma-Zahl zwischen 0 und 1 an!", e)
            except Exception as e:
                print("Da ist etwas schiefgelaufen!", e)

        while isLogoPos == 0:

            try:
                print("Position des Wasserzeichens, durch 'Mausklick' bestätigen: ")
                MainImage.show()

                cv2.setMouseCallback(MainImage.name, MainImage.setLogoPosition)
                cv2.waitKey(0)
                MainImage.close()

                MainImage.addWatermark(Watermark)
                MainImage.show()
                print("Drücke eine beliebige Taste, um fortzufahren!")
                cv2.waitKey(0)
                outputImageSatisfactory = ""
                isLogoPos = 1

            except Exception as e:
                print("Hier lief etwas schief: ", e)

        while outputImageSatisfactory != "J" and outputImageSatisfactory != "N":

            outputImageSatisfactory = input("Gefällt Ihnen das Wasserzeichen? (J = Ja, N = Nein): ").upper()

            try:
                if outputImageSatisfactory == "J":
                    outputImagePath = input("Bitte geben Sie einen Namen für die zu speichernde Datei an: ") + ".png"
                    MainImage.save(outputImagePath)
                    print("Bild wurde gespeichert!")
                    isWatermark = 1

                elif outputImageSatisfactory == "N":
                    print("#DoItAgain")
                    isLogoPos = 0
                    MainImage = BaseImage(mainPath)
                    factorFlag = 0
                    isWatermark = 0

                else:
                    print("Falscher Buchstabe!")
            except Exception as e:
                print("Hier lief etwas schief: ", e)
