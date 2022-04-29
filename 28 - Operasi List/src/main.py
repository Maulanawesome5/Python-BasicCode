# operasi yang dapat dikenakan pada list
angka = [1, 2, 3, 4, 5, 3, 2, 0, 9, 7, 6, 8, 9, 0, 1, 2]
print(f'List Angka = {angka}')

# mengurutkan angka didalam list
angka.sort()
print(f'List Angka = {angka} # sort method')

# mencari angka yang kembar dalam list
print(f'\nAngka kembar dalam list \
0 = {angka.count(0)}, 1 = {angka.count(1)}, 2 = {angka.count(2)}, 3 = {angka.count(3)} dengan method count')

nama = ['Ucup', 'Otong', 'Dudung', 'Ujang']
print('Nama =', nama)
print(f'Otong berada di index ke {nama.index("Otong")} \nUjang berada di index ke {nama.index("Ujang")}')

# mengurutkan list berisi string
nama.sort()
print(f'\nSort Nama = {nama}')
print(f'Otong berada di index ke {nama.index("Otong")} \nUjang berada di index ke {nama.index("Ujang")}')

nama.reverse() # membalik urutan
print(f'\nReverse Nama = {nama}')
print(f'Otong berada di index ke {nama.index("Otong")} \nUjang berada di index ke {nama.index("Ujang")}')
