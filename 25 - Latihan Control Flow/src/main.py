# Latihan control flow
# menggambar segitiga di console

sisi = int(input("Masukkan jumlah panjang sisi: "))

# menggunakan for looping
# dummy variable
count = 1
for i in range(sisi):
    print("*" * count)
    count += 1
print("\n")

# menggunakan while looping
count = 1
while True:
    print("*" * count)
    count += 1
    if count > sisi:
        break
print("\n")

# loop sisi yang ganjil
count = 1
while True:
    if (count % 2): # jika count dimodulus 2
        # akan di print jika ganjil
        print("*" * count)
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue
    # akan break jika count melebihi sisi
    if count > sisi:
        break
print("\n")

# Membuat segitiga sama kaki dengan loop
count = 1
spasi = int(sisi / 2)
while True:
    if (count % 2): # Jika count di modulus 2 menjadi 1
        print(" " * spasi, "*" * count)
        spasi -= 1 # decrement jumlah spasi
        count += 1 # increment loop
    else: # Jika count dimodulus 2 tidak menjadi 0, maka lanjutkan increment
        count += 1
        continue
    if count > sisi: # untuk membatasi agar loop tidak melebihi jumlah
        break
print("\n")


