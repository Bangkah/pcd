import cv2
import matplotlib.pyplot as plt


def hats_process():
  image = cv2.imread("assets/mobil.png")
  if image is None:
    print(
        "Gagal memuat gambar 'assets/mobil.png'. Periksa kembali nama atau path file."
    )
    return

  # Konversi ke grayscale
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  print("\n--- PENGATURAN TOP HAT & BLACK HAT ---")
  print("Menerapkan operasi Top Hat dan Black Hat dengan kernel persegi panjang...")

  # Membuat kernel persegi panjang dengan ukuran 13x5 (cocok untuk mendeteksi area plat nomor)
  rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))

  # Menerapkan Black Hat (menemukan area gelap pada latar belakang terang)
  blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)

  # Menerapkan Top Hat / White Hat (menemukan area terang pada latar belakang gelap)
  tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)

  # Menampilkan hasil menggunakan Matplotlib (1 baris, 3 kolom: Asli, Blackhat, Tophat)
  fig, axs = plt.subplots(1, 3, figsize=(12, 4))

  axs[0].imshow(gray, cmap="gray")
  axs[0].set_title("Original Gray")

  axs[1].imshow(blackhat, cmap="gray")
  axs[1].set_title("Black Hat (Dark on Light)")

  axs[2].imshow(tophat, cmap="gray")
  axs[2].set_title("Top Hat / White Hat (Light on Dark)")

  for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

  plt.tight_layout()
  plt.show()


if __name__ == "__main__":
  hats_process()