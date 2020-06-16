# Membuat list database mobil sederhana

ListMobil = ["Avanza", "Inova", "Toyota", "Kijang"]
ListTahun = ["2015", "2016", "2017"]
ListWarna = ["Hitam", "Silver", "Putih"]

print(ListMobil) # Menampilkan list mobil
print(ListTahun) # Menampilkan list tahun
print(ListWarna) # Menampilkan list warna
print()
# Tampilkan list mobil avanza tahun 2015 berwarna hitam
print(ListMobil[0], ListTahun[0], ListWarna[0])
print()
# Tampilkan list mobil inova tahun 2017 berwarna hitam
print(ListMobil[1], ListTahun[2], ListWarna[0])
print()
# Tampilkan list mobil acak dengan Negative Indexing
print(ListMobil[-2], ListTahun[-1], ListWarna[0])
print(ListMobil[-3], ListTahun[-2], ListWarna[-3])
print()
# Menambahkan data baru dalam list
ListMobil.append("Pajero")
print(ListMobil)
ListTahun.append("2018")
ListWarna.append("Merah")
print(ListTahun)
print(ListWarna)
ListMobil.insert(5, "Suzuki")
ListMobil.insert(6, "BMW")
ListMobil.insert(7, "Honda")
print(ListMobil)
ListTahun.insert(4, "2019")
ListTahun.insert(5, "2020")
ListWarna.insert(4, "Biru Metalic")
ListWarna.insert(5, "Coklat")
ListWarna.insert(6, "Hijau")
print(ListTahun)
print(ListWarna)
print()
# Tampilkan list mobil acak dengan Positive Indexing
print(ListMobil[4], ListTahun[2], ListWarna[0])
print(ListMobil[5], ListTahun[4], ListWarna[2])
print(ListMobil[7], ListTahun[3], ListWarna[5])
print(ListMobil[6], ListTahun[0], ListWarna[1])
print()
# Menambahkan lalu menghapus item baru
ListMobil.insert(8, "Daihatsu")
ListMobil.insert(9, "Pagani")
ListMobil.insert(10, "Buggati")
print(ListMobil)
ListMobil.remove("Pagani")
print(ListMobil)
ListMobil.pop()
print(ListMobil)
print()
# Menerapkan fungsi loop
for grade in ListMobil:
	print(grade)
print()
for grade in ListWarna:
	print(grade)
print()