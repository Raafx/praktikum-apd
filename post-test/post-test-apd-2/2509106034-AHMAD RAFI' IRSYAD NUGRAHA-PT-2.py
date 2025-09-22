#Membuat List
list_data = [173,70.5,"Rafi",True]

#Menampilkan tipe data masing-masing elemen dalam list sebelum diubah
print("Tipe data sebelum diubah: ")
print(list_data[0],":",type(list_data[0]))
print(list_data[1],":",type(list_data[1]))
print(list_data[2],":",type(list_data[2]))
print(list_data[3],":",type(list_data[3]))

#Menampilkan jumlah data yang bertipe integer dan float sebelum diubah
jumlah_int_dan_float = list_data[0]+list_data[1]
print("jumlah data int dan float:",jumlah_int_dan_float)

#Mengubah tipe data masing-masing element dalam list
list_data[0] = str(list_data[0])
list_data[1] = int(list_data[1])
list_data[2] = list(list_data[2])
list_data[3] = float(list_data[3])

#Menampilkan tipe data masing-masing elemen dalam list  setelah diubah
print("\nTipe data setelah diubah: ")
print(list_data[0],":",type(list_data[0]))
print(list_data[1],":",type(list_data[1]))
print(list_data[2],":",type(list_data[2]))
print(list_data[3],":",type(list_data[3]))


#Menampilkan jumlah data yang bertipe integer dan float sebelum diubah
jumlah_int_dan_float = list_data[1]+list_data[3]
print("jumlah data int dan float:",jumlah_int_dan_float)

    