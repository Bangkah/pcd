from modules.closing_ops import closing_process
from modules.dilation_ops import dilation_process
from modules.edge_detection import edge_detection_process
from modules.gaussian_lowpass import gaussian_lowpass_process
from modules.gradient_ops import gradient_process
from modules.ideal_highpass import ideal_highpass_process
from modules.image_blur import blur_image_process
from modules.image_inverse import inverse_image_process
from modules.image_negative import negative_image_process
from modules.image_normalization import normalize_image_process
from modules.image_resizing import resize_image_process
from modules.image_rotation import rotate_image_process
from modules.image_shearing import shear_image_process
from modules.image_translation import translate_image_process
from modules.morphological_hats import hats_process
from modules.morphological_ops import erosion_process
from modules.opening_ops import opening_process
from modules.power_law_transformation import power_law_process


def tampilkan_menu():
  print("\n=== PROGRAM MENU PENGOLAHAN CITRA DIGITAL ===")
  print("1. Image Resizing (Zoom & Scale)")
  print("2. Image Rotation")
  print("3. Image Translation")
  print("4. Image Shearing")
  print("5. Image Normalization")
  print("6. Edge Detection (Prewitt, Sobel, Canny)")
  print("7. Image Blurring (Gaussian)")
  print("8. Morphological Erosion")
  print("9. Morphological Dilation")
  print("10. Morphological Opening")
  print("11. Morphological Closing")
  print("12. Morphological Gradient")
  print("13. Top Hat & Black Hat Operations")
  print("14. Image Intensity Addition (+50)")
  print("15. Image Inversion / Negative (Terang <-> Gelap)")
  print("16. Power-Law (Gamma) Transformation")
  print("17. Gaussian Lowpass Filter (GLPF)")
  print("18. Ideal Highpass Filter (IHPF)")
  print("19. Keluar")


def main():
  while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-19): ")

    if pilihan == "1":
      resize_image_process()
    elif pilihan == "2":
      rotate_image_process()
    elif pilihan == "3":
      translate_image_process()
    elif pilihan == "4":
      shear_image_process()
    elif pilihan == "5":
      normalize_image_process()
    elif pilihan == "6":
      edge_detection_process()
    elif pilihan == "7":
      blur_image_process()
    elif pilihan == "8":
      erosion_process()
    elif pilihan == "9":
      dilation_process()
    elif pilihan == "10":
      opening_process()
    elif pilihan == "11":
      closing_process()
    elif pilihan == "12":
      gradient_process()
    elif pilihan == "13":
      hats_process()
    elif pilihan == "14":
      inverse_image_process()
    elif pilihan == "15":
      negative_image_process()
    elif pilihan == "16":
      power_law_process()
    elif pilihan == "17":
      gaussian_lowpass_process()
    elif pilihan == "18":
      ideal_highpass_process()
    elif pilihan == "19":
      print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
      break
    else:
      print("Pilihan tidak valid, silakan masukkan angka 1 sampai 19.")


if __name__ == "__main__":
  main()