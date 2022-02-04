# Memanipulasi string
# Operator dalam bentuk method

nama = "maulana aji w"
print("Nama = " + nama)

# Mengubah semua huruf menjadi uppercase
print("Nama (uppercase) = " + nama.upper())

# Mengubah semua huruf menjadi lowercase
nama = "MAULANA AJI W"
print("Nama = " + nama)
print("Nama (lowercase) = " + nama.lower())

# memeriksa komponen menggunakan is method
# memeriksa lowercase
namaLain = "herman"
cekLower = namaLain.islower() # Hasilnya boolean
print(f"{namaLain} is lowercase ? {cekLower}")
# memeriksa uppercase
cekUpper = namaLain.isupper()
print(f"{namaLain} is uppercase ? {cekUpper}")


""" METHOD IS UNTUK TIPE DATA STRING
isalpha() -> mengecek semuanya huruf
isalnum() -> mengecek kombinasi huruf dan angka
isdecimal() -> mengecek angka saja
isspace() -> mengecek spasi, tab dan newline
istitle() -> mengecek semua kata dimulai dengan huruf kapital
"""

judul = "It Is Okay Not To Be Orkay"
cekJudul = judul.istitle()
print(f"{judul} is title ? {cekJudul}")


# memeriksa komponen menggunakan startswith() dan endswith()
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print(f"Start = {str(cek_start)}")
cek_end = "Sangjangnim Oppa".endswith("Oppak")
print(f"End = {str(cek_end)}")


# Penggabungan komponen dengan method join() dan split()
pisah = ['aku', 'sayang', 'kamu'] # tipe data list
# join method
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = ' ehm '.join(pisah)
print(gabung)

# split method
gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm')) # hasilnya dikonversi ke tipe data list


# Alokasi karakter -> rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print(f"'{kanan}'")

kiri = "kiri".ljust(10)
print(f"'{kiri}'")

tengah = "tengah".center(10)
print(f"'{tengah}'")

# Method untuk menghapus alokasi karakter -> strip()
tengah = "tengah".strip()
print(f"'{tengah}'")
