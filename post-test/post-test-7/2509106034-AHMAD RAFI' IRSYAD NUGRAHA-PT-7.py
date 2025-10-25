import os
os.system("cls || clear") 

list_akun_admin = {}
list_akun_user = {}
data_pelanggan = {}

def admin_regist():
    print("Anda belum memiliki akun Admin, silahkan register akun terlebih dahulu\n")
    username = input("Buat Username Anda: ")
    password = input("Buat Password Anda: ")
    list_akun_admin.update({username:password})
    os.system("cls || clear")
    print("\n----------------REGISTRASI BERHASIL!----------------\n")
    
def admin_login():
    login_status = False
    print("Silahkan login menggunakan akun Admin")
    while True:
        username = input("Masukan Username Admin: ")
        password = input("Masukan Password Admin: ")
        for username_tersimpan,password_tersimpan in list_akun_admin.items():
            if username == username_tersimpan and password == password_tersimpan:
                os.system("cls || clear")
                print("\n--------------Login Berhasil!--------------\n")
                login_status = True
                break
        
        if login_status:
            break
        else:
            os.system("cls || clear")
            print("\n=====Username dan Password tidak sesuai, silahkan ulangi lagi=====")
            continue
        

    
    

def login_menu():
    os.system("cls || clear") 
    print("=========SISTEM SERVIS PERANGKAT ELEKTRONIK=========\n")
    print("-----SEBAGAI APA ANDA MENGGUNAKAN PROGRAM INI?-----")
    print("1. Admin")
    print("2. User")
    print("3. Keluar")
    
    
    

def input_number_handling(input_message):
    while True:
        try:
            user_input = int(input(input_message))
            return user_input
        except ValueError:
            print("Mohon Masukan Angka!\n")
            continue

def input_handling(input_message):
    while True:

        try:
            user_input = input(input_message)
            if user_input == "":
                raise ValueError("Input tidak boleh kosong, silahkan coba lagi!\n")
            else:
                return user_input
        except ValueError as e:
            print(e)
            continue
    

def crud_menu():
    print("=========SISTEM SERVIS PERANGKAT ELEKTRONIK===========\n")
    print("Anda Login sebagai Admin, Silahkan pilih menu dibawah:")
    
    while True:
        print("\n======================================================")
        print("1. Tambah Data Servis (Create)")
        print("2. Tampilkan Data Servis (Read)")
        print("3. Ubah Data Service (Update)")
        print("4. Hapus Data Pelanggan (Delete)")
        print("5. Keluar")
        print("======================================================")

def update_data():
    read_data()
    while True:
                            
        pilih_data = input("\npilih data yang ingin anda ubah berdasarkan Kodenya: ") 
                            
        data_terpilih = data_pelanggan.get(pilih_data)
        if data_terpilih != None:
            break
        else:
            print("Data tidak ditemukan, Coba lagi")
            continue

    while True: 
        os.system("cls || clear")
        print("\n=================================================")
        print("Pilih jenis data servis yang ingin anda ubah: ")
        print("=================================================")
        print("1. Nama Pelanggan")
        print("2. Jenis Perangkat")
        print("3. Jenis Kerusakan")
        print("4. Status Perbaikan")
        print("5. Biaya Service")
        print("=================================================")
        pilih_data_baru = input("pilih data [1-5]: ")
        if pilih_data_baru == "1":         
            nama_pelanggan_baru = input_handling("Masukan Nama pelanggan Baru: ")
            data_terpilih["nama pelanggan"] = nama_pelanggan_baru
            
        elif pilih_data_baru == "2":
            jenis_perangkat_baru = input_handling("Masukan Jenis Perangkat Baru: ")
            data_terpilih["jenis perangkat"] = jenis_perangkat_baru
            
        elif pilih_data_baru == "3":
            keluhan_baru = input_handling("Masukan Jenis Kerusakan Baru: ")
            data_terpilih["jenis kerusakan"] = keluhan_baru
            
        elif pilih_data_baru == "4":
            status_perbaikan_baru = input_handling("Masukan Status Perbaikan Baru: ")
            data_terpilih["status perbaikan"] = status_perbaikan_baru
            
        elif pilih_data_baru == "5":
            biaya_service_baru = input_number_handling("Masukan Biaya service Baru: ")
            data_terpilih["biaya service"] = biaya_service_baru
            
        else:
            os.system("cls || clear")
            print("Pilihan tidak dikenali, silahkan ulangi lagi")
            continue
        
        print("\n=====Data sukses Diubah!=====\n")  
        ulangi = input("Apakah ada data yang ingin anda ubah lagi? ketik Y jika iya: ")
        if ulangi == "Y" or ulangi == "y":
            os.system("cls || clear")
            continue
        else: 
            os.system("cls || clear")
            break  
    
    


