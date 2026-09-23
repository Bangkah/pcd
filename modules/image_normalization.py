import cv2
import matplotlib.pyplot as plt
import numpy as np


def normalize_image_process():
  # Memuat gambar
  image = cv2.imread("assets/gambar.png")
  if image is None:
    print(
        "Gagal memuat gambar 'assets/gambar.png'. Periksa kembali nama atau path"
        " file."
    )
    return

  image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  b, g, r = cv2.split(image_rgb)

  # Normalisasi masing-masing channel warna ke rentang [0, 1]
  b_normalized = cv2.normalize(
      b.astype("float"), None, 0, 1, cv2.NORM_MINMAX
  )
  g_normalized = cv2.normalize(
      g.astype("float"), None, 0, 1, cv2.NORM_MINMAX
  )
  r_normalized = cv2.normalize(
      r.astype("float"), None, 0, 1, cv2.NORM_MINMAX
  )

  normalized_image = cv2.merge((b_normalized, g_normalized, r_normalized))

  print("\n--- PENGATURAN IMAGE NORMALIZATION ---")
  print("Matriks channel Biru (B) yang telah dinormalisasi:")
  print(
      normalized_image[:, :, 0]
  )  # Menampilkan sebagian atau seluruh matriks channel B

  # Menampilkan gambar asli dan hasil normalisasi
  fig, axs = plt.subplots(1, 2, figsize=(7, 4))
  axs[0].imshow(image_rgb)
  axs[0].set_title("Original Image")
  axs[1].imshow(normalized_image)
  axs[1].set_title("Normalized Image")

  for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

  plt.tight_layout()
  plt.show()