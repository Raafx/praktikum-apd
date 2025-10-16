import os
os.system("cls")

# angka = {1,2,2,3,4,5,5,6,7,9,9,3}

# print(angka)

# buah = {"apel", "jeruk", "mangga", "apel"}
# for i in buah:
#     print(i,end=" ")

# angka = [1,1,2,3,4,4,2,6,7,2,3]
# unik = set(angka)
# print("set:",unik)
# print("list:",angka)

# Daftar_buku = {
#     "Buku1" : "Bumi Manusia",
#     "Buku2" : "Laut Bercerita"
# }

# print(Daftar_buku["Buku1"])

# for i in Daftar_buku:
    
#     print(Daftar_buku[i])


# Biodata = {
# "Nama" : "Ahmad Rafi' Irsyad Nugraha",
# "NIM" : 2509106034,
# "KRS" : ["Kalkulus", "Algoritma Pemrograman Dasar", "Orsikom"],
# "Mahasiswa_Aktif" : True,
# "Social Media" : {
#     "Instagram": "rafisyd",
#     "Github": "Raafx"
#     }
# }

# # for i,j in Biodata.items():
# #     print(i)
# #     print(j)

# print(f"nama saya adalah {Biodata['Nama']}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"nama saya adalah {Biodata.get('Nama')}")


# update

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }

# print("Before Update and Delete")
# print(Film)
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"})
# Film.update({"Upin Ipin":"Comedy"})

# print("\nAfter Update")
# print(Film)

# del Film["The Conjuring"]

# print("\nAfter Delete")
# print(Film)


# Musik = {
#     "The Chainsmoker": ["All we Know", "The Paris"],
#     "Alan Walker": ["Alone", "Lily"],
#     "Neffex": ["Best of Me",['tes','halo'], "Memories"],
#     'Paramore' : ["Misery Business", "Ain't It Fun", 
                  
#                 ['All We Know Is Falling',
                 
#                 ['Here We Go Again', 'My Heart']
                
#                 ],
                
#                 'This Is Why']
# }

# print(Musik['Paramore'][2][1][0])

# a = {1,2,3}
# b = {2,3,4}

# print(a | b)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# print(Nilai)

Musik = {
"The Chainsmoker" : ["All we Know", "The Paris"],
"Alan Walker" : ["Alone", "Lily"],
"Neffex" : ["Best of Me", "Memories"]
}

for i,j in Musik.items():
    nomor = 1
    print(f"Musik milik {i} adalah: ")
    for musik in j:
        print(f"{nomor}. {musik}")
        nomor+=1
    print("")