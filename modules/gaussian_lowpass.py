import cv2
import matplotlib.pyplot as plt
import numpy as np


def gaussian_lowpass_process():
  # Memuat gambar dari folder assets dan ubah ke grayscale
  image = cv2.imread("assests/mobil.png")
  if image is None:
    print(
        "Gagal memuat gambar dari folder assets. Periksa kembali nama atau path"
        " file."
    )
    return

  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  print("\n--- PENGATURAN GAUSSIAN LOWPASS FILTER (GLPF) ---")
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
  # Menggeser komponen frekuensi rendah ke tengah
  f_shift = np.fft.fftshift(f_transform)

  # 2. Inisialisasi variabel untuk fungsi konvolusi (Filter GLPF)
  rows, cols = gray.shape
  center_row, center_col = rows / 2, cols / 2

  # Membuat meshgrid untuk jarak Euclidean dari pusat
  u = np.arange(0, rows)
  v = np.arange(0, cols)
  U, V = np.meshgrid(v, u)
  D_sq = (U - center_col) ** 2 + (V - center_row) ** 2

  # Rumus GLPF: H(u,v) = exp( - D^2 / (2 * D_0^2) )
  # Sesuai teks: t1 = 2 * d_0, maka penyebutnya adalah 2 * (d_0 ** 2)
  H = np.exp(-D_sq / (2 * (d_0**2)))

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

  # Menampilkan gambar asli (grayscale) dan hasil filter GLPF
  fig, axs = plt.subplots(1, 2, figsize=(7, 4))
  axs[0].imshow(gray, cmap="gray")
  axs[0].set_title("Original Grayscale")

  axs[1].imshow(img_back, cmap="gray")
  axs[1].set_title(f"Gaussian Lowpass Filter ($D_0$ = {d_0})")

  for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

  plt.tight_layout()
  plt.show()


if __name__ == "__main__":
  gaussian_lowpass_process()