def kalkulator():
    while True:
        print("1. Penjumlahan (+)")
        print("2. Pengurangan (-)")
        print("3. Perkalian (*)")
        print("4. Pembagian (/)")
        print("5. Pangkat (^)")
        print("6. Faktorial (!)")
        print("7. Keluar")
        
        pilihan = input("\nPilih menu (1-7): ")
        
        if pilihan == '7':
            print("Terima kasih!")
            break
            
        if pilihan in ('1', '2', '3', '4', '5'):
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
            
            if pilihan == '1':
                print(f"Hasil: {a + b}")
            elif pilihan == '2':
                print(f"Hasil: {a - b}")
            elif pilihan == '3':
                print(f"Hasil: {a * b}")
            elif pilihan == '4':
                if b == 0:
                    print("Error: Pembagi tidak boleh nol.")
                else:
                    print(f"Hasil: {a / b}")
            elif pilihan == '5':
                print(f"Hasil: {a ** b}")
                
        elif pilihan == '6':
            n = int(input("Masukkan angka untuk faktorial: "))
            if n < 0:
                print("Error: Faktorial tidak bisa untuk angka negatif.")
            else:
                hasil = 1
                for i in range(1, n + 1):
                    hasil *= i
                print(f"Hasil: {n}! = {hasil}")
        else:
            print("Pilihan tidak valid.")

kalkulator()