import os 
from ERORR_HANDLING import input_handling,input_number_handling

def user_create(data_pelanggan):
    os.system("cls || clear") 
    print("\n=========Silahkan Buat Data Servis Anda=========\n")
    
    nama_pelanggan = input_handling("Masukan nama Anda: ")
    jenis_perangkat = input_handling("Masukan jenis Perangkat Anda: ")
    keluhan = input_handling("Masukan Keluhan Anda: ")
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

def create_data(data_pelanggan):
     
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
        create_data(data_pelanggan)
    else: 
        os.system("cls || clear")
        
