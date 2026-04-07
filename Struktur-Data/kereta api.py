import os
from datetime import datetime

# Fungsi clear layar
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Data kereta
kereta_list = []

# Data jadwal
jadwal_list = []

# Data tiket
tiket_list = []

# Fungsi tambah kereta
def tambah_kereta():
    clear()
    nama = input("Masukkan nama kereta: ")
    tujuan = input("Masukkan tujuan: ")
    kapasitas = int(input("Masukkan kapasitas: "))
    
    kereta = {
        "nama": nama,
        "tujuan": tujuan,
        "kapasitas": kapasitas
    }
    kereta_list.append(kereta)
    print("Kereta berhasil ditambahkan!\n")
    input("Tekan Enter untuk lanjut...")

# Fungsi lihat kereta
def lihat_kereta():
    clear()
    if not kereta_list:
        print("Belum ada data kereta.\n")
    else:
        for i, k in enumerate(kereta_list):
            print(f"{i+1}. {k['nama']} - {k['tujuan']} (Kapasitas: {k['kapasitas']})")
    input("\nTekan Enter untuk kembali...")

# Fungsi tambah jadwal
def tambah_jadwal():
    clear()
    
    if not kereta_list:
        print("Belum ada data kereta.")
        input("Tekan Enter...")
        return

    # Tampilkan kereta
    for i, k in enumerate(kereta_list):
        print(f"{i+1}. {k['nama']} - {k['tujuan']}")

    index = int(input("Pilih kereta (nomor): ")) - 1

    # Validasi waktu
    while True:
        waktu_input = input("Masukkan waktu (HH:MM): ")
        try:
            datetime.strptime(waktu_input, "%H:%M")
            break
        except:
            print("Format salah! Gunakan HH:MM (contoh: 08:30)")

    jadwal = {
        "kereta": kereta_list[index]["nama"],
        "tujuan": kereta_list[index]["tujuan"],
        "waktu": waktu_input,
        "kursi_tersedia": kereta_list[index]["kapasitas"]
    }

    jadwal_list.append(jadwal)
    print("Jadwal berhasil ditambahkan!\n")
    input("Tekan Enter untuk lanjut...")

# Fungsi lihat jadwal
def lihat_jadwal():
    clear()
    if not jadwal_list:
        print("Belum ada jadwal.\n")
    else:
        for i, j in enumerate(jadwal_list):
            print(f"{i+1}. {j['kereta']} ke {j['tujuan']} - {j['waktu']} (Sisa kursi: {j['kursi_tersedia']})")
    input("\nTekan Enter untuk kembali...")

# Fungsi pesan tiket
def pesan_tiket():
    clear()
    
    if not jadwal_list:
        print("Belum ada jadwal.")
        input("Tekan Enter...")
        return

    # Tampilkan jadwal
    for i, j in enumerate(jadwal_list):
        print(f"{i+1}. {j['kereta']} ke {j['tujuan']} - {j['waktu']} (Sisa kursi: {j['kursi_tersedia']})")

    index = int(input("Pilih jadwal (nomor): ")) - 1

    if jadwal_list[index]["kursi_tersedia"] <= 0:
        print("Tiket habis!")
        input("Tekan Enter...")
        return

    nama = input("Masukkan nama penumpang: ")

    tiket = {
        "nama": nama,
        "kereta": jadwal_list[index]["kereta"],
        "tujuan": jadwal_list[index]["tujuan"],
        "waktu": jadwal_list[index]["waktu"]
    }

    tiket_list.append(tiket)
    jadwal_list[index]["kursi_tersedia"] -= 1

    print("Tiket berhasil dipesan!\n")
    input("Tekan Enter untuk lanjut...")

# Fungsi laporan
def laporan():
    clear()
    if not tiket_list:
        print("Belum ada tiket terjual.\n")
    else:
        for t in tiket_list:
            print(f"{t['nama']} - {t['kereta']} ke {t['tujuan']} ({t['waktu']})")
    input("\nTekan Enter untuk kembali...")

# Menu utama
def menu():
    while True:
        clear()
        print("=== SISTEM ADMINISTRASI STASIUN KERETA API ===")
        print("1. Tambah Kereta")
        print("2. Lihat Kereta")
        print("3. Tambah Jadwal")
        print("4. Lihat Jadwal")
        print("5. Pesan Tiket")
        print("6. Laporan")
        print("7. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_kereta()
        elif pilihan == "2":
            lihat_kereta()
        elif pilihan == "3":
            tambah_jadwal()
        elif pilihan == "4":
            lihat_jadwal()
        elif pilihan == "5":
            pesan_tiket()
        elif pilihan == "6":
            laporan()
        elif pilihan == "7":
            clear()
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter...")

# Jalankan program
menu()