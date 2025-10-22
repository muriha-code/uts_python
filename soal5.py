# Program: Rekap Kehadiran UTS

import os
import csv
import json
import logging

# setup logging sederhana
logging.basicConfig(
    filename='log_presensi.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Program dimulai")

# 1. buat folder data
folder = "data"
if not os.path.exists(folder):
    os.makedirs(folder)

# nama file csv dan json
file_csv = os.path.join(folder, "presensi.csv")
file_json = os.path.join(folder, "ringkasan.json")

# 2. tulis data CSV
try:
    with open(file_csv, mode="w", newline="") as file:
        tulis = csv.writer(file)
        tulis.writerow(["nim", "nama", "hadir_uts"])
        tulis.writerow(["2310001", "Alya", 1])
        tulis.writerow(["2310002", "Rafi", 0])
        tulis.writerow(["2310003", "Dinda", 1])
    logging.info("Berhasil menulis file CSV")
except Exception as e:
    print("Gagal menulis file CSV:", e)
    logging.error("Gagal menulis CSV: " + str(e))

# 3. baca CSV dan hitung ringkasan
try:
    with open(file_csv, mode="r") as file:
        baca = csv.DictReader(file)
        total = 0
        hadir = 0
        for baris in baca:
            total += 1
            if baris["hadir_uts"] == "1":
                hadir += 1

        # hitung persentase hadir
        if total > 0:
            persen = (hadir / total) * 100
        else:
            persen = 0

        ringkasan = {
            "total_mahasiswa": total,
            "jumlah_hadir": hadir,
            "persentase_hadir": persen
        }

        # simpan ke JSON
        with open(file_json, mode="w") as fjson:
            json.dump(ringkasan, fjson, indent=4)

        logging.info("Berhasil membuat file JSON ringkasan")

except Exception as e:
    print("Gagal membaca/menulis file:", e)
    logging.error("Terjadi error saat baca/tulis: " + str(e))

logging.info("Program selesai")
