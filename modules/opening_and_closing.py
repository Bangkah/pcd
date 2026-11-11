import os
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

NAMA_FILE = "assests/gambar.png"
THRESHOLD = 128         
UKURAN_SE = 3         
ITERASI = 1           


# ============================================================
# BAGIAN 1: FUNGSI PERSIAPAN CITRA & OPERASI MORFOLOGI
# ============================================================

def load_dan_binarisasi(path=NAMA_FILE, threshold=THRESHOLD):
    """Membuka gambar grayscale lalu mengubahnya menjadi citra biner (0 dan 255)."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"File '{path}' tidak ditemukan!")

    im_gray = np.array(Image.open(path).convert("L"), dtype=np.uint8)
    _, im_binary = cv2.threshold(im_gray, threshold, 255, cv2.THRESH_BINARY)
    return im_gray, im_binary


def buat_kernel(ukuran=UKURAN_SE):
    """Membuat Structuring Element (kernel) persegi berukuran ganjil."""
    if ukuran % 2 == 0:
        ukuran += 1
    return np.ones((ukuran, ukuran), np.uint8)


def operasi_dilasi(im_binary, kernel, iterasi=1):
    """1. Dilasi (A + B): Mempertebal objek putih."""
    return cv2.dilate(im_binary, kernel, iterations=iterasi)


def operasi_erosi(im_binary, kernel, iterasi=1):
    """2. Erosi (A - B): Mengikis / menipiskan objek putih."""
    return cv2.erode(im_binary, kernel, iterations=iterasi)


def operasi_opening(im_binary, kernel, iterasi=1):
    """3. Opening : Erosi lalu Dilasi (menghilangkan noise putih kecil)."""
    return cv2.morphologyEx(im_binary, cv2.MORPH_OPEN, kernel, iterations=iterasi)


def operasi_closing(im_binary, kernel, iterasi=1):
    """4. Closing : Dilasi lalu Erosi (menutup lubang hitam kecil)."""
    return cv2.morphologyEx(im_binary, cv2.MORPH_CLOSE, kernel, iterations=iterasi)


# ============================================================
# BAGIAN 2: FUNGSI VISUALISASI
# ============================================================
    plt.subplots_adjust(bottom=0.22, wspace=0.08)

    axes[0].imshow(im_gray, cmap="gray", vmin=0, vmax=255)
    axes[0].axis("off")
    axes[0].text(0.5, -0.08, "(a) Citra Grayscale Asli",
                 transform=axes[0].transAxes, ha="center", va="top", fontsize=11)

    axes[1].imshow(im_binary, cmap="gray", vmin=0, vmax=255)
    axes[1].axis("off")
    axes[1].text(0.5, -0.08, f"(b) Citra Biner (T = {THRESHOLD})",
                 transform=axes[1].transAxes, ha="center", va="top", fontsize=11)

    axes[2].imshow(im_hasil, cmap="gray", vmin=0, vmax=255)
    axes[2].axis("off")
    axes[2].text(0.5, -0.08, judul_hasil,
                 transform=axes[2].transAxes, ha="center", va="top", fontsize=11)

    fig.text(0.5, 0.02, rumus_fig, ha="center", fontsize=10)
    plt.savefig(nama_simpan, dpi=150, bbox_inches="tight")
    print(f"✓ Grafik disimpan sebagai: {nama_simpan}")
    plt.show()


def tampilkan_semua(im_gray, im_binary, out_dilasi, out_erosi, out_opening, out_closing, ukuran_se, iterasi):
    """Menampilkan perbandingan ke-4 operasi morfologi sekaligus (layout 2x3)."""
    fig, axes = plt.subplots(2, 3, figsize=(14, 9))
    plt.subplots_adjust(hspace=0.25, wspace=0.08)

    panel = [
        (im_gray, "(a) Citra Grayscale Asli"),
        (im_binary, f"(b) Citra Biner (T = {THRESHOLD})"),
        (out_dilasi, f"(c) 1. Dilasi ({ukuran_se}x{ukuran_se}, iter={iterasi})"),
        (out_erosi, f"(d) 2. Erosi ({ukuran_se}x{ukuran_se}, iter={iterasi})"),
        (out_opening, f"(e) 3. Opening ({ukuran_se}x{ukuran_se}, iter={iterasi})"),
        (out_closing, f"(f) 4. Closing ({ukuran_se}x{ukuran_se}, iter={iterasi})"),
    ]

    for ax, (img, judul) in zip(axes.flat, panel):
        ax.imshow(img, cmap="gray", vmin=0, vmax=255)
        ax.axis("off")
        ax.text(0.5, -0.06, judul, transform=ax.transAxes,
                ha="center", va="top", fontsize=11)

    plt.savefig("figure_morfologi_semua.png", dpi=150, bbox_inches="tight")
    print("✓ Grafik gabungan disimpan sebagai: figure_morfologi_semua.png")
    plt.show()


# ============================================================
# BAGIAN 3: MENU & INPUT USER
# ============================================================

def menu():
    print("\n" + "=" * 55)
    print("   PROGRAM OPERASI MORFOLOGI CITRA BINER")
    print(f"   File: {NAMA_FILE} | Threshold: {THRESHOLD}")
    print("=" * 55)
    print(" 1. Dilasi   (Dilation) ")
    print(" 2. Erosi    (Erosion)  ")
    print(" 3. Opening            ")
    print(" 4. Closing            ")
    print(" 5. Tampilkan Semua (1-4 sekaligus)")
    print(" 0. Keluar")
    print("=" * 55)


def input_parameter():
    """Meminta input ukuran kernel dan jumlah iterasi (bisa tekan Enter untuk default)."""
    teks_se = input(f"Ukuran kernel ganjil [default {UKURAN_SE}]: ").strip()
    ukuran_se = int(teks_se) if teks_se.isdigit() and int(teks_se) >= 3 else UKURAN_SE
    if ukuran_se % 2 == 0:
        ukuran_se += 1

    teks_iter = input(f"Jumlah iterasi [default {ITERASI}]: ").strip()
    iterasi = int(teks_iter) if teks_iter.isdigit() and int(teks_iter) >= 1 else ITERASI

    return ukuran_se, iterasi


# ============================================================
# BAGIAN 4: PROGRAM UTAMA
# ============================================================

def main():
    try:
        im_gray, im_binary = load_dan_binarisasi(NAMA_FILE, THRESHOLD)
    except FileNotFoundError as e:
        print(f"X {e}")
        return

    print(f"\n✓ Gambar dimuat: {im_gray.shape}, piksel putih awal = {np.count_nonzero(im_binary)}")

    while True:
        menu()
        pilihan = input("Pilih menu (0-5): ").strip()

        if pilihan == "0":
            print("\nTerima kasih! Program selesai.")
            break

        if pilihan not in ["1", "2", "3", "4", "5"]:
            print(" Pilihan tidak valid. Masukkan angka 0-5.")
            continue

        ukuran_se, iterasi = input_parameter()
        kernel = buat_kernel(ukuran_se)

        # ============ 1. DILASI ============
        if pilihan == "1":
            print("\n--- 1. BINARY DILATION (DILASI) ---")
            hasil = operasi_dilasi(im_binary, kernel, iterasi)
            Image.fromarray(hasil).save("output_dilasi.png")
            print(f"✓ Piksel putih: {np.count_nonzero(im_binary)} -> {np.count_nonzero(hasil)}")
            print("✓ Disimpan: output_dilasi.png")
            tampilkan_3panel(
                im_gray, im_binary, hasil,
                f"(c) Hasil Dilasi ({ukuran_se}x{ukuran_se}, iter={iterasi})",
                r"$\bf{DILASI:}$ $A \oplus B$ menggunakan $\tt{cv2.dilate()}$",
                "figure_dilasi.png"
            )

        # ============ 2. EROSI ============
        elif pilihan == "2":
            print("\n--- 2. BINARY EROSION (EROSI) ---")
            hasil = operasi_erosi(im_binary, kernel, iterasi)
            Image.fromarray(hasil).save("output_erosi.png")
            print(f"✓ Piksel putih: {np.count_nonzero(im_binary)} -> {np.count_nonzero(hasil)}")
            print("✓ Disimpan: output_erosi.png")
            tampilkan_3panel(
                im_gray, im_binary, hasil,
                f"(c) Hasil Erosi ({ukuran_se}x{ukuran_se}, iter={iterasi})",
                r"$\bf{EROSI:}$ $A \ominus B$ menggunakan $\tt{cv2.erode()}$",
                "figure_erosi.png"
            )

        # ============ 3. OPENING ============
        elif pilihan == "3":
            print("\n--- 3. BINARY OPENING ---")
            hasil = operasi_opening(im_binary, kernel, iterasi)
            Image.fromarray(hasil).save("output_opening.png")
            print(f"✓ Piksel putih: {np.count_nonzero(im_binary)} -> {np.count_nonzero(hasil)}")
            print("✓ Disimpan: output_opening.png")
            tampilkan_3panel(
                im_gray, im_binary, hasil,
                f"(c) Hasil Opening ({ukuran_se}x{ukuran_se}, iter={iterasi})",
                r"$\bf{OPENING:}$ $A \circ B = (A \ominus B) \oplus B$ menggunakan $\tt{cv2.MORPH\_OPEN}$",
                "figure_opening.png"
            )

        # ============ 4. CLOSING ============
        elif pilihan == "4":
            print("\n--- 4. BINARY CLOSING ---")
            hasil = operasi_closing(im_binary, kernel, iterasi)
            Image.fromarray(hasil).save("output_closing.png")
            print(f"✓ Piksel putih: {np.count_nonzero(im_binary)} -> {np.count_nonzero(hasil)}")
            print("✓ Disimpan: output_closing.png")
            tampilkan_3panel(
                im_gray, im_binary, hasil,
                f"(c) Hasil Closing ({ukuran_se}x{ukuran_se}, iter={iterasi})",
                r"$\bf{CLOSING:}$ $A \bullet B = (A \oplus B) \ominus B$ menggunakan $\tt{cv2.MORPH\_CLOSE}$",
                "figure_closing.png"
            )

        # ============ 5. SEMUA SEKALIGUS ============
        elif pilihan == "5":
            print("\n--- 5. SEMUA OPERASI MORFOLOGI SEKALIGUS ---")
            out_dil = operasi_dilasi(im_binary, kernel, iterasi)
            out_ero = operasi_erosi(im_binary, kernel, iterasi)
            out_opn = operasi_opening(im_binary, kernel, iterasi)
            out_cls = operasi_closing(im_binary, kernel, iterasi)

            Image.fromarray(out_dil).save("output_dilasi.png")
            Image.fromarray(out_ero).save("output_erosi.png")
            Image.fromarray(out_opn).save("output_opening.png")
            Image.fromarray(out_cls).save("output_closing.png")
            print("✓ Ke-4 gambar hasil berhasil disimpan.")

            tampilkan_semua(
                im_gray, im_binary,
                out_dil, out_ero, out_opn, out_cls,
                ukuran_se, iterasi
            )


if __name__ == "__main__":
    main()