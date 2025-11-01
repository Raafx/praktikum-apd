import os

from prettytable import PrettyTable


def read_data(data_pelanggan):
    
    os.system("cls || clear") 
    
    table = PrettyTable()
    no_urut = 1
    if len(data_pelanggan) > 0:
        table.field_names = ["No. ", "Kode", "Nama Pelanggan", "Jenis Perangkat", "Jenis Kerusakan", "Status Perbaikan", "Biaya Service"]
        
        for kode_unik,data in data_pelanggan.items():
            table.add_row([no_urut, kode_unik, data["nama pelanggan"], data["jenis perangkat"], data["jenis kerusakan"], data["status perbaikan"], data["biaya service"]])
            no_urut+=1
        print(table)
        print()
    else:
        print("\nBelum ada Data yang tersimpan, silahkan Buat Data servis terlebih dahulu\n")
    
    
def user_read(data_pelanggan):
    os.system("cls || clear") 
    table = PrettyTable()
    
    if len(data_pelanggan) > 0:
        nama_pelanggan = input("Masukan nama untuk melihat data servis Anda: ")
        for kode,data in data_pelanggan.items():
            if data["nama pelanggan"] == nama_pelanggan:
                no_urut = 1
                table.field_names = ["No. ", "Nama Pelanggan", "Jenis Perangkat", "Jenis Kerusakan", "Status Perbaikan", "Biaya Service"]
                
                table.add_row([no_urut, data["nama pelanggan"], data["jenis perangkat"], data["jenis kerusakan"], data["status perbaikan"], data["biaya service"]])
                
                print(table)
                print()
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

    