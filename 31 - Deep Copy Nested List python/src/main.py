# Nested list (list bersarang)
# berguna untuk mengolah data yang bersifat serial
# nested list tidak bisa dikenakan dengan method copy
# meskipun tidak error, namun nilai dari kedua variabel akan ikut berubah

from copy import deepcopy # menggunakan function


a = [1, 2]
b = [3, 4]
list_2_dimensi = [a, b]
print(f"List AB = {list_2_dimensi}")

# ambil nilai dengan index untuk nested list
print(f'List AB[0] = {list_2_dimensi[0]}')
print(f'List AB[0][1] = {list_2_dimensi[0][1]}')

copy_list_2_dimensi = list_2_dimensi.copy()
print(f"\nList AB_copy = {copy_list_2_dimensi} # copy method")
print(f"Memory address List AB {hex(id(list_2_dimensi))} \n\
Memory address List AB_copy {hex(id(copy_list_2_dimensi))} # copy method")

# karena address kedua variabel berbeda 
# sekarang kita cek address dari member list (isinya)
print(f"\nAddress member {list_2_dimensi[0]} = {hex(id(list_2_dimensi[0]))}")
print(f"Address member {copy_list_2_dimensi[0]} = {hex(id(copy_list_2_dimensi[0]))} # copy method")
print()

# coba ditambahkan nilai baru
list_2_dimensi = [a, b, 10] # Menambahkan nilai 10
print(f"List AB = {list_2_dimensi} # Menambah nilai 10 \n\
List AB_copy = {copy_list_2_dimensi} # Menambah nilai 10")

list_2_dimensi[1][0] = 5
print(f"List AB[1][0] = {list_2_dimensi} # Mengubah jadi 5")

copy_list_2_dimensi[0][1] = 9
print(f"List AB_copy[0][1] = {copy_list_2_dimensi} # Mengubah jadi 9")

# ================= DEEPCOPY =================
# sekarang mari coba dengan menggunakan deep copy method, lakukan import
list_with_deepcopy = deepcopy(list_2_dimensi)






