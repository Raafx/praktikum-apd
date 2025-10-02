# # for i in range(10):
# #     print(i+1)

# # for j in range(1,11,2):
# #     print(j)


# # nama = ["bakil","difthya","anugrah"]

# # for i in nama:
# #     print(i)

# # for i in range(100):
# #     print("Raffi")

# # jawab = "ya"
# # hitung = 0

# # while jawab == "ya":
# #     hitung+=1
# #     jawab = input("ulang lagi?: ")

# # print(f"total jawab ya {hitung}")

# # cuaca = "hujan"

# # while cuaca == "hujan" or cuaca == "Hujan":
# #     print("jangan keluar rumah!")
# #     cuaca = input("Apa cucaca sekarang?")

# # print("Pergi Keluar Rumah")

# # angka = 10

# # while(angka > 1):
# #     print(angka)
# #     angka -= 2

# # for i in range(1,5):
# #     for j in range(1,5):
# #         print(f"{i} x {j} = {i*j}")
# #     print()


# # angka = [2,5,8,12,15,7,20]

# # for i in angka:
# #     if i>10:
# #         print(f"{i} lebih besar dari 10")
# #         break

# # print("program selesai")

# import random

# for i in range(1,11):
#     if i % 2 == 0:
#         continue
#     print(f"angka ditemukan yaitu : {i}")

# print("program selesai")    

# kuadrat = [random.randint(1,100) for i in range(1,100)]

# print(kuadrat)
# jumlah_lulus = 0
# for i in kuadrat:
#     if i < 70:
#         jumlah_lulus+=1

# print(jumlah_lulus)

# print(sum(kuadrat)/len(kuadrat))
    

# for i in range(1,6):
#     for j in range(1,4):
#         print(f"A{j}")



for i in range(1,6):
    print(i*"*")

    
    

a = 5
for i in range(1,6):
    print(a*"*")
    a-=1

a = 5
for i in range(1,6):
    print(a*" "+"*"*(i*2-1))
    a-=1

print()
c = 0
d = 5
for i in range(1,6):
    print(c*" "+"*"*d)
    c+=1
    d-=1




    