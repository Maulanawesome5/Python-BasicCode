# tipe data List
# merupakan tipe data collection, atau tipe data yang dapat
# menampung tipe data lainnya

# operasi untuk manipulasi tipe data list
nama = ['Ucup', 'Otong', 'Dudung']
print(nama)

# menggunakan index
nama_ke_0 = nama[0]
print(f'index ke 0 = {nama_ke_0}')

index_negatif = nama[-2]
print(f'index ke -2 = {index_negatif}')

# mengambil info jumlah data dalam list
panjang_list = len(nama)
print(f'Jumlah data di list {panjang_list}')

# menambah item didalam list
print(nama)
nama.insert(1, 'Asep')
print(nama, '# insert Asep')

print(nama)
nama.append('Bagus')
print(nama, '# append Bagus')

# menambah list dengan list
nama_lain = ['Rusdi', 'Kholik', 'Indra']
nama.extend(nama_lain)
print(nama, '# extend method')

# mengubah data dalam list
nama[2] = 'Celeng'
print(nama, '# ubah index ke 2')

# menghapus data dalam list
nama.remove('Bagus')
print(f'{nama} # remove Bagus')

# mengeluarkan salah satu nilai dari dalam list
pop_data = nama.pop()
print(f'{pop_data} # pop method')
print(f'{nama} # pop Indra')





