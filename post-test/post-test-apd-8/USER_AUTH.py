import os
import inquirer


def user_regist(list_akun_user):
    print("Anda belum memiliki akun, silahkan register akun terlebih dahulu\n")
    username = input("Buat Username Anda: ")
    password = input("Buat Password Anda: ")
    os.system("cls || clear")
    print("\n----------------REGISTRASI BERHASIL!----------------\n")
    return {username:password}
    
def user_login(list_akun_user):
    login_status = False
    
    
    pilih_menu_login = [inquirer.List(
        "Menu Login",
        message="Silahkan login dengan akun yang telah ada atau buat akun baru",
        choices=[
            "1. Buat Akun",
            "2. Login dengan akun yang ada"
        ]
    )]
    
    menu_dipilih = inquirer.prompt(pilih_menu_login)["Menu Login"][0]
    
    if menu_dipilih == "1":
        user_regist()
    else:
    
        while True:
            username = input("Masukan Username Anda: ")
            password = input("Masukan Password Anda: ")
            for username_tersimpan,password_tersimpan in list_akun_user.items():
                if username == username_tersimpan and password == password_tersimpan:
                    os.system("cls || clear")
                    print("\n--------------Login Berhasil!--------------\n")
                    login_status = True
                    break
                
            if login_status:
                break
            else:
                os.system("cls || clear")
                print("\n=====Username dan Password tidak sesuai, silahkan ulangi lagi=====")
                continue
