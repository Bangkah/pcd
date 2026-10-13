import cv2
import matplotlib.pyplot as plt
import numpy as np


def inverse_image_process():
  # Memuat gambar dari folder assets
  image = cv2.imread("C:\\Users\\atha\\Documents\\PCD\\assests\\grayscale.png")
  if image is None:
    print(
        "Gagal memuat gambar dari folder assets. Periksa kembali nama atau path"
        " file."
    )
    return

  image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

  print("\n--- PENGATURAN INTENSITY ADDITION ---")
  print("Menambahkan nilai piksel sebanyak 50 pada citra...")

  # Menggunakan cv2.add agar terjadi saturasi (jika melebihi 255, otomatis dibatasi di 255, bukan kembali ke 0)
  value = np.array([50, 50, 50], dtype=np.uint8)
  added_image = cv2.add(image_rgb, value)

  # Menampilkan gambar asli dan hasil penambahan
  fig, axs = plt.subplots(1, 2, figsize=(7, 4))
  axs[0].imshow(image_rgb)
  axs[0].set_title("Original Image")
  axs[1].imshow(added_image)
  axs[1].set_title("Image Intensity + 50")

  for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

  plt.tight_layout()
  plt.show()


if __name__ == "__main__":
  inverse_image_process()

  import math
  import scipy.misc
  import numpy as np
