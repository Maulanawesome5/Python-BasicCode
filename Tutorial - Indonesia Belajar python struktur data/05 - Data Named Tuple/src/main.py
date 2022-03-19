# Struktur data NAMED TUPLE
# merupakan pengembangan dari tuple dengan kemampuan akses berdasarkan nama
# Named Tuple termasuk collection data type
from collections import namedtuple

Barang = namedtuple(
    'Barang', # parameter typename
    ['nama_barang', 'harga_jual', 'garansi_vendor'] # parameter field_name
)

# Membuat object berdasarkan named tuple
barang1 = Barang('keyboard', 500, True)
print(f'Barang 1 {barang1}')
# Penulisan argumen bisa dibalik, namun jika di print akan tetap urut
barang2 = Barang(garansi_vendor=False, nama_barang='mouse', harga_jual=150)
print(f'Barang 2 {barang2}\n')

# Named Tuple termasuk sequence data type
# sehingga bisa diakses dengan indexing
# Posisi index akan sesuai dengan awal deklarasi
print(f'Index 0 Barang 2 --> {barang2[0]}')
print(f'Nama Barang 1 --> {barang1.nama_barang} \n\
Harga Barang 1 Rp.{barang1.harga_jual}.000') # Mekanisme akses yang lebih baik dengan nama

# Named Tuple bersifat immutable atau tidak bisa ditambah, dihapus, diperbarui
# barang1.harga_jual = 600 # AttributeError: Can't set attribute
print('\n==Looping isi data named tuple==')
for barang in barang1:
    print(barang) # coba looping menggunakan index
