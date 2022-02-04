# Memanipulasi string

# 1. Menyambung string (concatenation)
youtuber = "Kelas Terbuka"
print("Subscribe channel YouTube ", youtuber)
print("Subscribe channel YouTube {}".format(youtuber))
print(f"Subscribe channel YouTube {youtuber}\n")

namaDepan = "Edward"
namaTengah = "John"
namaBelakang = "Phillip"
namaLengkap = namaDepan + namaTengah + namaBelakang
print(namaLengkap)
namaLengkap = namaDepan + " " + namaTengah + " " + namaBelakang
print(namaLengkap)


# 2. Menghitung panjang string
panjang = len(namaLengkap)
print(f"Panjang nama {namaLengkap} adalah ", panjang)


# 3. Memeriksa komponen dalam string
cariHuruf = "h"
status = cariHuruf in namaLengkap
print(f"\nHuruf {cariHuruf} ada dalam {namaLengkap} = {status}")

cariHuruf = "E"
status = cariHuruf not in namaLengkap
print(f"Huruf {cariHuruf} tidak ada dalam {namaLengkap} = {status}")


# 4. Manipulasi string
# Repeat string
print("\n", 10*"=")

# Mencari huruf berdasarkan index dalam string
print("Index ke-0 :", namaLengkap[0])
print("Index ke-6 :", namaLengkap[7])
print("Index ke-[0:9] :", namaLengkap[0:11]) # start index : stop index
print("Index ke-[0::1] :", namaLengkap[0::1]) # start index : stop index : step
print("Index ke-[0::2] :", namaLengkap[0::2]) # start index : stop index : step
print("\n")

# ASCII code dari huruf
kode_ascii = ord("z")
print("ASCII code untuk z = " + str(kode_ascii))
huruf = 113
print(f"Char dari kode {huruf} = " + chr(huruf))


# 5. Method yang digunakan untuk data string
nama = "otong surotong pararotong"
jumlah = nama.count("o")
print(f'Jumlah huruf "o" dalam {nama} adalah ' + str(jumlah))
