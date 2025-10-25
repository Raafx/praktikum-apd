import os

def read_data(data_pelanggan):
    os.system("cls || clear") 
    
    no_urut = 1
    if len(data_pelanggan) > 0:
        print("\n========================================================================================================================================")
        print(f"{"No.":<4} | {"Kode":<5} | {"Nama pelanggan":<15} | {"Jenis Perangkat":<20} | {"Jenis Kerusakan":<35} | {"Status Perbaikan":<20} | {"Biaya Service":<20}")
        print("________________________________________________________________________________________________________________________________________")
        for kode_unik,data in data_pelanggan.items():
            print(f"{no_urut:<4} | {kode_unik:<5} | {data["nama pelanggan"]:<15} | {data["jenis perangkat"]:<20} | {data["jenis kerusakan"]:<35} | {data["status perbaikan"]:<20} | {data["biaya service"]:<20}")
            no_urut+=1
        print("========================================================================================================================================\n")
    else:
        print("\nBelum ada Data yang tersimpan, silahkan Buat Data servis terlebih dahulu\n")
    
    
def user_read(data_pelanggan):
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

    