nama = input("Nama tamu: ")
alamat = input("Alamat tamu: ")

member = input("Member hotel (Y/N): ")
while member != "Y" and member != "N":
    print("Pilihan hanya Y atau N")
    member = input("Member hotel (Y/N): ")

lama = int(input("Lama menginap (malam): "))

print("\nTipe kamar:")
print("1. Suite")
print("2. Superior")
print("3. Deluxe")
pilihan = input("Pilih tipe kamar (1/2/3): ")

if pilihan == "1":
    tipe = "Suite"
    harga = 1000000
elif pilihan == "2":
    tipe = "Superior"
    harga = 600000
elif pilihan == "3":
    tipe = "Deluxe"
    harga = 400000
else:
    tipe = None

if tipe is None:
    print("Pilihan kamar tidak valid")
else:
    diskon = 0
    if member == "Y":
        diskon = harga * 0.2

    harga_akhir = harga - diskon
    total = harga_akhir * lama

    print("\n===== STRUK HOTEL UNTIDAR =====")
    print("Nama tamu       :", nama)
    print("Alamat          :", alamat)
    print("Member          :", member)
    print("Tipe kamar      :", tipe)
    print("Harga kamar     : Rp", harga)
    print("Potongan member : Rp", diskon)
    print("Lama menginap   :", lama, "malam")
    print("Total bayar     : Rp", total)