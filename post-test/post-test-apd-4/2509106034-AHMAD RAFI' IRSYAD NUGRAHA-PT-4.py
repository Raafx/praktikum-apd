import os

os.system("cls")

#menginisiasi username dan password
username = "Rafi"
password = "034"

#menginisiasi jumlah percobaan
percobaan = 0

print("\n============Silahkan Login terlebih dahulu============\n")

#memasuki while looop selama jumlah percobaan kurang dari 5
while percobaan < 5:

    #Menerima input username dan password dari user
    username_input = input("Masukan Username Anda: ")
    password_input = input("Masukan Password Anda: ")

    #mengecek jumlah percobaan terlebih dahulu (nilai awal = 0)

    #mengecek apakah username dan password yang diinput user sesuai dengan yang dinisiasi sebelumnya
    #jika sesuai, maka login dinyatakan berhasil, dan memasuki kode program post-test sebelumnya
    if username_input == username and password_input == password: 
        login_status = True
        print("\n=====Login Berhasil!=====\n")
        break
        
         

    #jika tidak, maka jumlah percobaan akan bertambah 1
    #Jika jumlah percobaan mencapai 5, while loop akan berhenti
    else:
        print("Username dan Password tidak sesuai, coba lagi!")
        print("=============================================")
        percobaan+=1
        login_status = False
    

while login_status:
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

        #Menanyakan user apakah ingin melanjutkan program
        isLanjut = input("Apakah anda ingin mengulang program? [ya/tidak]: ")

        #Jika tidak, maka while akan berhenti dengan menggunakan break
        if isLanjut != "ya":
            break



#menampilkan pesan jika user mencoba login sebanyak 5 kali
if percobaan == 5:
    print("Anda terlalu banyak mencoba, program akan berhenti secara otomatis")
        

print("\n===============Program Selesai===============\n")






