# Nested list (list bersarang)

# list
list_biasa = [1, 2, 3, 4]
print(f"List biasa = {list_biasa}")


# Nested list (list bersarang)
# berguna untuk mengolah data yang bersifat serial
a = [1, 2]
b = [3, 4]
list_2_dimensi = [a, b]
print(f"Nested List = {list_2_dimensi}")

# Contoh penggunaan nested list
siswa_1 = ['ucup', 25, 'Laki-Laki']
siswa_2 = ['otong', 26, 'Laki-Laki']
siswa_3 = ['dedeh', 24, 'Perempuan']
list_siswa = [siswa_1,siswa_2,siswa_3]
print(f'Daftar Siswa = {list_siswa}')

# melakukan loop untuk nested list
for siswa in list_siswa:
    print(f"Nama   : {siswa[0]}")
    print(f"Umur   : {siswa[1]}")
    print(f"Kelamin: {siswa[2]}\n")

# nested list tidak bisa dikenakan dengan method copy
# meskipun tidak error, namun nilai dari kedua variabel akan ikut berubah
