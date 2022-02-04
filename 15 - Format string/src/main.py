# Menggunakan format string untuk
# mengkonstruksi suatu tipe data string

# untuk data string
youtuber = "Kelas Terbuka"
print(f"Subscribe to {youtuber}") # format string diawali f""

# untuk data boolean
perbandingan = (5 >= 10)
print(f"Apakah 5 >= 10 ? {perbandingan}")

# untuk data angka
angka = 20.5
print(f"Angka = {angka}")

# untuk menulis nominal uang
uang = 200000
print(f"Jumlah uang Rp. {uang:,}") # otomatis mendeteksi 3 digit dan diberi koma

# menulis bilangan desimal
angkaDesimal = 2005.54321
format_str = f"Desimal = {angkaDesimal:.3f}"
print(format_str)

# menampilkan leading zero
angkaDesimal = 2005.54321
format_str = f"Desimal = {angkaDesimal:010.3f}"
print(format_str)

# menampilkan tanda positif dan negatif
numMin = -10 # integer
numPlus = 3.14159265359 # float
print(f"Angka negatif {numMin:+d}")
print(f"Angka positif {numPlus:+.2f}") # 2f untuk menampilkan 2 angka dibelakang koma (untuk float)

# menulis format persen
persentase = 0.045
print(f"Angka persen {persentase:.2%}")

# melakukan operasi aritmatika dalam placeholder {}
harga = 10000
jumlah = 5
print(f"Harga total belanja Rp. {harga*jumlah:,}")

# memformat bilangan biner, octal, hexadesimal
angka = 255
print(f"""
Bilangan biner = {bin(angka)}
Bilangan octal = {oct(angka)}
Bilangan hexadecimal = {hex(angka)}
""")

