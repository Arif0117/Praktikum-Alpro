print("=== Nomor 1 ===")
mahasiswa = ("Muhammad Arif Nur Syafii", 2605060040 , "Teknologi Informasi" )
print("Nama: ",mahasiswa[0])
print("Prodi: ",mahasiswa[2])

mahasiswa[2] = "Teknologi Informasi" #kode tersebut error, karena pada index kedua sudah terisi dengan data prodi 

nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print(nilai_angka)#angka 10 dan 4 termasuk elemen unik, maka kedua angka tersebut hanya akan dicetak 1 kali mengikuti aturan struktur data sets

print("=== Nomor 2 ===")

data_mahsiswa = {
    "nim" : "240101",
    "nama" : "Budi Santoso",
    "prodi" : "Teknologi Informasi"
}

data_mahsiswa["prodi"] = "Sastra Mesin"
data_mahsiswa["angkatan"] =  "2026"
del data_mahsiswa["nim"]
print(data_mahsiswa)

print("=== Nomor 3 ===")
keranjang = {
    "apel" : 5000,
    "pisang" : 3000,
    "jeruk" : 7000,
    "anggur" : 15000
}
total = 0

for key, value in keranjang.items():
    print(f"Harga {key}, Rp{value}")
    total += value

print(f"Total belanja: Rp{total}")