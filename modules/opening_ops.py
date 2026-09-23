import cv2
import matplotlib.pyplot as plt


def opening_process():
  image = cv2.imread("assets/image.png")
  if image is None:
    print(
        "Gagal memuat gambar 'assets/image.png'. Periksa kembali nama atau path file."
    )
    return

  # Konversi ke grayscale
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  print("\n--- PENGATURAN OPENING ---")
  print("Menerapkan operasi Opening dengan berbagai ukuran kernel...")

  # Daftar ukuran kernel yang akan diuji
  kernel_sizes = [(3, 3), (5, 5), (7, 7)]

  # Menyiapkan subplot untuk menampilkan hasil (1 baris untuk asli + 3 ukuran kernel)
  fig, axs = plt.subplots(1, 4, figsize=(14, 3))

  # Menampilkan gambar asli (grayscale)
  axs[0].imshow(gray, cmap="gray")
  axs[0].set_title("Original Gray")

  # Melakukan perulangan berdasarkan ukuran kernel
  for idx, k_size in enumerate(kernel_sizes):
    # Membuat structuring element berbentuk persegi (RECT)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, k_size)
    # Menerapkan operasi opening
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)

    axs[idx + 1].imshow(opening, cmap="gray")
    axs[idx + 1].set_title(f"Opening: {k_size[0]}x{k_size[1]}")

  for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

  plt.tight_layout()
  plt.show()


if __name__ == "__main__":
  opening_process()