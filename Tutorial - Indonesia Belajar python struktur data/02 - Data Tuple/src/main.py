# Tipe data TUPLE
# tuple termasuk tipe data collection, yaitu dapat menampung berbagai
# macam jenis tipe data
# Baik tuple dan list dapat menampung data yang kembar
# List bersifat mutable / bisa diubah, dihapus, ditambahkan
# Tuple bersifat immutable / tidak bisa diubah atau dihapus

myTuple = (40, 50, 10, 50, 30, 40, 70)
print(f'myTuple = {myTuple}')
yourTuple = ()
print(f'yourTuple = {yourTuple}')

tuple_tanpa_kurung = 20, 30, 40 # tipe data tuple tanpa tanda kurung
print(f'Tuple Tanpa Kurung = {tuple_tanpa_kurung}')
print(f'Tuple Tanpa Kurung = {type(tuple_tanpa_kurung)}')

yourTuple = (54, 7.4, False, 'hello world', [77, 'ini list'])
print(f'yourTuple = {yourTuple}')

# mengakses data didalam tuple menggunakan indexing
print(f'myTuple = {myTuple}')
print(f'Data posisi ketiga myTuple: {myTuple[2]}')

# mengakses data didalam tuple menggunakan slicing index
print(f'Data posisi ketiga myTuple: {myTuple[2:]}') # hanya memasukkan start index

# menggabungkan kedua tuple
joinTuple = myTuple + yourTuple
print(f'Join tuple: {joinTuple}')
