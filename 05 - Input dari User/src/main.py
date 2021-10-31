# Mengambil input dari user melalui terminal (cmd)
# menggunakan keyword input()

inputAngka = input("\nMasukkan angka sembarang: ")
print("Anda memasukkan angka -> ", inputAngka)

inputHuruf = input("Masukkan kata/huruf sembarang: ")
print("Anda memasukkan kata/huruf -> ", inputHuruf)

# Memasukkan input melalui terminal menggunakan keyword input()
# secara otomatis tipe datanya akan dikenali sebagai string meskipun memasukkan angka
print("Tipe data dari", inputAngka, "adalah", type(inputAngka))
print("Tipe data dari", inputHuruf, "adalah", type(inputHuruf))
print(25*("="))

# Jika ingin diubah, maka perlu dilakukan casting tipe data
# 1. Casting tipe data angka (int atau float)
inputA = int(input("\nMasukkan angka untuk a: "))
print("Anda memasukkan angka -> ", inputA)
print("Tipe data dari", inputA, "adalah", type(inputA))
inputB = float(input("\nMasukkan angka untuk b: "))
print("Anda memasukkan angka -> ", inputB)
print("Tipe data dari", inputB, "adalah", type(inputB))
print(25*("="))

# 2. Casting tipe data boolean
inputBool = bool(input("\nMasukkan data boolean: "))
print("Nilai boolean ->", inputBool)
print("Tipe data dari", inputBool, "adalah", type(inputBool))
# Jika diisi huruf/kalimat, hasilnya akan true
# Jika diisi angka sembarang meskipun 0, hasilnya akan true
# Jika dibiarkan kosong, hasilnya akan false

# 3. Menggabungkan dua input string
namaDepan = str(input("\nMasukkan nama depan Anda: "))
namaBelakang = str(input("Masukkan nama belakang Anda: "))
namaLengkap = namaDepan + " " + namaBelakang
print("Nama lengkap anda adalah ->", namaLengkap)
print("Tipe data dari", namaLengkap, "adalah", type(namaLengkap))
