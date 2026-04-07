# Data harga BBM
harga_bbm = {
    "premium": 8000,
    "Pertalite": 10000,
    "Pertamax": 14000,
    "Solar": 6800,
    "dexlite": 12500
}

# List untuk menyimpan transaksi
transaksi = []

def tampilkan_menu():
    print("\n=== SISTEM ADMINISTRASI SPBU ===")
    print("1. Input Transaksi")
    print("2. Lihat Laporan")
    print("3. Keluar")

def input_transaksi():
    print("\n--- Input Transaksi ---")
    print("Jenis BBM:")
    
    for i, bbm in enumerate(harga_bbm.keys(), start=1):
        print(f"{i}. {bbm} - Rp{harga_bbm[bbm]}/liter")
    
    pilihan = int(input("Pilih jenis BBM (1,2,3,4,5): "))
    jenis = list(harga_bbm.keys())[pilihan - 1]
    
    liter = float(input("Masukkan jumlah liter: "))
    
    total = liter * harga_bbm[jenis]
    
    data = {
        "jenis": jenis,
        "liter": liter,
        "total": total
    }
    
    transaksi.append(data)
    
    print(f"\nTotal bayar: Rp{total}")
    print("Transaksi berhasil disimpan!")

def lihat_laporan():
    print("\n--- LAPORAN TRANSAKSI ---")
    
    if len(transaksi) == 0:
        print("Belum ada transaksi.")
        return
    
    total_pendapatan = 0
    
    for i, t in enumerate(transaksi, start=1):
        print(f"{i}. {t['jenis']} - {t['liter']} liter - Rp{t['total']}")
        total_pendapatan += t['total']
    
    print(f"\nTotal Pendapatan: Rp{total_pendapatan}")

# Program utama
while True:
    tampilkan_menu()
    pilih = input("Pilih menu: ")
    
    if pilih == "1":
        input_transaksi()
    elif pilih == "2":
        lihat_laporan()
    elif pilih == "3":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")# Data harga BBM
harga_bbm = {
    "premium": 8000,
    "Pertalite": 10000,
    "Pertamax": 14000,
    "Solar": 6800,
    "dexlite": 12500
}

# List untuk menyimpan transaksi
transaksi = []

def tampilkan_menu():
    print("\n=== SISTEM ADMINISTRASI SPBU ===")
    print("1. Input Transaksi")
    print("2. Lihat Laporan")
    print("3. Keluar")

def input_transaksi():
    print("\n--- Input Transaksi ---")
    print("Jenis BBM:")
    
    for i, bbm in enumerate(harga_bbm.keys(), start=1):
        print(f"{i}. {bbm} - Rp{harga_bbm[bbm]}/liter")
    
    pilihan = int(input("Pilih jenis BBM (1,2,3,4,5): "))
    jenis = list(harga_bbm.keys())[pilihan - 1]
    
    liter = float(input("Masukkan jumlah liter: "))
    
    total = liter * harga_bbm[jenis]
    
    data = {
        "jenis": jenis,
        "liter": liter,
        "total": total
    }
    
    transaksi.append(data)
    
    print(f"\nTotal bayar: Rp{total}")
    print("Transaksi berhasil disimpan!")

def lihat_laporan():
    print("\n--- LAPORAN TRANSAKSI ---")
    
    if len(transaksi) == 0:
        print("Belum ada transaksi.")
        return
    
    total_pendapatan = 0
    
    for i, t in enumerate(transaksi, start=1):
        print(f"{i}. {t['jenis']} - {t['liter']} liter - Rp{t['total']}")
        total_pendapatan += t['total']
    
    print(f"\nTotal Pendapatan: Rp{total_pendapatan}")

# Program utama
while True:
    tampilkan_menu()
    pilih = input("Pilih menu: ")
    
    if pilih == "1":
        input_transaksi()
    elif pilih == "2":
        lihat_laporan()
    elif pilih == "3":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")

# Simpan ke file
with open("laporan.txt", "a") as file:
    file.write(f"{jenis},{liter},{total}\n")