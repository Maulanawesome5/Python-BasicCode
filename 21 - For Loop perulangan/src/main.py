# perulangan for loop

# ==========
angka = [0, 1, 2, 3, 4] # tipe data list
print(angka)

for i in angka: # i adalah variabel scope local
    # i akan menampung nilai dari variabel angka
    print(f"i ==> {i}")

# ==========
rangeAngka = range(5) # menggunakan range
print(rangeAngka)

for i in rangeAngka:
    print(f"i ==> {i}")

# ==========
rangeNumber = range(1, 10) # start limit 1, stop limit 10
print(rangeNumber)

for i in rangeNumber:
    print(f"i ==> {i}")

