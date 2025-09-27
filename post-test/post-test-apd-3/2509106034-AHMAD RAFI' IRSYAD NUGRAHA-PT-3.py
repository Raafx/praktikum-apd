#menginput ketiga sisi segitiga dari user
sisi_A = int(input("Masukan sisi pertama: "))
sisi_B = int(input("Masukan sisi kedua: "))
sisi_C = int(input("Masukan sisi ketiga: "))

#Menentukan jenis segitiga berdasarkan panjang masing-masing sisinya
if sisi_A <= 0 or sisi_B <= 0 or sisi_C <= 0:
    hasil = "Sisi tidak boleh bernilai kurang dari sama dengan 0!"
elif sisi_A+sisi_B <= sisi_C or sisi_B+sisi_C <= sisi_A or sisi_A+sisi_C <= sisi_B:
    hasil = "Bukan Segitiga"
elif sisi_A == sisi_B == sisi_C:
    hasil = "Segitiga sama sisi"
elif sisi_A == sisi_B != sisi_C or sisi_B == sisi_C != sisi_A or sisi_A == sisi_C != sisi_B:
    hasil = "Segitiga sama kaki"
elif sisi_A != sisi_B != sisi_C:
    hasil = "Segitiga sembarang"

#Menampilkan jenis segitiga
print(hasil)

#Menghitung luas segitiga apabila terdefinisi sebagai segitiga
if hasil != "Bukan Segitiga" and hasil != "Sisi tidak boleh bernilai kurang dari sama dengan 0!":
    s = 1/2*(sisi_A+sisi_B+sisi_C)
    luas_segiitiga = (s*(s-sisi_A)*(s-sisi_B)*(s-sisi_C))**0.5
    print("Luas Segitiga:",luas_segiitiga)

