import os
os.system("cls")

# matakuliah = ["APD", "Kalkulus", "Orsikom"]

# # # menampilkan list
# # print(matakuliah)

# # # menampilkan element dalam list
# # print(matakuliah[0])
# # print(matakuliah[1])
# # print(matakuliah[2])

# # #menampilkan beberapa element list
# # print(matakuliah[1:3])

# # # menampilkan elemn terakhir dalam list
# # print(matakuliah[-1])

# # menambah elemnt list

# matakuliah.append("Matematika")

# print(matakuliah)

# matakuliah.insert(0,"Web")
# print(matakuliah)

# matakuliah[3] = "Basdat"

# print(matakuliah)

# # update list

# study_club = ["Web","Data science","Robotic","Network"]

# print(study_club)

# study_club[3] = "AI"

# print(study_club)



# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)

# # menampilkan list
# for i in matakuliah:
#     print(f"matakuliah: {i}")

# for index,i in enumerate(matakuliah,1):
#     print(f"{index}. matakuliah: {i}")

# # menghapus elemen pada indeks ke-2, yakni "Kalkulus"
# del matakuliah[2]

# print(matakuliah)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)

# # menghapus elemen pada indeks ke-2, yakni "Kalkulus"
# matakuliah.remove("Kalkulus")

# print(matakuliah)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']


# hapus = matakuliah.pop(2)

# print(matakuliah)
# print(f"matkul yang dihapus: {hapus}")

# list = [1,2,3,"Santo"]
# print(list)

# nilai = [1,2,3,4,5,6]

# print(f"element terbesar: {max(list)}")
# print(f"element terkecil: {min(list)}")
# print(f"jumlah element: {sum(list)}")
# print(f"panjang list: {len(list)}")

# hasil = list + nilai
# print(hasil)

# kelas = [
# ["Ridho", "Lian", "Nabil"],
# ["Daffa", "Dante", "Santoso"],
# ["Pernanda", "Riyadi", "Ahnaf"],
# ]

# # menampilkan lian
# print(kelas[0][1])

# # menampilkan santoso
# print(kelas[1][2])

# kelas[0].insert(1,"Rahmat")
# print(kelas)

# # menampilkan element dalam nested list satu persatu
# print("\nNama nama aslab:")
# for i in kelas:
#     for index,j in enumerate(i,1):
#         print(f"{index} aslab: {j}")

# for index,i in enumerate(kelas):
#     if index == 1:
#         for aslab in i:
#             print(aslab)
