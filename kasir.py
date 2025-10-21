# 1. Daftar produk kita
# Format: "KODE": ["NAMA BARANG", HARGA]
PRODUK = {
    "A1": ["Buku Tulis", 5000],
    "A2": ["Pensil", 3000],
    "A3": ["Penghapus", 2000],
    "B1": ["Air Mineral", 3000],
    "B2": ["Roti Sobek", 7000],
}

# 2. Fungsi untuk menampilkan produk
def tampilkan_produk():
    """Menampilkan semua produk yang ada."""
    print("===== DAFTAR PRODUK =====")
    for kode, data in PRODUK.items():
        # data[0] adalah nama, data[1] adalah harga
        print(f"Kode: {kode} | {data[0]} | Rp {data[1]}")
    print("=========================")
    print("Ketik 'selesai' jika sudah selesai.\n")

# 3. Fungsi utama program
def jalankan_kasir():
    """Fungsi utama untuk menjalankan kasir."""
    
    # Keranjang belanja untuk menyimpan (kode_produk: jumlah)
    keranjang = {}
    total_belanja = 0

    print("--- SELAMAT DATANG DI KASIR SEDERHANA ---")

    while True:
        # Tampilkan produk setiap kali akan input
        tampilkan_produk()
        
        # Minta input kode dari kasir
        kode = input("Masukkan Kode Produk: ").strip().upper()

        # Cek jika kasir ingin selesai
        if kode == 'SELESAI':
            break # Keluar dari loop input barang

        # Cek apakah kodenya ada di daftar produk
        if kode not in PRODUK:
            print("Error: Kode produk tidak ditemukan. Coba lagi.\n")
            continue # Ulangi loop

        # Jika kode ada, minta jumlahnya
        try:
            jumlah = int(input(f"Masukkan jumlah {PRODUK[kode][0]}: "))
            if jumlah <= 0:
                print("Error: Jumlah harus lebih dari 0.\n")
                continue
        except ValueError:
            print("Error: Masukkan jumlah dalam angka.\n")
            continue

        # Masukkan ke keranjang
        # Jika barang sudah ada, tambahkan jumlahnya
        keranjang[kode] = keranjang.get(kode, 0) + jumlah
        print(f"-> Berhasil menambah {jumlah} {PRODUK[kode][0]}.\n")

    # --- Selesai belanja, lanjut ke pembayaran ---

    if not keranjang:
        print("Anda tidak membeli apa-apa. Terima kasih.")
        return # Hentikan program

    # Hitung total belanja
    print("\n===== RINCIAN BELANJA =====")
    for kode, jumlah in keranjang.items():
        nama_barang = PRODUK[kode][0]
        harga_barang = PRODUK[kode][1]
        
        # Hitung subtotal per item
        sub_total_item = harga_barang * jumlah
        print(f"{nama_barang} (x{jumlah}) = Rp {sub_total_item}")
        
        # Tambahkan ke total belanja keseluruhan
        total_belanja += sub_total_item
    
    print("----------------------------")
    print(f"TOTAL BELANJA ANDA: Rp {total_belanja}")
    print("----------------------------")

    # --- Proses Pembayaran ---
    while True:
        try:
            uang_bayar = int(input("Masukkan jumlah uang pembayaran: Rp "))
            
            if uang_bayar < total_belanja:
                print(f"Uang Anda kurang Rp {total_belanja - uang_bayar}. Silakan bayar dengan cukup.")
            else:
                kembalian = uang_bayar - total_belanja
                print(f"Uang Anda: Rp {uang_bayar}")
                print(f"Kembalian: Rp {kembalian}")
                print("\n--- TERIMA KASIH! ---")
                break # Keluar dari loop pembayaran
                
        except ValueError:
            print("Error: Masukkan jumlah uang dalam bentuk angka.")

# Menjalankan program utama
jalankan_kasir()