import os

# Fungsi clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Data harga BBM
harga_bbm = {
    "premium": 8000,
    "Pertalite": 10000,
    "Pertamax": 14000,
    "Solar": 6800,
    "dexlite": 12500
}

# Data stok BBM (dalam liter)
stok_bbm = {
    "premium": 100,
    "Pertalite": 100,
    "Pertamax": 100,
    "Solar": 100,
    "dexlite": 100
}

# List transaksi
transaksi = []

def tampilkan_menu():
    clear()
    print("=== SISTEM ADMINISTRASI SPBU ===")
    print("1. Input Transaksi")
    print("2. Lihat Laporan")
    print("3. Lihat Stok")
    print("4. Keluar")

def input_transaksi():
    clear()
    print("--- Input Transaksi ---")
    print("Jenis BBM:")
    
    for i, bbm in enumerate(harga_bbm.keys(), start=1):
        print(f"{i}. {bbm} - Rp{harga_bbm[bbm]}/liter (Stok: {stok_bbm[bbm]} liter)")
    
    try:
        pilihan = int(input("Pilih jenis BBM (1-5): "))
        jenis = list(harga_bbm.keys())[pilihan - 1]
    except:
        print("Input tidak valid!")
        input("Tekan Enter untuk lanjut...")
        return
    
    liter = float(input("Masukkan jumlah liter: "))
    
    # CEK STOK
    if liter > stok_bbm[jenis]:
        print("Stok tidak mencukupi!")
        input("Tekan Enter untuk kembali...")
        return
    
    total = liter * harga_bbm[jenis]
    
    # Kurangi stok
    stok_bbm[jenis] -= liter
    
    # Simpan transaksi
    transaksi.append({
        "jenis": jenis,
        "liter": liter,
        "total": total
    })
    
    print(f"\nTotal bayar: Rp{total}")
    print("Transaksi berhasil!")
    
    # Notifikasi stok menipis
    if stok_bbm[jenis] < 20:
        print("⚠️ Stok hampir habis!")
    
    input("Tekan Enter untuk kembali ke menu...")

def lihat_laporan():
    clear()
    print("--- LAPORAN TRANSAKSI ---")
    
    if not transaksi:
        print("Belum ada transaksi.")
    else:
        total_pendapatan = 0
        
        for i, t in enumerate(transaksi, start=1):
            print(f"{i}. {t['jenis']} - {t['liter']} liter - Rp{t['total']}")
            total_pendapatan += t['total']
        
        print(f"\nTotal Pendapatan: Rp{total_pendapatan}")
    
    input("Tekan Enter untuk kembali...")

def lihat_stok():
    clear()
    print("--- STOK BBM ---")
    for bbm, stok in stok_bbm.items():
        print(f"{bbm}: {stok} liter")
    
    input("Tekan Enter untuk kembali...")

# Program utama
while True:
    tampilkan_menu()
    pilih = input("Pilih menu: ")
    
    if pilih == "1":
        input_transaksi()
    elif pilih == "2":
        lihat_laporan()
    elif pilih == "3":
        lihat_stok()
    elif pilih == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk lanjut...")