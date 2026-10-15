import cv2
import matplotlib.pyplot as plt
import numpy as np


def power_law_process():
  # Memuat gambar dari folder assets
  image = cv2.imread("assests/gambar.png")
  if image is None:
    print(
        "Gagal memuat gambar dari folder assets. Periksa kembali nama atau path"
        " file."
    )
    return

  image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

  print("\n--- PENGATURAN POWER-LAW (GAMMA) TRANSFORMATION ---")
  try:
    gamma = float(
        input(
            "Masukkan nilai Gamma (misal: 0.5 untuk mencerahkan, 2.0 untuk"
            " menggelapkan): "
        )
    )
  except ValueError:
    print("Input harus berupa angka.")
    return

  # 1. Normalisasi citra ke rentang [0, 1]
  normalized = image_rgb / 255.0

  # 2. Terapkan rumus Power-Law: s = c * (r ^ gamma) dengan c = 1
  corrected = np.array(255 * (normalized**gamma), dtype=np.uint8)

  # Menampilkan gambar asli dan hasil transformasi gamma
  fig, axs = plt.subplots(1, 2, figsize=(7, 4))
  axs[0].imshow(image_rgb)
  axs[0].set_title("Original Image")

  axs[1].imshow(corrected)
  axs[1].set_title(f"Power-Law Transformation ($\gamma$ = {gamma})")

  for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

  plt.tight_layout()
  plt.show()


if __name__ == "__main__":
  power_law_process()