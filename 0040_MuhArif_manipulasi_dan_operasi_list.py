print("==== Soal Nomor 1 ====")

kendaraan = ["motor","mobil","sepeda","bus"]
print(f"Kendaraan: \n{kendaraan}")

kendaraan.append("truk")
print(f"Menambahkan kendaraan truk pada akhir list: \n{kendaraan}")

kendaraan.insert(1,"becak")
print(f"Menyisipkan becak pada index pertama: \n{kendaraan}")

kendaraan.remove("bus")
print(f"Menghapus data paling akhir: \n{kendaraan}")

kendaraan[3] = "skuter"
print(f"Mengubah elemen sepeda menjadi skuter: \n{kendaraan}")

panjang_kendaraan = len(kendaraan)
print(f"Jumlah Kendaraan = {panjang_kendaraan}")

print("==== Soal Nomor 2 ====")

angka = [75, 80, 90, 75, 85, 100, 65]
print(f"list angka: \n{angka}")

index_100 = angka.index(100)
print(f"Angka 100 berapa pada index: {index_100}")

jumlah_siswa_skor_75 = angka.count(75)
print(f"Jumlah siswa yang mendapatkan skor 75: {jumlah_siswa_skor_75}")

print(f"List angka sebelum sort: \n{angka}")
angka.sort()
print(f"Mengurutkan data: \n{angka}")

angka.reverse()
print(f"Membalikkan urutan: \n{angka}")

print("==== Soal Nomor 3 ====")

menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]
menu_utama.extend(menu_tambahan)
print(f"Gabungan menu: \n{menu_utama}")

print("==== Soal Nomor 4 ====")

data_barang = [ ["Buku", 5000], ["pensil", 2000], ["penggaris", 3000]]

print(f"Harga Pensil: {data_barang[0][1]}")

for barang in data_barang:
    print(f"Nama Barang\t: {barang[0]}, Harga Barang: {barang[1]}")
