# Program: Jadwal Kuliah Berdasarkan Hari

def jadwal_hari(hari):
    """
    Menampilkan jadwal kuliah berdasarkan hari yang dicari.
    """
    jadwal = [
        {"hari": "Senin", "matkul": "Algoritma", "jam": "08.00"},
        {"hari": "Selasa", "matkul": "Basis Data", "jam": "09.00"},
        {"hari": "Rabu", "matkul": "Pemrograman Python", "jam": "10.00"},
        {"hari": "Kamis", "matkul": "Sistem Operasi", "jam": "13.00"},
        {"hari": "Jumat", "matkul": "Jaringan Komputer", "jam": "08.00"}
    ]

    # cari data jadwal berdasarkan hari
    ketemu = False
    for data in jadwal:
        if data["hari"].lower() == hari.lower():
            print("Mata kuliah:", data["matkul"])
            print("Jam:", data["jam"])
            ketemu = True
            break

    if not ketemu:
        print("Jadwal tidak ditemukan untuk hari tersebut.")


# --- Contoh pemanggilan fungsi ---
jadwal_hari("Rabu")
jadwal_hari("Minggu")
