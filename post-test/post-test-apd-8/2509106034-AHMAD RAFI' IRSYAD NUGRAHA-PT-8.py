import os
import inquirer

from CREATE import user_create,create_data
from READ import user_read,read_data
from UPDATE import update_data
from DELETE import delete_data

from DISPLAY_MENU import crud_menu,user_menu

from ADMIN_AUTH import admin_login,admin_regist
from USER_AUTH import user_login,user_regist

from DISPLAY_MENU import login_menu,user_menu,crud_menu


os.system("cls || clear") 


list_akun_admin = {}
list_akun_user = {}
data_pelanggan = {}

# FUNGSI TANPA PARAMETER 1
def crud_operation():
    while True:
        
        menu_dipilih = crud_menu()
        if menu_dipilih == "1":
            create_data(data_pelanggan)
            
        elif menu_dipilih == "2":
            read_data(data_pelanggan)
            
        elif menu_dipilih == "3":
            update_data(data_pelanggan)
            
        elif menu_dipilih == "4":
            delete_data(data_pelanggan)
            
        elif menu_dipilih == "5":
            break
        
        else:
            print("\nPilihan tidak dikenali, mohon input pilihan antara angka 1 sampai 5!\n")
            continue
        
# FUNGSI TANPA PARAMETER 2
        
def user_operation():
    while True:
        

        pilih_menu = user_menu()
        
        if pilih_menu == "1":
            user_create(data_pelanggan)
            
        elif pilih_menu == "2":
            user_read(data_pelanggan)
            
        elif pilih_menu == "3":
            break
        else:
            os.system("cls || clear")
            print("Pilihan Tidak dikenali!, silahkan ulangi input menu")
            continue


    
    

if __name__ == "__main__":
    while True:
        pilih_login = login_menu()
        if pilih_login == "1":
            os.system("cls || clear")
            if len(list_akun_admin) == 0:
                list_akun_admin.update(admin_regist())
            else:
                admin_login(list_akun_admin)

            crud_operation()



        elif pilih_login == "2":
            os.system("cls || clear") 

            if len(list_akun_user) == 0:
                print("Anda belum memiliki akun, silahkan register akun terlebih dahulu\n")
                list_akun_user.update(user_regist())

            else:
                user_login(list_akun_user)

            user_operation()

        elif pilih_login == "3":
            break
        else:
            print("Input tidak dikenal, silahkan ulangi login")
            continue

    print("\n=============PROGRAM BERAKHIR=============")



