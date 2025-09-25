# angka = ""

# if angka:
#     print("angka lebih besar dari lima")

# # contoh pertama
# cuaca = "panas"
# if cuaca == "hujan":
#     print("Di rumah aja")
# else:
#     print("Nongkrong")

# # contoh kedua

# nilai = 70

# # if nilai >= 70:
# #     print("lulus")
# # else:
# #     print("tidak lulus") 

# status = "lulus" if nilai > 70 else "tidak lulus"
# print(status)

# cuaca = "badai"

# if cuaca == "hujan":
#     print("di rumah aja")

# elif cuaca == "mendung":
#     print("makan mie")

# else:
#     print("nongkrong")

#contoh 4

# usia = int(input("Masukan usia: "))

# if usia < 0:
#     print("Usia tidak valid")
# elif usia <= 13:
#     print("Anak-anak")
# elif usia <= 18:
#     print("Remaja")
# elif usia <= 40:
#     print("Dewasa")
# else:
#     print("Tua")

# nilai = int(input("Masukan Nilai: "))

# if nilai >= 90:
#     print("A")
# elif nilai >= 70:
#     print("B")
# elif nilai >= 60:
#     print("C")
# elif nilai <= 60:
#     print("D")

# ternary operator

# nested if

# a = 4
# b = 5
# c = 6

# if a<b:
#     if a<c:
#         print("a paling kecil")
#     else:
#         print("c lebih kecil dari a")
# elif a<c:
#     print("c lebih besar")
# else:
#     print("c paling besar")


# studi kasus 1

# tinggi = float(input("Masukan tinggi badan: "))

# status = "Diizinikan" if tinggi >= 145 else "Tidak diizinkan"
# print(status)

# harga_barang = int(input("Masukan Harga Berang: "))

# if harga_barang < 0:
#     print("Gratis ini")
# elif harga_barang > 100000:
#     total_bayar = harga_barang-(harga_barang*20/100)
#     print("Anda Mendapatkan diskon 20%")
    
# elif harga_barang > 50000:
#     total_bayar = harga_barang-(harga_barang*10/100)
#     print("Anda Mendapatkan diskon 10%")
    
# else:
#     print("Maaf yah ga dapat diskon")
#     total_bayar = harga_barang

# print("Total bayar anda:",total_bayar)

nilai = int(input("Masukan Nilai: "))
kelas = input("Masukan kelas: ")

if nilai > 80 and (kelas == "A" or kelas == "a"):
    print("IPK 4")
elif nilai > 80 and (kelas == "B" or kelas == "b"):
    print("IPK 3")
else:
    print("IPK 2")