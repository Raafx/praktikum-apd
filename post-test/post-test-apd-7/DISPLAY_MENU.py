import os

# PROSEDUR

def login_menu():
    os.system("cls || clear") 
    print("=========SISTEM SERVIS PERANGKAT ELEKTRONIK=========\n")
    print("-----SEBAGAI APA ANDA MENGGUNAKAN PROGRAM INI?-----")
    print("1. Admin")
    print("2. User")
    print("3. Keluar")

def crud_menu():
    print("=========SISTEM SERVIS PERANGKAT ELEKTRONIK===========\n")
    print("Anda Login sebagai Admin, Silahkan pilih menu dibawah:")
    
    
    print("\n======================================================")
    print("1. Tambah Data Servis (Create)")
    print("2. Tampilkan Data Servis (Read)")
    print("3. Ubah Data Service (Update)")
    print("4. Hapus Data Pelanggan (Delete)")
    print("5. Keluar")
    print("======================================================")
    
def user_menu():
    print("=========SISTEM SERVIS PERANGKAT ELEKTRONIK===========\n")
    print("Anda Login sebagai User, Silahkan pilih menu dibawah:")
    
    print("\n======================================================")
    print("1. Buat Laporan Servis")
    print("2. Tampilkan Data Servis Saya")
    print("3. Keluar")
    print("======================================================")
    

def update_menu():
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

