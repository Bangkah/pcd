import cv2
import matplotlib.pyplot as plt
# img = cv2.imread('gambar.png')
# image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# center = (image_rgb.shape[1] // 2, image_rgb.shape[0] // 2)
# angle = 30
# scale = 1
# rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
# rotated_image = cv2.warpAffine(image_rgb, rotation_matrix, (img.shape[1], img.shape[0]))

# fig, axs = plt.subplots(1, 2, figsize=(7, 4))
# axs[0].imshow(image_rgb)
# axs[0].set_title('Original Image')
# axs[1].imshow(rotated_image)
# axs[1].set_title('Image Rotation')
# for ax in axs:
#     ax.set_xticks([])
#     ax.set_yticks([])
    
# plt.tight_layout()
# plt.show()


def rotate_image_process():
  # Memuat gambar
  img = cv2.imread("assets/gambar.png")
  if img is None:
    print(
        "Gagal memuat gambar 'assets/gambar.png'. Periksa kembali nama atau path"
        " file."
    )
    return

  image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  center = (image_rgb.shape[1] // 2, image_rgb.shape[0] // 2)

  print("\n--- PENGATURAN ROTASI ---")
  try:
    angle = float(
        input("Masukkan sudut rotasi (derajat, contoh: 30 atau 90): ")
    )
  except ValueError:
    print("Input sudut harus berupa angka.")
    return

  scale = 1.0
  rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
  rotated_image = cv2.warpAffine(
      image_rgb, rotation_matrix, (img.shape[1], img.shape[0])
  )

  # Menampilkan hasil dengan Matplotlib
  fig, axs = plt.subplots(1, 2, figsize=(7, 4))
  axs[0].imshow(image_rgb)
  axs[0].set_title("Original Image")
  axs[1].imshow(rotated_image)
  axs[1].set_title(f"Image Rotation ({angle}°)")

  for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

  plt.tight_layout()
  plt.show()