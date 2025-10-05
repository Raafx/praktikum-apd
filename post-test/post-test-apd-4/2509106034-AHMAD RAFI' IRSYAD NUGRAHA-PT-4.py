#menginisiasi username dan password
username = "Rafi"
password = "034"

#menginisiasi jumlah percobaan
percobaan = 1

print("\n============Silahkan Login terlebih dahulu============\n")
while True:

    #Menerima input username dan password dari user
    username_input = input("Masukan Username Anda: ")
    password_input = input("Masukan Password Anda: ")

    #mengecek jumlah percobaan terlebih dahulu (nilai awal = 1)
    if percobaan < 5:

        #mengecek apakah username dan password yang diinput user sesuai dengan yang dinisiasi sebelumnya
        if username_input == username and password_input == password:
            print("\n=====Login Berhasil!=====\n")
            login_status = True

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

                isLanjut = input("Apakah anda ingin mengulang program? [ya/tidak]: ")

                if isLanjut != "ya":
                    login_status = False

            break


    
        else:
            print("Username dan Passowrd tidak sesuai, coba lagi!")
            print("=============================================")
            percobaan+=1
    else:
        print("Anda terlalu banyak mencoba, program akan berhenti secara otomatis")
        break


        

print("\n===============Program Selesai===============\n")






