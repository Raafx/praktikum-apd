# #Fungsi dan Modular Programing

import os

os.system("cls || clear")

def perkenalan(nama):
    print(f"Hallo aku {nama}")



def kali(s):
    x= s*s
    return x

c = 5


kali(c)

nama = "Rafi"

perkenalan(nama)

def luasPersegiPanjang(panjang,lebar):
    luas = panjang*lebar
    return luas

luas_persegi_panjang = luasPersegiPanjang(20,5)
print(f"luas persegi panjang adalah: {luas_persegi_panjang}")



nama = "Rafi"

def biodata():
    nama = "Ahmad"

print(nama)


def faktorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * faktorial(n-1)
    
print(faktorial(5))