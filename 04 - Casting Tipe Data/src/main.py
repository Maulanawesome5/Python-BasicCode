# Casting = mengubah jenis tipe data

# Dari integer menjadi tipe data lainnya
print("\n", 5*"=", "DARI INTEGER")
data_integer = 5
print("Data int =", data_integer, ", type =", type(data_integer))
data_float = float(data_integer)
data_string = str(data_integer)
data_biner = bool(data_integer)
print("Hasil casting =", data_float, ", type =", type(data_float))
print("Hasil casting =", data_string, ", type =", type(data_string))
print("Hasil casting =", data_biner, ", type =", type(data_biner))

# Dari float menjadi tipe data lainnya
print("\n", 5*"=", "DARI FLOAT")
data_float = 5.25
print("Data float =", data_float, ", type =", type(data_float))
data_integer = int(data_float)
data_string = str(data_float)
data_biner = bool(data_float)
print("Hasil casting =", data_integer, ", type =", type(data_integer))
print("Hasil casting =", data_string, ", type =", type(data_string))
print("Hasil casting =", data_biner, ", type =", type(data_biner))

# Dari boolean menjadi tipe data lainnya
print("\n", 5*"=", "DARI BOOLEAN")
# data_biner = 5 > 2 #Hasilnya true, jadi angka 1 dan 1.0
data_biner = 5 < 2 #Hasilnya false, jadi angka 0 dan 0.0
print("Data boolean =", data_biner, ", type =", type(data_biner))
data_integer = int(data_biner)
data_float = float(data_biner)
data_string = str(data_biner)
print("Hasil casting =", data_integer, ", type =", type(data_integer))
print("Hasil casting =", data_float, ", type =", type(data_float))
print("Hasil casting =", data_string, ", type =", type(data_string))

# Dari string menjadi tipe data lainnya
print("\n", 5*"=", "DARI STRING")
data_string = "10" #Tidak bisa memakai string huruf/kata untuk cast ke int & float
print("Data string =", data_string, ", type =", type(data_string))
data_integer = int(data_string)
data_float = float(data_string)
data_biner = bool(data_string)
print("Hasil casting =", data_integer, ", type =", type(data_integer))
print("Hasil casting =", data_float, ", type =", type(data_float))
print("Hasil casting =", data_biner, ", type =", type(data_biner))

# Khusus string ke boolean
print("\n", 5*"=", "STRING -> BOOLEAN")
data_string = "mawar" #True
# data_string = "0" #True
# data_string = "-1" #True
# data_string = "" #False
# a = 10
# b = 5
# data_string = "a < b" # Tidak berhasil di konversi
print("Data string =", data_string, ", type =", type(data_string))
data_biner = bool(data_string)
print("Hasil casting =", data_biner, ", type =", type(data_biner))

#String huruf/kata akan tetap 'true' untuk cast ke boolean
#String angka "0" akan menjadi true
#String angka 1 dan -1, dst. akan menjadi true
#String kosong " " akan menjadi false
#String variabel komparasi hasilnya akan tetap true, tidak berhasil