def create_data():
     
    os.system("cls || clear") 
    print("\n=========Silahkan Buat Data pelanggan baru=========\n")
    
    nama_pelanggan = input_handling("Masukan nama pelanggan: ")
    jenis_perangkat = input_handling("Masukan jenis Perangkat: ")
    keluhan = input_handling("Masukan jenis kerusakan: ")    
    biaya_service = input_number_handling("Masukan biaya service: ")
    status_perbaikan = "Belum Diperbaiki"
    
    kode_unik = f"{nama_pelanggan[0]}{jenis_perangkat[0]}{keluhan[0]}{str(biaya_service)[0]}"
    
    
    
    data_pelanggan.update({kode_unik:{
        "nama pelanggan": nama_pelanggan,
        "jenis perangkat":jenis_perangkat,
        "jenis kerusakan":keluhan,
        "status perbaikan": status_perbaikan,
        "biaya service": biaya_service
        }})
    print("\nData Berhasil Ditambahkan!\n")
    ulangi = input("Apakah Anda ingin menambahkan data lagi? ketik Y jika iya: ")
    if ulangi == "Y" or ulangi == "y":
        os.system("cls || clear")
        create_data()
    else: 
        os.system("cls || clear")
        
        
def read_data():
    os.system("cls || clear") 
    print("========================================================================================================================================")

    no_urut = 1
    if len(data_pelanggan) > 0:
        print(f"{"No.":<4} | {"Kode":<5} | {"Nama pelanggan":<15} | {"Jenis Perangkat":<20} | {"Jenis Kerusakan":<35} | {"Status Perbaikan":<20} | {"Biaya Service":<20}")
        print("________________________________________________________________________________________________________________________________________")
        for kode_unik,data in data_pelanggan.items():
            print(f"{no_urut:<4} | {kode_unik:<5} | {data["nama pelanggan"]:<15} | {data["jenis perangkat"]:<20} | {data["jenis kerusakan"]:<35} | {data["status perbaikan"]:<20} | {data["biaya service"]:<20}")
            no_urut+=1
    else:
        print("\nBelum ada Data yang tersimpan, silahkan Buat Data servis terlebih dahulu")
    print("========================================================================================================================================")
    
def delete_data():
    while True:
        read_data()
        pilih_data = input("\npilih data yang ingin anda ubah berdasarkan Kodenya: ") 
        
        data_terpilih = data_pelanggan.get(pilih_data)
        if data_terpilih != None:
            del data_pelanggan[pilih_data]
            print("\n======Data Berhasil Dihapus!======\n")
        else:
            print("Data tidak ditemukan, Coba lagi")
            continue
        ulangi = input("Apakah ada data yang ingin anda hapus lagi? ketik Y jika iya: ")
        if ulangi == "Y" or ulangi == "y":
            os.system("cls || clear")
            continue
        else: 
            os.system("cls || clear")
            break
    


