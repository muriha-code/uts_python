# Program: Menghitung Ongkir RapidSend

def hitung_ongkir(berat_kg, kota, asuransi=False):
    """
    Menghitung ongkir berdasarkan kota, berat, dan asuransi (opsional).
    """
    tarif_dasar = {
        "Jakarta": 10000,
        "Bandung": 12000,
        "Surabaya": 15000,
        "Yogyakarta": 13000
    }

    # cek apakah kota ada di dalam tarif_dasar
    if kota not in tarif_dasar:
        print("Kota tidak ditemukan")
        return None

    total = tarif_dasar[kota] + 2000 * berat_kg

    # kalau ada asuransi, tambah 3000
    if asuransi == True:
        total = total + 3000

    return total


# --- Contoh pemanggilan fungsi ---
ongkir1 = hitung_ongkir(2, "Jakarta")
print("Ongkir 1:", ongkir1)

ongkir2 = hitung_ongkir(3, "Surabaya", True)
print("Ongkir 2:", ongkir2)
