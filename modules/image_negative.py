import cv2
import matplotlib.pyplot as plt
import numpy as np


def negative_image_process():
  # Memuat gambar dari folder assets
  image = cv2.imread("assests/image.jpg")
  if image is None:
    print(
        "Gagal memuat gambar dari folder assets. Periksa kembali nama atau path"
        " file."
    )
    return

  image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

  print("\n--- PENGATURAN IMAGE INVERSION (NEGATIF) ---")
  print("Membalikkan intensitas piksel (terang jadi gelap, gelap jadi terang)...")

  # Proses inversi citra (255 - nilai piksel)
  inverted_image = 255 - image_rgb

  # Menampilkan gambar asli dan hasil inversi
  fig, axs = plt.subplots(1, 2, figsize=(7, 4))
  axs[0].imshow(image_rgb)
  axs[0].set_title("Original Image")
  axs[1].imshow(inverted_image)
  axs[1].set_title("Inverted / Negative Image")

  for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

  plt.tight_layout()
  plt.show()


if __name__ == "__main__":
  negative_image_process()