while True:
    login_menu()
    login_menu = input("Masukan Kode angka untuk login: ")
    if login_menu == "1":
        os.system("cls || clear")
        if len(list_akun_admin) == 0:
            admin_regist()
        else:
            admin_login()
        
        
            pilih_menu = input("Pilih menu [1-5]: ")
            if pilih_menu == "1":
                create_data()

            elif pilih_menu == "2":
                read_data()
                
            elif pilih_menu == "3":
                update_data()
                
            elif pilih_menu == "4":
                delete_data()
                
            elif pilih_menu == "5":
                break
            
            else:
                print("\nPilihan tidak dikenali, mohon input pilihan antara angka 1 sampai 5!\n")
                continue


    elif login_menu == "2":
        os.system("cls || clear") 

        if len(list_akun_user) == 0:
            print("Anda belum memiliki akun, silahkan register akun terlebih dahulu\n")
            username = input("Buat Username Anda: ")
            password = input("Buat Password Anda: ")
            list_akun_user.update({username:password})
            os.system("cls || clear")
            print("\n----------------REGISTRASI BERHASIL!----------------\n")
        else:
            login_status = False
            print("Silahkan login menggunakan akun Anda")
            while True:
                username = input("Masukan Username Anda: ")
                password = input("Masukan Password Anda: ")

                for username_tersimpan,password_tersimpan in list_akun_user.items():
                    if username == username_tersimpan and password == password_tersimpan:
                        os.system("cls || clear")
                        print("\n--------------Login Berhasil!--------------\n")
                        login_status = True
                        break
                
                if login_status:
                    break
                else:
                    os.system("cls || clear")
                    print("\n=====Username dan Password tidak sesuai, silahkan ulangi lagi=====")
                    continue

        print("=========SISTEM SERVIS PERANGKAT ELEKTRONIK===========\n")
        print("Anda Login sebagai User, Silahkan pilih menu dibawah:")
        while True:
            print("\n======================================================")
            print("1. Buat Laporan Servis")
            print("2. Tampilkan Data Servis Saya")
            print("3. Keluar")
            print("======================================================")
            pilih_menu = input("Pilih menu [1-3]: ")

            if pilih_menu == "1": 
                os.system("cls || clear") 
                print("\n=========Silahkan Buat Data Servis Anda=========\n")
                while True:
                    nama_pelanggan = input("Masukan nama Anda: ")
                    if nama_pelanggan == "":
                        print("Input tidak boleh kosong, silahkan coba lagi!\n")
                        continue
                    else:
                        break
                while True:
                    jenis_perangkat = input("Masukan jenis Perangkat Anda: ")
                    if nama_pelanggan == "":
                        print("Input tidak boleh kosong, silahkan coba lagi!\n")
                        continue
                    else:
                        break
                while True:
                    keluhan = input("Masukan Keluhan Anda: ")
                    if nama_pelanggan == "":
                        print("Input tidak boleh kosong, silahkan coba lagi!\n")
                        continue
                    else:
                        break

                biaya_service = "Belum diinput Admin"
                status_perbaikan = "Belum Diperbaiki"

                kode_unik = f"{nama_pelanggan[0]}{jenis_perangkat[0]}{keluhan[0]}0"

                data_pelanggan.update({kode_unik:{
                    "nama pelanggan": nama_pelanggan,
                    "jenis perangkat":jenis_perangkat,
                    "jenis kerusakan":keluhan,
                    "status perbaikan": status_perbaikan,
                    "biaya service": biaya_service
                }})
                
                os.system("cls || clear")
                print("\nData Anda Berhasil Ditambahkan!\n")
                    
            elif pilih_menu == "2":
                os.system("cls || clear") 
                if len(data_pelanggan) > 0:

                    nama_pelanggan = input("Masukan nama untuk melihat data servis Anda: ")
                    for kode,data in data_pelanggan.items():
                        if data["nama pelanggan"] == nama_pelanggan:
                            no_urut = 1
                            print("Data Anda Ditemukan!")
                            print("\n========================================================================================================================================")
                            print(f"{"No.":<4} | {"Nama pelanggan":<15} | {"Jenis Perangkat":<20} | {"Jenis Kerusakan":<35} | {"Status Perbaikan":<20} | {"Biaya Service":<20}")
                            print("________________________________________________________________________________________________________________________________________")
                            print(f"{no_urut:<4} | {data["nama pelanggan"]:<15} | {data["jenis perangkat"]:<20} | {data["jenis kerusakan"]:<35} | {data["status perbaikan"]:<20} | {data["biaya service"]:<20}")
                            print("========================================================================================================================================")
                            data_ditemukan = True
                            break
                        else:
                            data_ditemukan = False
                    if(data_ditemukan == False):
                        os.system("cls || clear")
                        print("Mohon Maaf, data anda tidak ditemukan")
                else:
                    os.system("cls || clear")
                    print("Belum Ada data pelanggan, silahkan buat data anda terlebih dahulu")
                
            elif pilih_menu == "3":
                break
            else:
                os.system("cls || clear")
                print("Pilihan Tidak dikenali!, silahkan ulangi input menu")
                continue



    elif login_menu == "3":
        break
    else:
        print("Input tidak dikenal, silahkan ulangi login")
        continue

print("\n=============PROGRAM BERAKHIR=============")



