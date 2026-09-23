def penjumlahan(a, b):
    return a + b

def perkalian(a, b):
    return a * b    

def pembagian(a, b):
    if b == 0:
        raise ValueError("Pembagi tidak boleh nol.")
    return a / b

def pengurangan(a, b):
    return a - b

def pangkat(a, b):
    return a ** b   

# Mengambil input dari pengguna
a = float(input("Masukkan angka pertama (a): "))
b = float(input("Masukkan angka kedua (b): "))

print("\nHasil Perhitungan:")
print(f"Penjumlahan ({a} + {b}) = {penjumlahan(a, b)}")
print(f"Pengurangan ({a} - {b}) = {pengurangan(a, b)}")
print(f"Perkalian ({a} * {b}) = {perkalian(a, b)}")

try:
    print(f"Pembagian ({a} / {b}) = {pembagian(a, b)}")
except ValueError as e:
    print(f"Pembagian: {e}")

print(f"Pangkat ({a} ** {b}) = {pangkat(a, b)}")