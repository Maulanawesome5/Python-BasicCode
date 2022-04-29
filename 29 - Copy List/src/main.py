# teknik menduplikat list

nama = ['Ucup', 'Otong', 'Dudung', 'Ujang']
print(f"Nama A = {nama}")
nama_lagi = nama # pass by reference, mengganti variabel namun nilainya tetap
print(f"Nama B = {nama_lagi} # Beda variabel")

# mengubah satu nilai dari list
nama[1] = 'Michael'
nama_lagi.sort()
print(f"\nNama A = {nama} # ubah Otong -> Michael")
print(f"Nama B = {nama_lagi} # Sort")

# cek memory address dari kedua variabel
print(f"Alamat memory Nama A = {hex(id(nama))} \n\
Alamat memory Nama B = {hex(id(nama_lagi))}")
print('')

# kesimpulannya meski berubah variabel, namun address tetap sama
# maka jika variabel baru diubah nilainya, variabel utama juga akan berubah
# copy list berguna untuk menempatkan variabel dalam alamat memory yang berbeda
# sehingga tidak akan mempengaruhi nilai variabel sebelumnya

nama_copy = nama.copy() # full duplicate
print(f"Alamat memory Nama A = {hex(id(nama))} \n\
Alamat memory Nama B = {hex(id(nama_lagi))} \n\
Alamat memory Nama C = {hex(id(nama_copy))} # pindah address dengan copy method")

nama_copy[2] = 'Ucuuuuppp'
print(f"\nNama A = {nama} # ubah Otong -> Michael")
print(f"Nama B = {nama_lagi} # sort method")
print(f"Nama C = {nama_copy} # copy method")

