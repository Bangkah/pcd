import cv2
import matplotlib.pyplot as plt
import numpy as np


def blur_image_process():
  # Memuat gambar
  image = cv2.imread("assets/gambar.png")
  if image is None:
    print(
        "Gagal memuat gambar 'assets/gambar.png'. Periksa kembali nama atau path"
        " file."
    )
    return

  image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

  print("\n--- PENGATURAN IMAGE BLURRING (GAUSSIAN) ---")
  try:
    k_size = int(
        input(
            "Masukkan ukuran kernel blur (harus bilangan ganjil, misal 3, 5,"
            " 9): "
        )
    )
    # Validasi sederhana agar ukuran kernel ganjil
    if k_size % 2 == 0:
      print("Ukuran kernel harus bilangan ganjil. Otomatis disesuaikan ke", k_size + 1)
      k_size += 1
  except ValueError:
    print("Input harus berupa angka bulat.")
    return

  # Proses Gaussian Blur (menggunakan k_size untuk lebar dan tinggi kernel)
  blurred = cv2.GaussianBlur(image, (k_size, k_size), 0)
  blurred_rgb = cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB)

  # Menampilkan gambar asli dan hasil blur menggunakan Matplotlib
  fig, axs = plt.subplots(1, 2, figsize=(7, 4))
  axs[0].imshow(image_rgb)
  axs[0].set_title("Original Image")
  axs[1].imshow(blurred_rgb)
  axs[1].set_title(f"Blurred Image (Kernel: {k_size}x{k_size})")

  for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

  plt.tight_layout()
  plt.show()