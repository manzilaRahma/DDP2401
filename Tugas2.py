# Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
def genap_ganjil(bilangan):
    hitung = bilangan % 2 == 0 # Menentukan bilangan ganjil atau genap
    return hitung # Mengembalikan nilai hitung

angka = 4 # Mendefinisikan bilangan
hasil = genap_ganjil(angka) # Memanggil fungsi
print(f"bilangan {angka} bernilai {hasil}")

angka2 = 7
hasil = genap_ganjil(angka2)
print(f"bilangan {angka2} bernilai {hasil}")