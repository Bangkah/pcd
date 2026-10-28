import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import threshold_otsu


def otsu_threshold_process():
  # Memuat gambar dari folder assets dan ubah ke grayscale
  image = cv2.imread("assests/mobil.png")
  if image is None:
    print(
        "Gagal memuat gambar dari folder assets. Periksa kembali nama atau path"
        " file."
    )
    return

  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  print("\n--- PENGATURAN OTSU'S THRESHOLDING ---")
  print("Menghitung nilai ambang batas (threshold) optimal secara otomatis...")

  # 1. Menghitung nilai threshold optimal menggunakan metode Otsu dari scikit-image
  thresh = threshold_otsu(gray)
  print(f"Nilai Otsu Threshold yang didapat: {thresh}")

  # 2. Melakukan binerisasi: piksel di atas threshold bernilai True (putih/1), sisanya False (hitam/0)
  binary_image = gray > thresh

  # Konversi boolean array ke tipe data uint8 (0 dan 255) agar bisa ditampilkan dengan benar
  binary_image_uint8 = np.array(binary_image * 255, dtype=np.uint8)

  # Menampilkan gambar asli (grayscale) dan hasil Otsu's Thresholding
  fig, axs = plt.subplots(1, 2, figsize=(7, 4))
  axs[0].imshow(gray, cmap="gray")
  axs[0].set_title("Original Grayscale")

  axs[1].imshow(binary_image_uint8, cmap="gray")
  axs[1].set_title(f"Otsu Threshold (Thresh = {int(thresh)})")

  for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

  plt.tight_layout()
  plt.show()


if __name__ == "__main__":
  otsu_threshold_process()