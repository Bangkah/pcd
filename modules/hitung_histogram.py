from PIL import Image
import matplotlib.pyplot as plt

# Membuka gambar dan mengubahnya menjadi grayscale
gambar = Image.open("assets/image.png").convert("L")

# Menghitung histogram
histogram = gambar.histogram()

# Menampilkan histogram
plt.plot(histogram)
plt.title("Histogram Grayscale")
plt.xlabel("Nilai Grayscale")
plt.ylabel("Jumlah Piksel")
plt.show()