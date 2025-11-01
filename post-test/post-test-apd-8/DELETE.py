import os
from READ import read_data

def delete_data(data_pelanggan):
    read_data(data_pelanggan)
    if len(data_pelanggan) > 0:
        pilih_data = input("\npilih data yang ingin anda hapus berdasarkan Kodenya: ") 

        while True:
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
            os.system("cls || clear")
            delete_data(data_pelanggan)
        else: 
            os.system("cls || clear")
            
