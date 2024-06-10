import cv2
import numpy as np
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

        try:
            self.base_image = cv2.imread(self.base_image_path)
            if self.base_image is None:
                raise ValueError(f"Konnte das Basisbild unter {self.base_image_path} nicht laden.")

            self.watermark = cv2.imread(self.watermark_image_path, cv2.IMREAD_UNCHANGED)
            if self.watermark is None:
                raise ValueError(f"Konnte das Wasserzeichenbild unter {self.watermark_image_path} nicht laden.")
        except Exception as e:
            print(f"Fehler beim Laden der Bilder: {e}")

    def set_position(self, position):
        self.position = position

    def set_size(self, size):
        try:
            self.size = size
            self.watermark = cv2.resize(self.watermark, self.size, interpolation=cv2.INTER_AREA)
        except Exception as e:
            print(f"Fehler bei der Größenanpassung des Wasserzeichens: {e}")

    def set_transparency(self, transparency):
        if 0 <= transparency <= 1:
            self.transparency = transparency
        else:
            print("Transparenz muss zwischen 0 und 1 liegen.")

    def apply_watermark(self):
        try:
            if self.watermark.shape[2] == 4:
                b, g, r, a = cv2.split(self.watermark)
                watermark_rgb = cv2.merge((b, g, r))
                mask = a / 255.0
            else:
                watermark_rgb = self.watermark
                b, g, r = cv2.split(watermark_rgb)
                mask = (b+g+r)/255.0
            mask = mask * self.transparency
            x, y = self.position
            h, w = watermark_rgb.shape[:2]

            if y + h > self.base_image.shape[0] or x + w > self.base_image.shape[1]:
                raise ValueError("Das Wasserzeichen passt nicht in das Basisbild an der angegebenen Position.")

            roi = self.base_image[y:y + h, x:x + w]

            for c in range(0, 3):
                roi[:, :, c] = roi[:, :, c] * (1 - mask) + watermark_rgb[:, :, c] * mask

            self.base_image[y:y + h, x:x + w] = roi
            cv2.imwrite(self.output_image_path, self.base_image)
            print(f"Erfolgreich gespeichert unter {self.output_image_path}")
        except Exception as e:
            print(f"Fehler beim Anwenden des Wasserzeichens: {e}")


# Beispiel für die Verwendung
if __name__ == "__main__":
    base_image_name = "Bild1.jpeg"
    watermark_image_name = "Bild1.jpeg"
    output_image_name = "Ergebnisbild.jpg"

    watermark = Watermark(base_image_name, watermark_image_name, output_image_name)
    watermark.set_position((50, 50))  # Position des Wasserzeichens (x, y)
    watermark.set_size((200, 100))  # Größe des Wasserzeichens (Breite, Höhe)
    watermark.set_transparency(0.5)  # Transparenz des Wasserzeichens (0-1)
    watermark.apply_watermark()
