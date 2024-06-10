import cv2
import numpy as np


class Watermark:
    def __init__(self, base_image_path, watermark_image_path, output_image_path):
        self.base_image_path = base_image_path
        self.watermark_image_path = watermark_image_path
        self.output_image_path = output_image_path
        self.base_image = cv2.imread(base_image_path)
        self.watermark = cv2.imread(watermark_image_path, cv2.IMREAD_UNCHANGED)

    def set_position(self, position):
        self.position = position

    def set_size(self, size):
        self.size = size
        self.watermark = cv2.resize(self.watermark, self.size, interpolation=cv2.INTER_AREA)

    def set_transparency(self, transparency):
        self.transparency = transparency

    def apply_watermark(self):
        if self.watermark.shape[2] == 4:
            b, g, r, a = cv2.split(self.watermark)
            watermark_rgb = cv2.merge((b, g, r))
            mask = a / 255.0
        else:
            watermark_rgb = self.watermark
            mask = np.ones(watermark_rgb.shape[:2], dtype=float)

        mask = mask * self.transparency
        x, y = self.position
        h, w = watermark_rgb.shape[:2]
        roi = self.base_image[y:y + h, x:x + w]

        for c in range(0, 3):
            roi[:, :, c] = roi[:, :, c] * (1 - mask) + watermark_rgb[:, :, c] * mask

        self.base_image[y:y + h, x:x + w] = roi
        cv2.imwrite(self.output_image_path, self.base_image)


# Beispiel für die Verwendung
if __name__ == "__main__":
    base_image_path = "/Users/linusollmann/PycharmProjects/Vorlesung/Ordner/Bild1.jpeg"
    watermark_image_path = "/Users/linusollmann/PycharmProjects/Vorlesung/Ordner/Logo.png"
    output_image_path = "/Users/linusollmann/PycharmProjects/Vorlesung/Ordner/Ergebnisbild.jpg"

    watermark = Watermark(base_image_path, watermark_image_path, output_image_path)
    watermark.set_position((50, 50))  # Position des Wasserzeichens (x, y)
    watermark.set_size((200, 100))  # Größe des Wasserzeichens (Breite, Höhe)
    watermark.set_transparency(0.5)  # Transparenz des Wasserzeichens (0-1)
    watermark.apply_watermark()
