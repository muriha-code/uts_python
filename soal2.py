# Program: Menentukan Kategori Setoran Koperasi

# minta input dari user
setoran1 = int(input("Masukkan setoran pertama: "))
setoran2 = int(input("Masukkan setoran kedua: "))
setoran3 = int(input("Masukkan setoran ketiga: "))

# cek validitas input
if setoran1 <= 0 or setoran2 <= 0 or setoran3 <= 0:
    print("Input tidak valid")
else:
    # hitung total setoran
    total = setoran1 + setoran2 + setoran3
    print("Total setoran:", total)

    # tentukan kategori berdasarkan total
    if total < 300000:
        print("Kategori: rendah")
    elif total < 600000:
        print("Kategori: sedang")
    else:
        print("Kategori: tinggi")
