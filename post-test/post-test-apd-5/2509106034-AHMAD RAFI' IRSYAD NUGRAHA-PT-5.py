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
            print("3. Ubah Status Perbaikan (Update)")
            print("4. Hapus Data Pelanggan (Delete)")
            print("5. Keluar")
            pilih_menu = input("Pilih menu [1-5]: ")
            if pilih_menu == "1":
                jenis_perangkat = input("Masukan jenis Perangkat: ")
                keluhan = input("Masukan jenis kerusakan: ")
                biaya_service = input("Masukan biaya service: ")
                status_perbaikan = "Belum Diperbaiki"

                data_pelanggan.append([jenis_perangkat,keluhan,status_perbaikan,biaya_service])
            elif pilih_menu == "2":
                print("No. Jenis Barang               Jenis Kerusakan          status perbaikan          biaya service")
                for index,data in enumerate(data_pelanggan,1):

                    print(f"{index}.  {data[0]}               {data[1]}                {data[2]}               {data[3]}")
                         

            elif pilih_menu == "3":
                pass
            elif pilih_menu == "4":
                pass
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



