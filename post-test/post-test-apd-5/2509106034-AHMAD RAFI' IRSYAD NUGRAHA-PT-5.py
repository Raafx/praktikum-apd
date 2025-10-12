import os
os.system("cls || clear") 



data_pelanggan = []

while True:
    os.system("cls || clear") 
    print("=========SISTEM SERVIS PERANGKAT ELEKTRONIK=========\n")
    print("-----SEBAGAI APA ANDA MENGGUNAKAN PROGRAM INI?-----")
    print("1. Admin")
    print("2. User")
    print("3. Keluar")
    user_status = input("Masukan Kode angka untuk login: ")
    os.system("cls || clear")
    
    if user_status == "1":

        print("=========SISTEM SERVIS PERANGKAT ELEKTRONIK=========\n")
        print("Anda Login sebagai Admin, Silahkan pilih menu dibawah:")

        while True:
            
            print("1. Tambah Data Servis (Create)")
            print("2. Tampilkan Data Servis (Read)")
            print("3. Ubah Data Service (Update)")
            print("4. Hapus Data Pelanggan (Delete)")
            print("5. Keluar")
            pilih_menu = input("Pilih menu [1-5]: ")
            if pilih_menu == "1":
                nama_pelanggan = input("Masukan nama pelanggan: ")
                jenis_perangkat = input("Masukan jenis Perangkat: ")
                keluhan = input("Masukan jenis kerusakan: ")
                while True:
                    isNumber = True
                    biaya_service = input("Masukan biaya service: ")
                    for i in biaya_service:
                        if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
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

                data_pelanggan.append([nama_pelanggan,jenis_perangkat,keluhan,status_perbaikan,biaya_service])

            elif pilih_menu == "2":
                if len(data_pelanggan) > 0:
                    print(f"{"No.":<3} {"Nama pelanggan":<20} {"Jenis Perangkat":<20} {"Jenis Kerusakan":<20} {"Status Perbaikan":<20} {"Biaya Service":<20}")

                    for index,data in enumerate(data_pelanggan,1):
                        print(f"{index:<3} {data[0]:<20} {data[1]:<20} {data[2]:<20} {data[3]:<20} {data[4]:<20}")
                else:
                    print("Belum Ada data yang bisa ditampilkan, silahkan Buat Data servis terlebih dahulu")
                         

            elif pilih_menu == "3":
                if len(data_pelanggan) > 0:
                    print(f"\n{"No.":<3} {"Nama pelanggan":<20} {"Jenis Perangkat":<20} {"Jenis Kerusakan":<20} {"Status Perbaikan":<20} {"Biaya Service":<20}")
                    for index,data in enumerate(data_pelanggan,1):

                        print(f"{index:<3} {data[0]:<20} {data[1]:<20} {data[2]:<20} {data[3]:<20} {data[4]:<20}")

                    while True:
                        isNumber = True
                        pilih_data = input("\npilih data yang ingin anda ubah berdasarkan nomornya: ")
                        for i in pilih_data:
                            if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
                                continue
                            else:
                                print("Mohon Masukan Angka!\n")
                                isNumber = False
                                break
                            
                        if isNumber:
                            pilih_data = int(pilih_data)
                            if pilih_data > len(data_pelanggan):
                                print("Data tidak ditemukan")
                                continue
                            else:
                                data_terpilih = data_pelanggan[pilih_data-1]
                                break
                        else:
                            continue 
                        

                    while True: 
                        print("\nPilih data servis yang ingin anda ubah: ")
                        print("1. Nama Pelanggan")
                        print("2. Jenis Perangkat")
                        print("3. Jenis Kerusakan")
                        print("4. Status Perbaikan")
                        print("5. Biaya Service")
                        pilih_data_servis = input("pilih data [1-5]: ")
                        if pilih_data_servis == "1":
                            nama_pelanggan_baru = input("Masukan Nama pelanggan Baru: ")
                            data_terpilih[0] = nama_pelanggan_baru
                            break
                        elif pilih_data_servis == "2":
                            jenis_perangkat_baru = input("Masukan Jenis Perangkat Baru: ")
                            data_terpilih[1] = jenis_perangkat_baru
                            break
                        elif pilih_data_servis == "3":
                            keluhan_baru = input("Masukan Jenis Kerusakan Baru: ")
                            data_terpilih[2] = keluhan_baru
                            break
                        elif pilih_data_servis == "4":
                            status_perbaikan_baru = input("Masukan Status Perbaikan Baru: ")
                            data_terpilih[3] = status_perbaikan_baru
                            break
                        elif pilih_data_servis == "5":
                            while True:
                                isNumber = True
                                biaya_service_baru = input("Masukan biaya service: ")
                                for i in biaya_service_baru:
                                    if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
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
                                
                            data_terpilih[4] = biaya_service_baru
                            break
                        else:
                            print("Pilihan tidak dikenali, silahkan ulangi lagi")
                            continue
                else:
                    print("Belum Ada data yang bisa diubah, silahkan Buat Data servis terlebih dahulu")

        
                
            elif pilih_menu == "4":
                if len(data_pelanggan) > 0:

                    print(f"\n{"No.":<3} {"Nama pelanggan":<20} {"Jenis Perangkat":<20} {"Jenis Kerusakan":<20} {"Status Perbaikan":<20} {"Biaya Service":<20}")
                    for index,data in enumerate(data_pelanggan,1):

                        print(f"{index:<3} {data[0]:<20} {data[1]:<20} {data[2]:<20} {data[3]:<20} {data[4]:<20}")

                    while True:
                        isNumber = True
                        pilih_data = input("\npilih data yang ingin anda Hapus berdasarkan nomornya: ")
                        for i in pilih_data:
                            if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
                                continue
                            else:
                                print("Mohon Masukan Angka!\n")
                                isNumber = False
                                break
                            
                        if isNumber:
                            pilih_data = int(pilih_data)
                            if pilih_data > len(data_pelanggan):
                                print("Data tidak ditemukan")
                                continue
                            else:
                                del data_pelanggan[pilih_data-1]
                                print("=======Data Berhasil Terhapus!=======")
                                break
                        else:
                            continue 
                else:
                    print("Belum ada data yang bisa dihapus, silahkan buat data servis terlebih dahulu")
                

            elif pilih_menu == "5":
                pass
            else:
                print("\nPilihan tidak dikenali, mohon input pilihan antara angka 1 sampai 5!\n")
                continue


    elif user_status == "2":
        break
    elif user_status == "3":
        break
    else:
        print("Input tidak dikenal, silahkan ulangi login")
        continue

print("\n=============PROGRAM BERAKHIR=============")



