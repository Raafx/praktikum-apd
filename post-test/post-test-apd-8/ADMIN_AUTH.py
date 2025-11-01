import os

def admin_regist():
    print("Anda belum memiliki akun Admin, silahkan register akun terlebih dahulu\n")
    username = input("Buat Username Anda: ")
    password = input("Buat Password Anda: ")
    {username:password}
    os.system("cls || clear")
    print("\n----------------REGISTRASI BERHASIL!----------------\n")
    return {username:password}
    
def admin_login(list_akun_admin):
    login_status = False
    print("Silahkan login menggunakan akun Admin")
    while True:
        username = input("Masukan Username Admin: ")
        password = input("Masukan Password Admin: ")
        for username_tersimpan,password_tersimpan in list_akun_admin.items():
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
