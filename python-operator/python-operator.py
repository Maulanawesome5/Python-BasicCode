"""
Operator adalah symbol tertentu yang digunakan untuk melakukan
operasi aritmatika maupun logika.
Nilai yang padanya dilakukan operasi disebut operand.
Misalnya adalah 2+3. Disini tanda + adalah operator penjumlahan.
2 dan 3 adalah operand.

Python memiliki sejumlah operator, yaitu :
1.) Operator Aritmatika
2.) Operator Perbandingan
3.) Operator Penugasan
4.) Operator Logika
5.) Operator Bitwise
6.) Operator Identitas
7.) Operator Keanggotaan
"""

"""
1.) Operator Aritmatika
adalah operator yang digunakan untuk melakukan operasi matematika
seperti penjumlahan, pengurangan, perkalian, pembagian, dsb.

"""
a = 30
b = 15
c = 5
x = 2
y = 3
print("### Operator Aritmatika ###")
print("Hasil penjumlahan =", a+b) 	# Menjumlahkan 2 angka
print("Hasil pengurangan =", a-b) 	# Mengurangkan 2 angka
print("Hasil perkalian =", a*b) 	# Mengalikan 2 angka
print("Hasil pembagian =", a/c) 	# Membagi 2 angka
print("Hasil pemangkatan", c**2) 	# Memangkatkan bilangan
print("Hasil pembagian bulat", a//c) # Pembagian bilangan tanpa koma
print("Hasil modulus", x%y) 		# Menghasilkan sisa pembagian 2 angka
print()

"""
2.) Operator Perbandingan
adalah operator yang digunakan untuk membandingkan 2 bilangan.
Hasil perbandingan adalah True atau False, tergantung kondisi
"""
print("### Operator Perbandingan ###")
print("30 lebih besar dari 15 =", a>b)
print("15 lebih kecil dari 30 =", b<a)
print("30 sama dengan 30 =", a==a)
print("30 tidak sama dengan 15 =", a != b)
print("15 lebih besar sama dengan 5 =", b>=c)
print("5 lebih kecil sama dengan 15 =", c<=b)
print()

"""
3.) Operator Penugasan
adalah operator yang digunakan untuk memberi nilai ke variabel
d = 40 adalah contoh operator penugasan yang memberi nilai 40
di kanan ke variabel yang ada di kiri.

Operator '=' menugaskan nilai yang ada di kanan ke operand yang
ada di sebelah kiri. c=a+b menugaskan a+b ke c

Operator '+=' menambahkan operand yang di kanan dengan operand
yang ada di kiri dan hasilnya di tugaskan ke operand yang di kiri.
c += a sama dengan c = c+a

Operator '-=' mengurangi operand yang di kanan dengan operand yang
ada di kiri dan hasilnya di tugaskan ke operand yang di kiri.
c -= a sama dengan c = c+a

Operator '*=' mengalikan operand yang di kanan dengan operand yang
ada di kiri dan hasilnya ditugaskan ke operand yang di kiri.
c *= a sama dengan c = c*a

Operator '/=' membagi operand yang di kanan dengan operand yang
ada di kiri dan hasilnya ditugaskan ke operand yang di kiri.
c /= a sama dengan c = c*a

Operator '**=' memangkatkan operand yang di kanan dengan operand
yang di kiri dan hasilnya ditugaskan ke operand yang di kiri.
c **= a sama dengan c = c**a

Operator '//=' melakukan pembagian bulat operand di kanan terhadap
operand di kiri dan hasilnya disimpan di operand yang di kiri.
c //= a sama dengan c = c//a

Operator '%=' melakukan operasi sisa bagi operand di kanan dengan
operand di kiri dan hasilnya disimpan di operand yang di kiri.
c %= a sama dengan c = c%a
"""
d = 40
e = 6
f = 24
g = d+e
print("### Operator Penugasan ###")
print(f)
print()

"""
4.) Operator Logika
adalah operator yang digunakan untuk melakukan operasi logika.
"""
print("### Operator Logika ###")
print(d < e and e < f) # Hasilnya adalah True jika kedua operand bernilai benar
print(b or c) # Hasilnya adalah True jika salah satu atau kedua operand bernilai benar
print(not(a > 20 and a >= 30)) # Hasilnya adalah True jika operand bernilai salah (kebalikan nilai)
print()

"""
5.) Operator Bitwise
adalah operator yang melakukan operasi bit terhadap operand.
Operand ini beroperasi bit per bit sesuai dengan namanya. Sebagai
misal, angka 2 dalam bit ditulis 10 dalam notasi biner dan angka
7 ditulis 111.
Pada contoh di bawah ini, misalkan x = 10 (0000 1010) dalam biner
dan y = 4 (0000 0100) dalam biner
"""
h = 10
i = 4
j = h+i
k = i + i
print("### Operator Bitwise ###")
print(g&h) 	# Bitwise AND simbol '&'
print(g|h) 	# Bitwise OR simbol '|'
print(~g) 	# Bitwise NOT simbol '~'
print(g^h) 	# Bitwise XOR simbol '^'
print(g>>2) # Bitwise RIGHT SHIFT simbol '>>'
print(g<<2) # Bitwise LEFT SHIFT simbol '<<'
print()

"""
6.) Operator Identitas
adalah operator yang memeriksa apakah dua nilai (atau variabel)
berada pada lokasi memori yang sama
"""
print("### Operator Logika ###")
print(g is True) #True jika kedua operand identik (menunjuk ke objek yang sama)
print(i is not True) #True jika kedua operand tidak identik (tidak merujuk ke objek yang sama)
print()

"""
7.) Operator Keanggotaan
adalah operator yang digunakan untuk memeriksa apakah suatu nilai
atau variabel merupakan anggota atau ditemukan didalam suatu data
(string, list, tuple, set, dictionary).
"""
angka = '1, 2, 3, 4'
print("### Operator Keanggotaan ###")
print('5' in angka) 	# True jika nilai/variabel ditemukan didalam data
print('4' in angka)
print('5' not in angka) # True jika nilai/variabel tidak ada di dalam data
print('4' not in angka)
print()