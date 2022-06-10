# Looping list
print("For Loop")
kumpulan_angka = [4, 3, 2, 5, 6, 1]
for angka in kumpulan_angka:
    print(f'Angka = {angka}')

peserta = ["ucup", "otong", "dadang", "dudung"]
for nama in peserta: print(f'Peserta = {nama}')

# for loop dan range
print("\nFor Loop dan Range")
kumpulan_nomor = [10, 5, 4, 2, 6, 5]
panjang_list = len(kumpulan_nomor)
for i in range(panjang_list): print(f'Nomor = {kumpulan_nomor[i]}')

# while
print("\nWhile Loop")
kumpulan_angka = [10, 5, 4, 2, 6, 5]
panjang_list = len(kumpulan_angka)
i = 0
while i < panjang_list:
    print(f'Angka = {kumpulan_angka[i]}')
    i += 1

# list comprehension
print("\nList Comprehension")
data = ["ucup", 1, 2, 3, "otong"]
[print(f"Data = {i}") for i in data]

list_angka = [10, 5, 4, 2, 6, 5]
angka_kuadrat = [i**2 for i in list_angka]
print("List Angka Kuadrat = ", angka_kuadrat)

# Enumerate
print("\nEnumerate")
data_list = ["ucup", 1, 2, 3, "otong"]
for index, data in enumerate(data_list):
    print(f"index = {index}, data = {data}")
