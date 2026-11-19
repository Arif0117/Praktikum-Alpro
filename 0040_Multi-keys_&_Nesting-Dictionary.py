import datetime
import string
import random

data_buku = {}

while True:

    print("=" * 40)
    print("       SISTEM MANAJEMEN PERPUSTAKAAN")
    print("=" * 40)
    judul = input("Judul Buku: ")
    penulis = input("Penulis: ")
    tahun = int(input("Tahun Terbit: "))

    tahun_pinjam = int(input("Tahun buku dipinjam: "))
    bulan_pinjam = int(input("Bulan buku dipinjam: "))
    tanggal_pinjam = int(input("Tanggal buku dipinjam: "))

    tanggal_terakhir_pinjam = datetime.datetime(
        tahun_pinjam,
        bulan_pinjam,
        tanggal_pinjam
    )

    status = input("Status (TERSEDIA/TIDAK): ").upper()

    KEY = ''.join(
        random.choice(string.ascii_uppercase)
        for i in range(6)
    )

    multi_keys = (KEY, judul)

    data_buku[multi_keys] = {
        'penulis': penulis,
        'tahun_terbit': tahun,
        'tanggal_pinjam': tanggal_terakhir_pinjam,
        'status': status
    }

    # Menampilkan seluruh data buku
    print("\n" + "=" * 75)
    print("                 DATA BUKU PERPUSTAKAAN")
    print("=" * 75)

    print(
        f"{'KEY':<8} {'JUDUL BUKU':<20} "
        f"{'PENULIS':<15} {'TAHUN':<8} "
        f"{'TGL PINJAM':<13} {'STATUS':<10}"
    )

    print("-" * 75)

    for multi_keys in data_buku:

        KEY = multi_keys[0]
        JUDUL = multi_keys[1]

        PENULIS = data_buku[multi_keys]['penulis']
        TAHUN = data_buku[multi_keys]['tahun_terbit']
        TANGGAL = data_buku[multi_keys]['tanggal_pinjam'].strftime("%d-%m-%Y")
        STATUS = data_buku[multi_keys]['status']

        print(
            f"{KEY:<8} {JUDUL:<20} "
            f"{PENULIS:<15} {TAHUN:<8} "
            f"{TANGGAL:<13} {STATUS:<10}"
        )

    tambah = input("\nTambah buku lagi? (y/n): ").lower()

    if tambah == "n":
        break
        
print("\nMenutup Perpustakaan")
