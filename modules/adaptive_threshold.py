import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import threshold_local


def adaptive_threshold_process():
  # Memuat gambar dari folder assets
  image = cv2.imread("assests/image.png")
  if image is None:
    print(
        "Gagal memuat gambar dari folder assets. Periksa kembali nama atau path"
        " file."
    )
    return

  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  print("\n--- PENGATURAN ADAPTIVE THRESHOLDING ---")
  print("Menerapkan local/adaptive thresholding pada citra...")

  # Parameter block_size (harus bernilai ganjil, misal 41) dan offset
  block_size = 41
  offset = 10

  # Menghitung ambang batas lokal menggunakan scikit-image
  local_thresh = threshold_local(gray, block_size, offset=offset)
  binary_image = gray > local_thresh

  # Konversi boolean array ke tipe data uint8 (0 dan 255)
  binary_image_uint8 = np.array(binary_image * 255, dtype=np.uint8)

  # Menampilkan gambar asli (grayscale) dan hasil adaptive thresholding
  fig, axs = plt.subplots(1, 2, figsize=(7, 4))
  axs[0].imshow(gray, cmap="gray")
  axs[0].set_title("Original Grayscale")

  axs[1].imshow(binary_image_uint8, cmap="gray")
  axs[1].set_title(f"Adaptive Threshold (Block={block_size}, Offset={offset})")

  for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

  plt.tight_layout()
  plt.show()


if __name__ == "__main__":
  adaptive_threshold_process()