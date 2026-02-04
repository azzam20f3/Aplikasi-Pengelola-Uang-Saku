import json

saldo = 0
laporan_pemasukan = []
laporan_pengeluaran = []

def simpan_saldo():
    global saldo, laporan_pemasukan, laporan_pengeluaran
    with open("saldo.json", "w") as file:
        json.dump({
            "saldo": saldo,
            "pemasukan": laporan_pemasukan,
            "pengeluaran": laporan_pengeluaran
        }, file, indent=2)

def muat_saldo():
    global saldo, laporan_pemasukan, laporan_pengeluaran
    try:
        with open("saldo.json", "r") as file:
            data = json.load(file)
            saldo = data["saldo"]
            laporan_pemasukan = data.get("pemasukan", [])
            laporan_pengeluaran = data.get("pengeluaran", [])
    except FileNotFoundError:
        saldo = 0
        laporan_pemasukan = []
        laporan_pengeluaran = []

def tambah_pemasukan():
    global saldo, laporan_pemasukan
    jumlah = int(input("Masukkan jumlah pemasukan: "))
    keterangan = input("Masukkan keterangan (opsional): ")
    saldo = saldo + jumlah
    laporan_pemasukan.append({"jumlah": jumlah, "keterangan": keterangan})
    print(f"Pemasukan sebesar Rp{jumlah} berhasil ditambahkan!")

def tambah_pengeluaran():
    global saldo, laporan_pengeluaran
    jumlah = int(input("Masukkan jumlah pengeluaran: "))
    keterangan = input("Masukkan keterangan (opsional): ")
    if jumlah > saldo:
        print(f"Peringatan: Saldo tidak cukup! Saldo Anda hanya Rp{saldo}")
    else:
        saldo = saldo - jumlah
        laporan_pengeluaran.append({"jumlah": jumlah, "keterangan": keterangan})
        print(f"Pengeluaran sebesar Rp{jumlah} berhasil dikurangi dari saldo!")

def lihat_saldo():
    print("=" * 30)
    print(f"Saldo Anda saat ini: Rp{saldo}")
    print("=" * 30)

def lihat_laporan():
    total_pemasukan = sum(item["jumlah"] for item in laporan_pemasukan)
    total_pengeluaran = sum(item["jumlah"] for item in laporan_pengeluaran)
    
    print("\n" + "=" * 50)
    print("LAPORAN PEMASUKAN DAN PENGELUARAN")
    print("=" * 50)
    
    print("\n--- PEMASUKAN ---")
    if laporan_pemasukan:
        for i, item in enumerate(laporan_pemasukan, 1):
            keterangan = item["keterangan"] if item["keterangan"] else "(tidak ada keterangan)"
            print(f"{i}. Rp{item['jumlah']} - {keterangan}")
        print(f"Total Pemasukan: Rp{total_pemasukan}")
    else:
        print("Belum ada pemasukan")
    
    print("\n--- PENGELUARAN ---")
    if laporan_pengeluaran:
        for i, item in enumerate(laporan_pengeluaran, 1):
            keterangan = item["keterangan"] if item["keterangan"] else "(tidak ada keterangan)"
            print(f"{i}. Rp{item['jumlah']} - {keterangan}")
        print(f"Total Pengeluaran: Rp{total_pengeluaran}")
    else:
        print("Belum ada pengeluaran")
    
    print("\n--- RINGKASAN ---")
    print(f"Total Pemasukan:   Rp{total_pemasukan}")
    print(f"Total Pengeluaran: Rp{total_pengeluaran}")
    print(f"Saldo Akhir:       Rp{saldo}")
    print("=" * 50 + "\n")

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Lihat laporan")
    print("5. Keluar")

muat_saldo()

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        lihat_laporan()
    elif pilihan == "5":
        simpan_saldo()
        print("Terima kasih! Data Anda sudah disimpan.")
        break
    else:
        print("Pilihan tidak valid")