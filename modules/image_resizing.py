import cv2
import numpy as np
import matplotlib.pyplot as plt

# image = cv2.imread('gambar.png')
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# scale_factor_1 =3.0
# scale_factor_2 =1/3.0
# height, width =image_rgb.shape[:2]
# new_height = int(height * scale_factor_1)
# new_width = int(width * scale_factor_1)

# zoomed_image = cv2.resize(src = image_rgb, dsize=(new_width, new_height), interpolation=cv2.INTER_CUBIC)

# new_height_1 = int(height * scale_factor_2)
# new_width_1 = int(width * scale_factor_2)
# scaled_image = cv2.resize(src=image_rgb, dsize=(new_width_1, new_height_1), interpolation=cv2.INTER_AREA)

# fig,axs = plt.subplots(1,3, figsize=(10, 4))
# axs[0].imshow(image_rgb)
# axs[0].set_title('Original Image Shape:'+str(image_rgb.shape))
# axs[1].imshow(zoomed_image)
# axs[1].set_title('Zoomed Image Shape:'+str(zoomed_image.shape))
# axs[2].imshow(scaled_image)
# axs[2].set_title('Scaled Image Shape:'+str(scaled_image.shape))

# for ax in axs:
#     ax.set_xticks([])
#     ax.set_yticks([])


def resize_image_process():
  # Memuat gambar (sesuaikan nama file jika perlu)
  image = cv2.imread("assets/gambar.png")
  if image is None:
    print(
        "Gagal memuat gambar 'assets/gambar.png'. Periksa kembali nama atau path"
        " file."
    )
    return

  image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  height, width = image_rgb.shape[:2]

  print("\n--- PENGATURAN RESIZING ---")
  try:
    scale_factor_1 = float(
        input("Masukkan faktor Zoom In (misal 3.0): ")
    )  # Contoh: 3.0
    scale_factor_2 = float(
        input("Masukkan faktor Scale/Zoom Out (misal 0.33 atau 0.5): ")
    )  # Contoh: 1/3.0 atau 0.5
  except ValueError:
    print("Input harus berupa angka.")
    return

  # Proses Zoom In
  new_height = int(height * scale_factor_1)
  new_width = int(width * scale_factor_1)
  zoomed_image = cv2.resize(
      src=image_rgb,
      dsize=(new_width, new_height),
      interpolation=cv2.INTER_CUBIC,
  )

  # Proses Scale / Zoom Out
  new_height1 = int(height * scale_factor_2)
  new_width1 = int(width * scale_factor_2)
  scaled_image = cv2.resize(
      src=image_rgb,
      dsize=(new_width1, new_height1),
      interpolation=cv2.INTER_AREA,
  )

  # Menampilkan hasil menggunakan Matplotlib
  fig, axs = plt.subplots(1, 3, figsize=(12, 4))
  axs[0].imshow(image_rgb)
  axs[0].set_title("Original\n" + str(image_rgb.shape))

  axs[1].imshow(zoomed_image)
  axs[1].set_title("Zoomed In\n" + str(zoomed_image.shape))

  axs[2].imshow(scaled_image)
  axs[2].set_title("Scaled / Zoom Out\n" + str(scaled_image.shape))

  for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

  plt.tight_layout()
  plt.show()