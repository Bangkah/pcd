import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import threshold_otsu


def otsu_threshold_process():
  # Memuat gambar dari folder assets
  image_path = "C:\\Users\\atha\\Documents\\PCD\\assests\\image.jpg"
  image = cv2.imread(image_path)
  if image is None:
    print(
        f"Gagal memuat gambar dari path: {image_path}. Periksa kembali path"
        " file."
    )
    return

  # Mengonversi BGR ke RGB untuk ditampilkan dengan benar oleh Matplotlib
  image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

  # 1. Mengubah citra warna (BGR) menjadi Grayscale (Keabuan)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  print("\n--- PROSES OTSU'S THRESHOLDING ---")
  print("Menghitung threshold optimal secara otomatis...")

  # 2. Menghitung nilai ambang batas (threshold) optimal secara otomatis menggunakan Otsu
  thresh = threshold_otsu(gray)
  print(f"Nilai Otsu Threshold yang didapat: {int(thresh)}")

  # 3. Melakukan binerisasi:
  # Piksel di atas nilai threshold akan menjadi Putih (True), sisanya Hitam (False)
  binary_image = gray > thresh

  # Konversi array boolean ke format gambar 8-bit (0 sampai 255)
  # (Diperbaiki dari kode sebelumnya yang kurang tanda kali *)
  binary_image_uint8 = np.array(binary_image * 255, dtype=np.uint8)

  # 4. Menampilkan perbandingan: 3 kolom (Asli Berwarna, Grayscale, Hasil Otsu)
  fig, axs = plt.subplots(1, 3, figsize=(12, 4))

  # Kolom 0: Gambar Asli Berwarna
  axs[0].imshow(image_rgb)
  axs[0].set_title("Original Image")
  axs[0].axis("off")

  # Kolom 1: Gambar Grayscale
  axs[1].imshow(gray, cmap="gray")
  axs[1].set_title("Original Grayscale")
  axs[1].axis("off")

  # Kolom 2: Hasil Otsu Segmentation
  axs[2].imshow(binary_image_uint8, cmap="gray")
  axs[2].set_title(f"Otsu Segmentation (Thresh = {int(thresh)})")
  axs[2].axis("off")

  plt.tight_layout()
  plt.show()


if __name__ == "__main__":
  otsu_threshold_process()