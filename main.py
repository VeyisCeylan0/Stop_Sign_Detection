import cv2
import numpy as np
import os

INPUT_FOLDER = "images"          # STOP tabelasi fotograflarinin oldugu klasor
OUTPUT_FOLDER = "output_images"  # Tespit sonrasi kaydedilecek klasor


def detect_stop_sign():

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    if not os.path.isdir(INPUT_FOLDER):
        print(f"Hata: '{INPUT_FOLDER}' klasoru bulunamadi.")
        return

    files = os.listdir(INPUT_FOLDER)

    for filename in files:
        if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        img_path = os.path.join(INPUT_FOLDER, filename)
        img = cv2.imread(img_path)

        if img is None:
            print(f"Hata: {filename} okunamadi.")
            continue

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        lower_red1 = np.array([0, 120, 70])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([150, 120, 70])
        upper_red2 = np.array([180, 255, 255])

        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask = mask1 + mask2

        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) == 0:
            print(f"Gorsel: {filename} -> STOP tabelasi bulunamadi.")
            continue

        largest_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_contour)

        min_area = 0.001 * img.shape[0] * img.shape[1]

        if area < min_area:
            print(f"Gorsel: {filename} -> Yeterince buyuk kirmizi alan bulunamadi.")
            continue

        x, y, w, h = cv2.boundingRect(largest_contour)

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        center_x = int(x + w / 2)
        center_y = int(y + h / 2)
        cv2.circle(img, (center_x, center_y), 5, (255, 0, 0), -1)

        print(f"Gorsel: {filename} -> Merkez Konumu: x={center_x}, y={center_y}")

        output_path = os.path.join(OUTPUT_FOLDER, "detected_" + filename)
        cv2.imwrite(output_path, img)


if __name__ == "__main__":
    detect_stop_sign()