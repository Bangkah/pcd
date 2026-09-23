import cv2
import matplotlib.pyplot as plt
import numpy as np


def edge_detection_process():
  # Memuat gambar
  img = cv2.imread("assets/gambar.png")
  if img is None:
    print(
        "Gagal memuat gambar 'assets/gambar.png'. Periksa kembali nama atau path"
        " file."
    )
    return

  image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  print("\n--- PENGATURAN EDGE DETECTION (CANNY) ---")
  try:
    threshold1 = float(input("Masukkan nilai Threshold 1 (misal 100): "))
    threshold2 = float(input("Masukkan nilai Threshold 2 (misal 700): "))
  except ValueError:
    print("Input harus berupa angka.")
    return

  # Deteksi tepi menggunakan Canny
  edges = cv2.Canny(image_rgb, threshold1, threshold2)

  # Menampilkan gambar asli dan hasil deteksi tepi
  fig, axs = plt.subplots(1, 2, figsize=(7, 4))
  axs[0].imshow(image_rgb)
  axs[0].set_title("Original Image")
  axs[1].imshow(edges, cmap="gray")  # Tampilan tepi biasanya cocok grayscale
  axs[1].set_title(f"Image Edges (Thresh: {threshold1}, {threshold2})")

  for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

  plt.tight_layout()
  plt.show()