import os
import inquirer


def login_menu():
    os.system("cls || clear") 
    print("=========SISTEM SERVIS PERANGKAT ELEKTRONIK=========\n")
    print("-----SEBAGAI APA ANDA MENGGUNAKAN PROGRAM INI?-----")
    
    pilih_menu = [inquirer.List(
        "Menu",
        message="Pilih Role Anda",
        choices=[
            "1. Admin",
            "2. User",
            "3. Keluar"]
        )
                  ]
    
    menu_dipilih = inquirer.prompt(pilih_menu)
    return menu_dipilih["Menu"][0]
    
    
    

def crud_menu():
    print("=========SISTEM SERVIS PERANGKAT ELEKTRONIK===========\n")
    print("Anda Login sebagai Admin, Silahkan pilih menu dibawah:")
    print("\n======================================================")
    pilih_menu = [inquirer.List(
            "Menu",
            message="Pilih Menu",
            choices=[
                "1. Tambah Data Servis (Create)",
                "2. Tampilkan Data Servis (Read)",
                "3. Ubah Data Service (Update)",
                "4. Hapus Data Pelanggan (Delete)",
                "5. Keluar"]
            )
        ]
    menu_dipilih = inquirer.prompt(pilih_menu)
    print("======================================================")
    return menu_dipilih["Menu"][0]
    
    
def user_menu():
    print("=========SISTEM SERVIS PERANGKAT ELEKTRONIK===========\n")
    print("Anda Login sebagai User, Silahkan pilih menu dibawah:")
    
    print("\n======================================================")
    

    pilih_menu = [inquirer.List(
            "Menu",
            message="Pilih Menu",
            choices=[
                    "1. Buat Laporan Servis",
                    "2. Tampilkan Data Servis Saya",
                    "3. Keluar"]
            )
        ]
    menu_dipilih = inquirer.prompt(pilih_menu)
    
    return menu_dipilih["Menu"][0]
    

def update_menu():
    os.system("cls || clear")
    print("\n=================================================")
    print("Pilih jenis data servis yang ingin anda ubah: ")
    print("=================================================")
    pilih_menu = [inquirer.List(
            "Menu",
            message="Pilih Menu",
            choices=[
                "1. Nama Pelanggan",
                "2. Jenis Perangkat",
                "3. Jenis Kerusakan",
                "4. Status Perbaikan",
                "5. Biaya Service",]
            )
        ]
    menu_dipilih = inquirer.prompt(pilih_menu)
    
    return menu_dipilih["Menu"][0]

