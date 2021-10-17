print("Selamat, program python berjalan di VSCode")
print("Menampilkan teks ke console")
print("Kalimat ini nyambung")
print("Kalimat ini", "tetap nyambung")
print("Kalimat ini", "juga", "tetap nyambung")

# Single line comment
"""
    Multiline comment
    untuk menambahkan deskripsi yang panjang untuk
    penjelasan dari suatu sintaks python
"""

# (Enter) antar baris program tidak akan di execute
print() #Kosong, untuk menambah 'enter' di console

# Menampilkan teks beserta nilai variabel ke console
a = 10
b = 1000
print("Angka a =", a)
print("Angka b =", b)

""" Menguji kecepatan running program
antara file python yang interpreted
dengan file python yang sudah di compile.
Gunakan library 'time' untuk membuat fungsi timer 
dan akan saya uji menggunakan looping """

import time
start_waktu = time.time()

while a < b:
    a += 10
    print(a)

print("Akhir loop")
print(time.time() - start_waktu, "detik")

# Kesimpulan :
# Hasil kecepatan file interpreted dan compile selalu berubah