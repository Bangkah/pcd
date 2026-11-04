import cv2
import numpy as np
import matplotlib.pyplot as plt

def simple_thresholding():
    image_path = "C:\\Users\\atha\\Documents\\PCD\\assests\\image.jpg"
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Gagal memuat gambar dari path: {image_path}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    print(f"\n--- SIMPLE THRESHOLDING ---")
    print(f"Nilai threshold yang dipakai: {ret}")
    
    return binary

def canny_edge_detection():
    image_path = "C:\\Users\\atha\\Documents\\PCD\\assests\\image.jpg"
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Gagal memuat gambar dari path: {image_path}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    
    print(f"\n--- CANNY EDGE DETECTION ---")
    print("Tinggal tunggu hasil edge-nya keluar!")
    
    return edges

if __name__ == "__main__":
    print("=== MEMULAI PROSES SEGMENTASI ===")
    
    # PERBAIKANNYA: define image dulu
    image_path = "C:\\Users\\atha\\Documents\\PCD\\assests\\image.jpg"
    image = cv2.imread(image_path)
    if image is None:
        print("Gagal memuat gambar!")
    else:
        # Baru panggil fungsi-fungsinya
        binary = simple_thresholding()
        edges = canny_edge_detection()
        
        # Tampilkan hasilnya
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        fig, axs = plt.subplots(1, 3, figsize=(17, 5))
        
        axs[0].imshow(image_rgb)
        axs[0].set_title("Original Image")
        axs[0].axis("off")
        
        axs[1].imshow(binary, cmap="gray")
        axs[1].set_title("Simple Thresholding")
        axs[1].axis("off")
        
        axs[2].imshow(edges, cmap="gray")
        axs[2].set_title("Canny Edge Detection")
        axs[2].axis("off")
        
        plt.tight_layout()
        plt.show()
        
        print("\nSelesai! 🎉")
