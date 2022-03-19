# Struktur data SET python
# SET merupakan implementasi himpunan bilangan matematika
# SET termasuk collection data type, yang bisa menampung berbagai macam tipe data didalamnya
# SET tidak termasuk sequence data type, sehingga tidak berlaku indexing

originalData = '{33, 66, 22, 66, 99, 22, 77, 33, 22}'
print(f"\nOriginal data {originalData}")
mySet = {33, 66, 22, 66, 99, 22, 77, 33, 22}
print(f"Struktur Data SET {mySet} --> {type(mySet)}\n")
# Struktur data SET tidak mendukung data yang kembar, sehingga akan dipilih satu saja
# Kelebihan dari SET adalah karena tidak bisa menerima data kembar
# maka nilai didalamnya akan selalu unik
# Kekurangan SET adalah tidak bisa membuat empty set, karena akan ambigu dengan dictionary
# sebab notasi penulisan dibuka dan ditutup dengan tanda {}

yourSet = {99, 6.6, False, 'Happy Birthday'}
print(f"Koleksi Data SET {yourSet} --> {type(yourSet)}")

# Jika membuat empty set, gunakan penulisan seperti berikut
set_kosong = set()
print(f"Empty SET {set_kosong} --> {type(set_kosong)}")

# mengubah data LIST menjadi SET
originalData = [10, 20, 10, 20, 10, 20]
print(f"\nOriginal data {originalData} --> {type(originalData)}")
indexingSet = set([10, 20, 10, 20, 10, 20])
print(f"LIST to SET {indexingSet} --> {type(indexingSet)}\n")

# struktur data SET bersifat mutable, artinya bisa ditambah, diubah, dihapus
# add data
mySet = {33, 66, 22, 66, 99, 22, 77, 33, 22}
print(f"\nOriginal data {mySet} --> {type(mySet)}")
mySet.add('python')
print(f"Add data {mySet} --> {type(mySet)}")

# remove data
mySet.remove(77)
print(f"Remove data {mySet} --> {type(mySet)}")

# discard data, lebih aman daripada remove.
# jika data yang ingin di hilangkan tidak tersedia, tidak menampilkan error
mySet.discard(99)
print(f"Discard data {mySet} --> {type(mySet)}")

