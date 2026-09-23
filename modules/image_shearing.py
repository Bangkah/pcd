import cv2
import numpy as np
import matplotlib.pyplot as plt

# image = cv2.imread('gambar.png')
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# width, height = image_rgb.shape[1], image_rgb.shape[0]

# shearX, shearY = -0.15, 0
# transformation_matrix = np.array([[1, shearX, 0], [0, 1, shearY]], dtype=np.float32)
# sheared_image = cv2.warpAffine(image_rgb, transformation_matrix, (width, height))

# fig, axs = plt.subplots(1, 2, figsize=(7, 4))
# axs[0].imshow(image_rgb), axs[0].set_title('Original Image')
# axs[1].imshow(sheared_image), axs[1].set_title('Sheared Image')

# for ax in axs:
#     ax.set_xticks([]), ax.set_yticks([])

# plt.tight_layout()
# plt.show()

import cv2
import matplotlib.pyplot as plt
import numpy as np


def shear_image_process():
  # Memuat gambar
  image = cv2.imread("assets/ gambar.png")
  if image is None:
    print(
        "Gagal memuat gambar 'assets/gambar.png'. Periksa kembali nama atau path"
        " file."
    )
    return

  image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  width, height = image_rgb.shape[1], image_rgb.shape[0]

  print("\n--- PENGATURAN IMAGE SHEARING ---")
  try:
    shearX = float(
        input("Masukkan nilai shear X (horizontal, misal -0.15 atau 0.2): ")
    )
    shearY = float(
        input("Masukkan nilai shear Y (vertikal, misal 0.0 atau 0.15): ")
    )
  except ValueError:
    print("Input harus berupa angka.")
    return

  # Matriks transformasi shearing
  transformation_matrix = np.array(
      [[1, shearX, 0], [0, 1, shearY]], dtype=np.float32
  )
  sheared_image = cv2.warpAffine(
      image_rgb, transformation_matrix, (width, height)
  )

  # Menampilkan gambar menggunakan Matplotlib
  fig, axs = plt.subplots(1, 2, figsize=(7, 4))
  axs[0].imshow(image_rgb)
  axs[0].set_title("Original Image")
  axs[1].imshow(sheared_image)
  axs[1].set_title(f"Sheared Image (X={shearX}, Y={shearY})")

  for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

  plt.tight_layout()
  plt.show()