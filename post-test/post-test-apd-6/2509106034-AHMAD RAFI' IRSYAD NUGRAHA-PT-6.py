import os
os.system("cls || clear") 

list_akun_admin = {}
data_pelanggan = {}

while True:
    os.system("cls || clear") 
    print("=========SISTEM SERVIS PERANGKAT ELEKTRONIK=========\n")
    print("-----SEBAGAI APA ANDA MENGGUNAKAN PROGRAM INI?-----")
    print("1. Admin")
    print("2. User")
    print("3. Keluar")
    login_menu = input("Masukan Kode angka untuk login: ")
    
    
    if login_menu == "1":
        os.system("cls || clear")
        if len(list_akun_admin) == 0:
            print("Anda belum memiliki akun Admin, silahkan register akun terlebih dahulu\n")
            username = input("Buat Username Anda: ")
            password = input("Buat Password Anda: ")
            list_akun_admin.update({username:password})
            print("\n----------------REGISTRASI BERHASIL!----------------\n")
        else:
            login_status = False
            print("Silahkan login menggunakan akun Admin")
            while True:
                username = input("Masukan Username Admin: ")
                password = input("Masukan Password Admin: ")

                for username_tersimpan,password_tersimpan in list_akun_admin.items():
                    if username == username_tersimpan and password == password_tersimpan:
                        print("\n--------------Login Berhasil!--------------\n")
                        login_status = True
                        break
                
                if login_status:
                    break
                else:
                    print("\n=====Username dan Password tidak sesuai, silahkan ulangi lagi=====")
                    continue
        print("======================================================")
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
            pilih_menu = input("Pilih menu [1-5]: ")
            if pilih_menu == "1":
                while True: 
                    os.system("cls || clear") 
                    print("\n=========Silahkan Buat Data pelanggan baru=========\n")
                    nama_pelanggan = input("Masukan nama pelanggan: ")
                    jenis_perangkat = input("Masukan jenis Perangkat: ")
                    keluhan = input("Masukan jenis kerusakan: ")
                    while True:
                        isNumber = True
                        biaya_service = input("Masukan biaya service: ")
                        for i in biaya_service:
                            if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i  == "9":
                                continue
                            else:
                                print("Mohon Masukan Angka!\n")
                                isNumber = False
                                break
                            
                        if isNumber:
                            biaya_service = int(biaya_service)
                            break
                        else:
                            continue
                        
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
                        continue
                    else: 
                        break

            elif pilih_menu == "2":
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
                    print("\nBelum Ada data yang bisa ditampilkan, silahkan Buat Data servis terlebih dahulu")
                print("========================================================================================================================================")


            elif pilih_menu == "3":
                while True: 
                    os.system("cls || clear") 
                    no_urut = 1
                    if len(data_pelanggan) > 0:
                        
                        print(f"{"No.":<4} | {"Kode":<5} | {"Nama pelanggan":<15} | {"Jenis Perangkat":<20} | {"Jenis Kerusakan":<35} | {"Status Perbaikan":<20} | {"Biaya Service":<20}")

                        
                        for kode_unik,data in data_pelanggan.items():

                            print(f"{no_urut:<4} | {kode_unik:<5} | {data["nama pelanggan"]:<15} | {data["jenis perangkat"]:<20} | {data["jenis kerusakan"]:<35} | {data["status perbaikan"]:<20} | {data["biaya service"]:<20}")

                            no_urut+=1
                        while True:
                            
                            pilih_data = input("\npilih data yang ingin anda ubah berdasarkan Kodenya: ") 
                            
                            data_terpilih = data_pelanggan.get(pilih_data)
                            if data_terpilih != None:
                                break
                            else:
                                print("Data tidak ditemukan, Coba lagi")
                                continue

                        while True: 
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
                                nama_pelanggan_baru = input("Masukan Nama pelanggan Baru: ")
                                data_terpilih["nama pelanggan"] = nama_pelanggan_baru
                                break
                            elif pilih_data_baru == "2":
                                jenis_perangkat_baru = input("Masukan Jenis Perangkat Baru: ")
                                data_terpilih["jenis perangkat"] = jenis_perangkat_baru
                                break
                            elif pilih_data_baru == "3":
                                keluhan_baru = input("Masukan Jenis Kerusakan Baru: ")
                                data_terpilih["jenis kerusakan"] = keluhan_baru
                                break
                            elif pilih_data_baru == "4":
                                status_perbaikan_baru = input("Masukan Status Perbaikan Baru: ")
                                data_terpilih["status perbaikan"] = status_perbaikan_baru
                                break
                            elif pilih_data_baru == "5":
                                while True:
                                    isNumber = True
                                    biaya_service_baru = input("Masukan biaya service: ")
                                    for i in biaya_service_baru:
                                        if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i    == "8" or i == "9":
                                            continue
                                        else:
                                            print("Mohon Masukan Angka!\n")
                                            isNumber = False
                                            break
                                        
                                    if isNumber:
                                        biaya_service_baru = int(biaya_service_baru)
                                        break
                                    else:
                                        continue
                                    
                                data_terpilih["biaya service"] = biaya_service_baru
                                break
                            else:
                                print("Pilihan tidak dikenali, silahkan ulangi lagi")
                                continue
                        print("\n=====Data sukses Diubah!=====\n")  
                        ulangi = input("Apakah ada data yang ingin anda ubah lagi? ketik Y jika iya: ")
                        if ulangi == "Y":
                            continue
                        else: 
                            break  

                    else:
                        print("Belum Ada data yang bisa diubah, silahkan Buat Data servis terlebih dahulu")
                        break
                
            elif pilih_menu == "4":
                while True:
                    no_urut = 1
                    os.system("cls || clear") 
                    if len(data_pelanggan) > 0:

                        print(f"{"No.":<4} | {"Kode":<5} | {"Nama pelanggan":<15} | {"Jenis Perangkat":<20} | {"Jenis Kerusakan":<35} | {"Status Perbaikan":<20} | {"Biaya Service":<20}")
                        for kode_unik,data in data_pelanggan.items():

                            print(f"{no_urut:<4} | {kode_unik:<5} | {data["nama pelanggan"]:<15} | {data["jenis perangkat"]:<20} | {data["jenis kerusakan"]:<35} | {data["status perbaikan"]:<20} | {data["biaya service"]:<20}")
                            no_urut+=1

                        while True:
                            pilih_data = input("\npilih data yang ingin anda ubah berdasarkan Kodenya: ") 
                            
                            data_terpilih = data_pelanggan.get(pilih_data)
                            if data_terpilih != None:
                                del data_pelanggan[pilih_data]
                                print("\n======Data Berhasil Dihapus!======\n")
                                break
                            else:
                                print("Data tidak ditemukan, Coba lagi")
                                continue

                        ulangi = input("Apakah ada data yang ingin anda hapus lagi? ketik Y jika iya: ")
                        if ulangi == "Y" or ulangi == "y":
                            continue
                        else: 
                            break 
                    else:
                        print("Belum ada data yang bisa dihapus, silahkan buat data servis terlebih dahulu")
                        break
                

            elif pilih_menu == "5":
                break
            else:
                print("\nPilihan tidak dikenali, mohon input pilihan antara angka 1 sampai 5!\n")
                continue


    elif login_menu == "2":
        os.system("cls || clear") 
        print("======================================================")
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

                nama_pelanggan = input("Masukan nama Anda: ")
                jenis_perangkat = input("Masukan jenis Perangkat Anda: ")
                keluhan = input("Masukan Keluhan Anda: ")
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



