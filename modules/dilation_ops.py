import cv2
import matplotlib.pyplot as plt


def dilation_process():
  image = cv2.imread("assets/image.png")
  if image is None:
    print(
        "Gagal memuat gambar 'assets/image.png'. Periksa kembali nama atau path file."
    )
    return

  # Konversi ke grayscale
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  print("\n--- PENGATURAN DILATION ---")
  print("Menerapkan serangkaian dilatasi (1 hingga 3 iterasi)...")

  # Menyiapkan subplot untuk menampilkan hasil perbandingan iterasi (1 baris, 4 kolom)
  fig, axs = plt.subplots(1, 4, figsize=(12, 3))

  # Menampilkan gambar asli (grayscale)
  axs[0].imshow(gray, cmap="gray")
  axs[0].set_title("Original Gray")

  # Melakukan perulangan untuk dilatasi sebanyak 1, 2, dan 3 kali iterasi
  for i in range(0, 3):
    # Menggunakan None agar OpenCV otomatis menggunakan structuring element 3x3 default
    dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)

    axs[i + 1].imshow(dilated, cmap="gray")
    axs[i + 1].set_title(f"Dilated {i+1}x")

  for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

  plt.tight_layout()
  plt.show()


if __name__ == "__main__":
  dilation_process()