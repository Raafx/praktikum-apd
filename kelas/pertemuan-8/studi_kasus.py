import random

karakter = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&"
kata_sandi = ""

panjang_pw = int(input("Masukan panjang password yang anda inginkan: "))

for i in range(panjang_pw):
    kata_sandi += random.choice(karakter)
    
print("Password Anda: ")
print(kata_sandi)