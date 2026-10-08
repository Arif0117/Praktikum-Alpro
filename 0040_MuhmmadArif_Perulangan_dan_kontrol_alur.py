print("Soal 1")
print("=== Bilangan Ganjil Genap dari 1 sampai 50 ===")

for angka in range(1, 51):
    if angka % 2 == 0:
        print(angka, "adalah Bilangan Genap")
    else:
        print(angka, "adalah Bilangan Ganjil")

print("soal 2")
print("=== Bilangan prima antara 1 sampai 100 ===")

for angka in range(2, 101):
    prima =  True
    for dibagi in range(2, angka):
        if angka % dibagi == 0:
            prima = False
            break
    if prima:
      print(angka, "Angka adalah bilangan prima")
