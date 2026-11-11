import os
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def dilation_process():
    NAMA_FILE = "assets/image.png" # Sesuaikan path gambar Anda
    THRESHOLD = 128
    
    print("\n--- 1. BINARY DILATION (DILASI) ---")
    if not os.path.exists(NAMA_FILE):
        print(f"X File '{NAMA_FILE}' tidak ditemukan! Cek folder assets.")
        return

    # Load & Binarisasi
    im_gray = np.array(Image.open(NAMA_FILE).convert("L"), dtype=np.uint8)
    _, im_binary = cv2.threshold(im_gray, THRESHOLD, 255, cv2.THRESH_BINARY)

    # Input User
    teks_se = input("Ukuran kernel ganjil [default 3]: ").strip()
    ukuran_se = int(teks_se) if teks_se.isdigit() and int(teks_se) >= 3 else 3
    if ukuran_se % 2 == 0: ukuran_se += 1

    teks_iter = input("Jumlah iterasi [default 1]: ").strip()
    iterasi = int(teks_iter) if teks_iter.isdigit() and int(teks_iter) >= 1 else 1

    # Proses Dilasi
    kernel = np.ones((ukuran_se, ukuran_se), np.uint8)
    hasil = cv2.dilate(im_binary, kernel, iterations=iterasi)

    # Visualisasi 3 Panel
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.5))
    plt.subplots_adjust(bottom=0.22, wspace=0.08)

    axes[0].imshow(im_gray, cmap="gray", vmin=0, vmax=255)
    axes[0].axis("off")
    axes[0].set_title("(a) Citra Grayscale Asli", fontsize=11)

    axes[1].imshow(im_binary, cmap="gray", vmin=0, vmax=255)
    axes[1].axis("off")
    axes[1].set_title(f"(b) Citra Biner (T = {THRESHOLD})", fontsize=11)

    axes[2].imshow(hasil, cmap="gray", vmin=0, vmax=255)
    axes[2].axis("off")
    axes[2].set_title(f"(c) Hasil Dilasi ({ukuran_se}x{ukuran_se}, iter={iterasi})", fontsize=11)

    fig.text(0.5, 0.02, r"$\bf{DILASI:}$ $A \oplus B$ menggunakan $\tt{cv2.dilate()}$", ha="center", fontsize=11)
    plt.show()

if __name__ == "__main__":
    dilation_process()