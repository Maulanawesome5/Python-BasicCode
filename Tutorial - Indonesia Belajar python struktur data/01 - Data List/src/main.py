# List termasuk collection data type
# dapat digunakan untuk menampung kumpulan nilai / data
# dapat menampung nilai yang kembar

# Perbedaan array dan list, array tidak bisa menampung
# nilai dengan tipe data yang berbeda

# List termasuk dalam sequence data type, artinya bisa diakses
# berdasar urutan nilai didalamnya

myList = [20, 40, 50, 10, 80, 50, 30, 40, 70]
print(f"\nMy List = {myList}")
print(f"data ke 3 My List = {myList[2]}") # mengambil urutan ketiga
print(f"data ke -3 My List = {myList[-3]}") # negatif index

yourList = [] # membuat list kosong
yourList = [54, 7.4, True, 'hello world', [10, 'abc']]
print(f"\nYour List = {yourList}")
print(f"slicing Your List = {yourList[1:4]}") # akses irisan index
print(f"slicing tanpa stop index = {yourList[2:]}") # tanpa stop index
print(f"slicing tanpa start index = {yourList[:2]}") # tanpa start index

# List bersifat mutable, artinya nilai yang ditampung
# dapat diganti, ditambahkan, dan dihapus
yourList[2] = "sudah diganti"
print(f"\nYour List = {yourList}")
yourList.append('Samlekom') # append() untuk menambahkan pada index paling belakang
print(f"Your List = {yourList}")

# Mengeluarkan nilai dari suatu list
var_temp = myList.pop() # pop untuk mengeluarkan suatu nilai paling belakang dari list
print(f"\nMy List = {myList}")
print(f"Temp. Var = {var_temp}")

# Menghapus nilai dari suatu list
myList.remove(50) # remove akan selalu membaca dari index awal. Jika ada nilai kembar, maka yang dihapus duluan adalah yang dari index awal
print(f"\nRemove 50 from My List = {myList}")

# List concatenation (penggabungan antar list)
listJoin = myList + yourList
print(f"\nJoined list = {listJoin}")

