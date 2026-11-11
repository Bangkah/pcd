import matplotlib.pyplot as plt
from PIL import Image


def hitung_histogram_process():
    image_path = "assests/image.png"
    try:
        gambar = Image.open(image_path).convert("L")
    except FileNotFoundError:
        print(f"Gagal memuat gambar '{image_path}'.")
        return

    histogram = gambar.histogram()
    plt.plot(histogram)
    plt.title("Histogram Grayscale")
    plt.xlabel("Nilai Grayscale")
    plt.ylabel("Jumlah Piksel")
    plt.show()


if __name__ == "__main__":
    hitung_histogram_process()