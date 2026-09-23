import cv2
import matplotlib.pyplot as plt
import numpy as np

# img = cv2.imread('gambar.png')
# image_rgb =  cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# width, height =  image_rgb.shape[1], image_rgb.shape[0]

# tx, ty = 100, 70
# translation_matrix = np.array([[1, 0, tx], [0, 1, ty]], dtype=np.float32)
# translated_image = cv2.warpAffine(image_rgb, translation_matrix, (width, height))

# fig, axs  =  plt.subplots(1, 2, figsize=(7, 4))
# axs[0].imshow(image_rgb), axs[0].set_title('Original  Image')
# axs[1].imshow(translated_image), axs[1].set_title('Translated Image')

# for ax  in  axs:
#     ax.set_xticks([]), ax.set_yticks([])

# plt.tight_layout()
# plt.show()


def translate_image_process():
  # Memuat gambar
  img = cv2.imread("assets/gambar.png")
  if img is None:
    print(
        "Gagal memuat gambar 'assets/gambar.png'. Periksa kembali nama atau path"
        " file."
    )
    return

  image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  width, height = image_rgb.shape[1], image_rgb.shape[0]

  print("\n--- PENGATURAN IMAGE TRANSLATION ---")
  try:
    tx = float(
        input("Masukkan nilai translasi pada sumbu x (geser kanan +, kiri -): ")
    )
    ty = float(
        input("Masukkan nilai translasi pada sumbu y (geser bawah +, atas -): ")
    )
  except ValueError:
    print("Input harus berupa angka.")
    return

  # Matriks translasi
  translation_matrix = np.array([[1, 0, tx], [0, 1, ty]], dtype=np.float32)
  translated_image = cv2.warpAffine(
      image_rgb, translation_matrix, (width, height)
  )

  # Menampilkan gambar menggunakan Matplotlib
  fig, axs = plt.subplots(1, 2, figsize=(7, 4))
  axs[0].imshow(image_rgb)
  axs[0].set_title("Original Image")
  axs[1].imshow(translated_image)
  axs[1].set_title(f"Image Translation (X={tx}, Y={ty})")

  for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

  plt.tight_layout()
  plt.show()