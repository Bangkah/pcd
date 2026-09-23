import os
import cv2
import matplotlib.pyplot as plt

def apply_blurring_process():
    """
    Fungsi proses blurring yang terintegrasi dengan menu interaktif.
    """
    image_path = input("Masukkan nama/path file gambar (contoh: gambar.png): ").strip()
    if not image_path:
        image_path = 'assets/gambar.png' 

    if not os.path.exists(image_path):
        print(f"[ERROR] File gambar '{image_path}' tidak ditemukan!")
        return

    image = cv2.imread(image_path)
    if image is None:
        print(f"[ERROR] Gagal membaca gambar dari '{image_path}'.")
        return

    print("\nPilih Jenis Blur:")
    print("1. Gaussian Blur")
    print("2. Average Blur")
    print("3. Median Blur")
    blur_choice = input("Masukkan pilihan (1-3): ").strip()

    try:
        k_val = int(input("Masukkan ukuran kernel (angka ganjil, misal 3, 5, 7): ").strip())
        if k_val <= 0 or k_val % 2 == 0:
            print("[INFO] Ukuran kernel harus ganjil positif. Otomatis disesuaikan ke 3.")
            k_val = 3
    except ValueError:
        print("[INFO] Input tidak valid, menggunakan ukuran kernel default 3.")
        k_val = 3

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    if blur_choice == '1':
        blurred = cv2.GaussianBlur(image, (k_val, k_val), 0)
        title_suffix = f"Gaussian Blur ({k_val}x{k_val})"
    elif blur_choice == '2':
        blurred = cv2.blur(image, (k_val, k_val))
        title_suffix = f"Average Blur ({k_val}x{k_val})"
    elif blur_choice == '3':
        blurred = cv2.medianBlur(image, k_val)
        title_suffix = f"Median Blur ({k_val}x{k_val})"
    else:
        print("[WARNING] Pilihan tidak valid, menggunakan Gaussian Blur sebagai default.")
        blurred = cv2.GaussianBlur(image, (k_val, k_val), 0)
        title_suffix = f"Gaussian Blur ({k_val}x{k_val})"

    blurred_rgb = cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB)

    # Menampilkan hasil
    fig, axs = plt.subplots(1, 2, figsize=(8, 4))
    axs[0].imshow(image_rgb)
    axs[0].set_title('Original Image')
    
    axs[1].imshow(blurred_rgb)
    axs[1].set_title(title_suffix)

    for ax in axs:
        ax.set_xticks([])
        ax.set_yticks([])

    plt.tight_layout()
    plt.show()