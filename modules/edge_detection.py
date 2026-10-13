import os
from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


def cari_gambar():
  base_dir = Path(__file__).resolve().parent.parent
  kandidat = [
      base_dir / "assests" / "gambar.png",
      base_dir / "assets" / "gambar.png",
      base_dir / "assests" / "image.png",
      base_dir / "assets" / "image.png",
      base_dir / "assests" / "mobil.png",
      base_dir / "assets" / "mobil.png",
  ]

  for path in kandidat:
    if path.exists():
      return str(path)

  raise FileNotFoundError(
      "Tidak ditemukan file gambar pendukung di folder 'assests/' atau 'assets/'."
  )


def prewitt_edge(gray_image):
  kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
  kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)

  gx = cv2.filter2D(gray_image, cv2.CV_32F, kernel_x)
  gy = cv2.filter2D(gray_image, cv2.CV_32F, kernel_y)
  magnitude = np.sqrt(gx**2 + gy**2)
  magnitude = np.uint8(np.clip(magnitude, 0, 255))
  return magnitude


def sobel_edge(gray_image):
  gx = cv2.Sobel(gray_image, cv2.CV_32F, 1, 0, ksize=3)
  gy = cv2.Sobel(gray_image, cv2.CV_32F, 0, 1, ksize=3)
  magnitude = np.sqrt(gx**2 + gy**2)
  magnitude = np.uint8(np.clip(magnitude, 0, 255))
  return magnitude


def edge_detection_process():
  try:
    image_path = cari_gambar()
    img = cv2.imread(image_path)
  except FileNotFoundError as e:
    print(e)
    return

  if img is None:
    print(f"Gagal memuat gambar '{image_path}'. Silakan cek path atau file gambar.")
    return

  image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  print("\n--- PENGATURAN EDGE DETECTION (PREWITT, SOBEL, CANNY) ---")
  print("1. Prewitt")
  print("2. Sobel")
  print("3. Canny")

  try:
    metode = input("Pilih metode edge detection (1-3): ")
  except ValueError:
    print("Input tidak valid.")
    return

  if metode == "1":
    edges = prewitt_edge(gray_image)
    title = "Prewitt Edge Detection"
  elif metode == "2":
    edges = sobel_edge(gray_image)
    title = "Sobel Edge Detection"
  elif metode == "3":
    try:
      threshold1 = float(input("Masukkan nilai Threshold 1 (misal 100): "))
      threshold2 = float(input("Masukkan nilai Threshold 2 (misal 150): "))
    except ValueError:
      print("Input harus berupa angka.")
      return
    edges = cv2.Canny(gray_image, threshold1, threshold2)
    title = f"Canny Edge Detection (Thresh: {threshold1}, {threshold2})"
  else:
    print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
    return

  fig, axs = plt.subplots(1, 2, figsize=(8, 4))
  axs[0].imshow(image_rgb)
  axs[0].set_title("Original Image")
  axs[1].imshow(edges, cmap="gray")
  axs[1].set_title(title)

  for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

  plt.tight_layout()
  plt.show()