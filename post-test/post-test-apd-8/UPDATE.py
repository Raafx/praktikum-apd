import os
from ERORR_HANDLING import input_handling,input_number_handling
from READ import read_data
from DISPLAY_MENU import update_menu


def update_data(data_pelanggan):
    read_data(data_pelanggan)
    if len(data_pelanggan) > 0:
         
        while True:

            pilih_data = input("\npilih data yang ingin anda ubah berdasarkan Kodenya: ") 

            data_terpilih = data_pelanggan.get(pilih_data)
            if data_terpilih != None:
                break
            else:
                print("Data tidak ditemukan, Coba lagi")
                continue

        while True:
            
            pilih_data_baru = update_menu()
            if pilih_data_baru == "1":         
                nama_pelanggan_baru = input_handling("Masukan Nama pelanggan Baru: ")
                data_terpilih["nama pelanggan"] = nama_pelanggan_baru
                break

            elif pilih_data_baru == "2":
                jenis_perangkat_baru = input_handling("Masukan Jenis Perangkat Baru: ")
                data_terpilih["jenis perangkat"] = jenis_perangkat_baru
                break

            elif pilih_data_baru == "3":
                keluhan_baru = input_handling("Masukan Jenis Kerusakan Baru: ")
                data_terpilih["jenis kerusakan"] = keluhan_baru
                break

            elif pilih_data_baru == "4":
                status_perbaikan_baru = input_handling("Masukan Status Perbaikan Baru: ")
                data_terpilih["status perbaikan"] = status_perbaikan_baru
                break

            elif pilih_data_baru == "5":
                biaya_service_baru = input_number_handling("Masukan Biaya service Baru: ")
                data_terpilih["biaya service"] = biaya_service_baru
                break

            else:
                os.system("cls || clear")
                print("Pilihan tidak dikenali, silahkan ulangi lagi")
                continue
            
        print("\n=====Data sukses Diubah!=====\n")  
        ulangi = input("Apakah ada data yang ingin anda ubah lagi? ketik Y jika iya: ")
        if ulangi == "Y" or ulangi == "y":
            os.system("cls || clear")
            update_data(data_pelanggan)
        else: 
            os.system("cls || clear")
          
