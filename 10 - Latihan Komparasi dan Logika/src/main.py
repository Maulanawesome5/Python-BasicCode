# Latihan logika dan komparasi


# Latihan 1
# +++++3-----10+++++
print("Masukkan angka yang bernilai '< 3' atau '> 10'")
inputUser = int(input('input here :'))
# +++++3-----
lessThan = (inputUser < 3)
print("Angka kurang dari 3 =", lessThan)
# -----10+++++
moreThan = (inputUser > 10)
print("Angka lebih dari 10 =", moreThan)
hasil = lessThan or moreThan
print("Hasil masukan angka :", hasil)


# Latihan 2
# -----3+++++10-----
print("\nMasukkan angka yang bernilai '> 3' dan '< 10'")
inputUser = int(input('input here :'))
# -----3+++++
moreThan = (inputUser > 3)
print("Angka lebih dari 3 =", moreThan)
# +++++10-----
lessThan = (inputUser < 10)
print("Angka kurang dari 10 =", lessThan)
hasil = moreThan and lessThan
print("Hasil masukan angka :", hasil)


# Tugas 1 -----0+++++5-----8+++++11-----
print("\nMasukkan angka yang bernilai '> 0' dan '< 5'")
# -----0+++++5
inputUser = int(input("Input here :"))
moreThan = (inputUser > 0)
lessThan = (inputUser < 5)
opsi1 = moreThan and lessThan
print("Angka lebih dari 0 dan kurang dari 5 =", opsi1)
# -----8+++++11-----
print("\nMasukkan angka yang bernilai '> 8' dan '< 11'")
inputUser = int(input("Input here :"))
moreThan = (inputUser > 8)
lessThan = (inputUser < 11)
opsi2 = moreThan and lessThan
print("Angka lebih dari 8 dan kurang dari 11 =", opsi2)
hasil = opsi1 or opsi2
print("Hasil angka ('>0' dan '<5') atau ('>8' dan '<11') =", hasil)


# # Tugas 2 +++++0-----5+++++8-----11+++++
print("\nMasukkan angka yang bernilai '< 0' atau '> 5'")
# +++++0-----5
inputUser = int(input("Input here :"))
moreThan = (inputUser < 0)
lessThan = (inputUser > 5)
opsi1 = moreThan or lessThan
print("Angka kurang dari 0 atau lebih dari 5 =", opsi1)
# +++++8-----11+++++
print("\nMasukkan angka yang bernilai '< 8' atau '> 11'")
inputUser = int(input("Input here :"))
moreThan = (inputUser < 8)
lessThan = (inputUser > 11)
opsi2 = moreThan or lessThan
print("Angka kurang dari 8 atau lebih dari 11 =", opsi2)
hasil = opsi1 and opsi2
print("Hasil angka ('<0' atau '>5') dan ('<8' atau '>11') =", hasil)