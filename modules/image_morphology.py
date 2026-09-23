import cv2
import matplotlib.pyplot as plt
import numpy as np


def morphology_image_process():
  # Memuat gambar
  image = cv2.imread("assets/gambar.png")
  if image is None:
    print(
        "Gagal memuat gambar 'assets/gambar.png'. Periksa kembali nama atau path"
        " file."
    )   
    return

  image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  print("\n--- PENGATURAN MORPHOLOGICAL OPERATIONS ---")
  try:
    kernel_size = int(
        input("Masukkan ukuran kernel (bilangan ganjil, misal 3 atau 5): ")
    )
    iterations = int(input("Masukkan jumlah iterasi (misal 1 atau 2): "))
  except ValueError:
    print("Input harus berupa angka bulat.")
    return

  # Membuat kernel berdasarkan input ukuran
  kernel = np.ones((kernel_size, kernel_size), np.uint8)

  # Proses operasi morfologi
  dilated = cv2.dilate(image_gray, kernel, iterations=iterations)
  eroded = cv2.erode(image_gray, kernel, iterations=iterations)
  opening = cv2.morphologyEx(image_gray, cv2.MORPH_OPEN, kernel)
  closing = cv2.morphologyEx(image_gray, cv2.MORPH_CLOSE, kernel)

  # Menampilkan hasil menggunakan Matplotlib (grid 2x2)
  fig, axs = plt.subplots(2, 2, figsize=(8, 8))
  axs[0, 0].imshow(dilated, cmap="Greys")
  axs[0, 0].set_title(f"Dilated Image (Iter: {iterations})")

  axs[0, 1].imshow(eroded, cmap="Greys")
  axs[0, 1].set_title(f"Eroded Image (Iter: {iterations})")

  axs[1, 0].imshow(opening, cmap="Greys")
  axs[1, 0].set_title("Opening")

  axs[1, 1].imshow(closing, cmap="Greys")
  axs[1, 1].set_title("Closing")

  for ax in axs.flatten():
    ax.set_xticks([])
    ax.set_yticks([])

  plt.tight_layout()
  plt.show()