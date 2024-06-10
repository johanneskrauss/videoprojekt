import cv2
import numpy as np
from tkinter import filedialog
import os


class Watermark:
    def __init__(self, base_image_name, watermark_image_name, output_image_name):
        self.base_image_name = base_image_name
        self.watermark_image_name = watermark_image_name
        self.output_image_name = output_image_name

        # Verzeichnis des aktuellen Skripts
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

        # Absolute Pfade zu den Bildern
        self.base_image_path = os.path.join(self.script_dir, self.base_image_name)
        self.watermark_image_path = os.path.join(self.script_dir, self.watermark_image_name)
        self.output_image_path = os.path.join(self.script_dir, self.output_image_name)

        self.base_image = None
        self.watermark = None
        self.position = (0, 0)
        self.size = None
        self.transparency = 1.0

def add_watermark(base_image_path, watermark_image_path, output_image_path, position, size, transparency):
    """
    Fügt ein Wasserzeichen zu einem Bild hinzu.

    :param base_image_path: Pfad zum Basisbild
    :param watermark_image_path: Pfad zum Wasserzeichenbild
    :param output_image_path: Pfad zum Ausgabe-Bild
    :param position: Tuple (x, y) für die Position des Wasserzeichens
    :param size: Tuple (width, height) für die Größe des Wasserzeichens
    :param transparency: Transparenz des Wasserzeichens (0-1)
    """
    # Basisbild und Wasserzeichen laden
    base_image = cv2.imread(base_image_path)
    watermark = cv2.imread(watermark_image_path, cv2.IMREAD_UNCHANGED)

    # Größe des Wasserzeichens anpassen
    watermark = cv2.resize(watermark, size, interpolation=cv2.INTER_AREA)

    # Wasserzeichen in RGBA zerlegen
    if watermark.shape[2] == 4:
        b, g, r, a = cv2.split(watermark)
        watermark_rgb = cv2.merge((b, g, r))
        mask = a / 255.0
    else:
        watermark_rgb = watermark
        mask = np.ones(watermark_rgb.shape[:2], dtype=float)

    # Transparenz anwenden
    mask = mask * transparency

    x, y = position
    h, w = watermark_rgb.shape[:2]

    # ROI für das Wasserzeichen festlegen
    roi = base_image[y:y+h, x:x+w]

    # Wasserzeichen hinzufügen
    for c in range(0, 3):
        roi[:, :, c] = roi[:, :, c] * (1 - mask) + watermark_rgb[:, :, c] * mask

    # Ergebnis speichern
    base_image[y:y+h, x:x+w] = roi
    cv2.imwrite(output_image_path, base_image)

def select_file():
    file = filedialog.askopenfilename()
    return file


# Beispiel für die Verwendung
if __name__ == "__main__":
    base_image_path = select_file()
    watermark_image_path = select_file()
    output_image_path = input("Bitte geben Sie einen Namen für die zu speichernde Datei an: ") + ".jpg"

    position = (50, 50)  # Position des Wasserzeichens (x, y)
    size = (100, 100)  # Größe des Wasserzeichens (Breite, Höhe)
    transparency = 0.6  # Transparenz des Wasserzeichens (0-1)

    add_watermark(base_image_path, watermark_image_path, output_image_path, position, size, transparency)
