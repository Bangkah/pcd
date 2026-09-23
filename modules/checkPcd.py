import os
import cv2
import numpy as np

filename = "assets/image.jpg"

if not os.path.exists(filename):
    print(
        f"[INFO] File '{filename}' tidak ditemukan di folder C:\\Users\\atha\\Documents\\PCD"
    )
    print("[INFO] Membuat gambar sampel otomatis ('image.jpg')...")

    sample_img = np.ones((400, 400, 3), dtype=np.uint8) * 255
    cv2.circle(sample_img, (200, 200), 80, (0, 0, 255), -1)
    cv2.rectangle(sample_img, (250, 250), (350, 350), (255, 0, 0), -1)

    cv2.imwrite(filename, sample_img)

img = cv2.imread(filename)

if img is None:
    print(f"[EROR] File '{filename}' gagal dibaca atau corrupt!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, threshold1=100, threshold2=200)

print("[SUCCESS] Pemrosesan citra berhasil!")
print("Menampilkan jendela gambar... (Tekan tombol apa saja untuk menutup)")

cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Canny Edge Detection", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()