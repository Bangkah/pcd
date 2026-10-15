import cv2
import matplotlib.pyplot as plt
import numpy as np


def ideal_highpass_process():
  # Memuat gambar dari folder assets dan ubah ke grayscale
  image = cv2.imread("assests/mobil.png")
  if image is None:
    print(
        "Gagal memuat gambar dari folder assets. Periksa kembali nama atau path"
        " file."
    )
    return

  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  print("\n--- PENGATURAN IDEAL HIGHPASS FILTER (IHPF) ---")
  try:
    d_0 = float(
        input(
            "Masukkan nilai cut-off frequency / radius (misal: 30 atau 50): "
        )
    )
  except ValueError:
    print("Input harus berupa angka.")
    return

  # 1. Melakukan 2D Fast Fourier Transform (FFT)
  f_transform = np.fft.fft2(gray)
  f_shift = np.fft.fftshift(f_transform)

  # 2. Inisialisasi variabel untuk fungsi konvolusi (Filter IHPF)
  rows, cols = gray.shape
  center_row, center_col = rows / 2, cols / 2

  # Membuat meshgrid untuk jarak Euclidean dari pusat
  u = np.arange(0, rows)
  v = np.arange(0, cols)
  U, V = np.meshgrid(v, u)
  D = np.sqrt((U - center_col) ** 2 + (V - center_row) ** 2)

  # Rumus IHPF: H(u,v) = 0 jika D <= d_0, dan 1 jika sebaliknya
  H = np.ones((rows, cols), dtype=np.float32)
  H[D <= d_0] = 0.0

  # 3. Melakukan perkalian konvolusi di domain frekuensi
  filtered_f_shift = f_shift * H

  # 4. Menggeser kembali frekuensi dan melakukan Inverse FFT (IFFT)
  f_ishift = np.fft.ifftshift(filtered_f_shift)
  img_back = np.fft.ifft2(f_ishift)
  img_back = np.abs(img_back)

  # Normalisasi nilai ke rentang [0, 255]
  img_back = cv2.normalize(
      img_back, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX
  )
  img_back = np.array(img_back, dtype=np.uint8)

  # Menampilkan gambar asli (grayscale) dan hasil filter IHPF
  fig, axs = plt.subplots(1, 2, figsize=(7, 4))
  axs[0].imshow(gray, cmap="gray")
  axs[0].set_title("Original Grayscale")

  axs[1].imshow(img_back, cmap="gray")
  axs[1].set_title(f"Ideal Highpass Filter ($D_0$ = {d_0})")

  for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

  plt.tight_layout()
  plt.show()


if __name__ == "__main__":
  ideal_highpass_process()