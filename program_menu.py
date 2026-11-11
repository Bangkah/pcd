from modules.adaptive_threshold import adaptive_threshold_process
from modules.closing_ops import closing_process
from modules.dilation_ops import dilation_process
from modules.edge_detection import edge_detection_process
from modules.erosion_ops import erosion_process
from modules.gaussian_lowpass import gaussian_lowpass_process
from modules.gradient_ops import gradient_process
from modules.hitung_histogram import hitung_histogram_process
from modules.ideal_highpass import ideal_highpass_process
from modules.image_blur import blur_image_process
from modules.image_blurring import apply_blurring_process
from modules.image_inverse import inverse_image_process
from modules.image_morphology import morphology_image_process
from modules.image_negative import negative_image_process
from modules.image_normalization import normalize_image_process
from modules.image_resizing import resize_image_process
from modules.image_rotation import rotate_image_process
from modules.image_shearing import shear_image_process
from modules.image_translation import translate_image_process
from modules.morphological_hats import hats_process
from modules.opening_ops import opening_process
from modules.otsu_thresholding import otsu_threshold_process
from modules.power_law_transformation import power_law_process
from modules.simple_tresholding import simple_thresholding


def tampilkan_menu():
    print("\n=== PROGRAM MENU PENGOLAHAN CITRA DIGITAL ===")
    print("1. Image Resizing (Zoom & Scale)")
    print("2. Image Rotation")
    print("3. Image Translation")
    print("4. Image Shearing")
    print("5. Image Normalization")
    print("6. Edge Detection (Prewitt, Sobel, Canny)")
    print("7. Gaussian Blur")
    print("8. Image Blurring (Gaussian, Average, Median)")
    print("9. Morphological Erosion")
    print("10. Morphological Dilation")
    print("11. Morphological Opening")
    print("12. Morphological Closing")
    print("13. Morphological Gradient")
    print("14. Top Hat & Black Hat Operations")
    print("15. Morphological Operations (Gabungan)")
    print("16. Image Inversion")
    print("17. Image Negative")
    print("18. Power-Law (Gamma) Transformation")
    print("19. Gaussian Lowpass Filter")
    print("20. Ideal Highpass Filter")
    print("21. Otsu Thresholding")
    print("22. Adaptive Thresholding")
    print("23. Simple Thresholding")
    print("24. Hitung & Tampilkan Histogram")
    print("25. Keluar")


def main():
    actions = {
        "1": resize_image_process,
        "2": rotate_image_process,
        "3": translate_image_process,
        "4": shear_image_process,
        "5": normalize_image_process,
        "6": edge_detection_process,
        "7": blur_image_process,
        "8": apply_blurring_process,
        "9": erosion_process,
        "10": dilation_process,
        "11": opening_process,
        "12": closing_process,
        "13": gradient_process,
        "14": hats_process,
        "15": morphology_image_process,
        "16": inverse_image_process,
        "17": negative_image_process,
        "18": power_law_process,
        "19": gaussian_lowpass_process,
        "20": ideal_highpass_process,
        "21": otsu_threshold_process,
        "22": adaptive_threshold_process,
        "23": simple_thresholding,
        "24": hitung_histogram_process,
    }

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-25): ").strip()

        if pilihan == "25":
            print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
            break

        action = actions.get(pilihan)
        if action is None:
            print("Pilihan tidak valid, silakan masukkan angka 1 sampai 25.")
            continue

        action()


if __name__ == "__main__":
    main()
