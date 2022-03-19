# Tipe data DICTIONARY
# Dictionary merupakan struktur data dasar dari bahasa Python
# yang terdiri dari pasangan 'key' dan 'value'
# Dictionary termasuk tipe data collection yang dapat menampung berbagai macam
# tipe data lainnya
# Dictionary bersifat mutable, jadi isi datanya bisa ditambah, diubah, dihapus

dataSiswa = {
    'Nama': 'Andri', # Value tipe data string
    'Nilai UTS': 80, # Value tipe data integer
    'Nilai UAS':80, # Mendukung data yang kembar untuk bagian value, sedangkan key tidak boleh kembar
    'Lulus': True, # value tipe data boolean
    'Hobby': ['Selfie', 'Belajar'] # value tipe data list
}
print(f'Data Siswa: {dataSiswa}')

# Dictionary tidak termasuk sequence data type, jadi tidak bisa diakses menggunakan indexing
print('Nama Siswa: ', dataSiswa['Nama'])
print('Hobi Siswa: ', dataSiswa.get('Hobby')) # menggunakan method get()
print('Alamat: ', dataSiswa.get('Alamat', 'Data tidak ditemukan')) # alternative value jika key tidak terdapat dalam dictionary

# Menampilkan key apa saja yang terdapat dalam dictionary
daftar_kunci = dataSiswa.keys()
print(f'Key dalam Data Siswa: {daftar_kunci}\n')

# Key yang terdapat dalam dictionary bersifat iterable, bisa diakses menggunakan looping
for kunci in daftar_kunci:
    print(kunci)


daftar_nilai = dataSiswa.values()
print(f'Value dalam Data Siswa: {daftar_nilai}\n')

# Value yang terdapat dalam dictionary bersifat iterable, bisa diakses menggunakan looping
for nilai in daftar_nilai:
    print(nilai)
print("\n")

# Tutorial sampai menit ke 17:20

# Menangkap pasangan key dan value tipe data dictionary
# menggunakan looping secara bersamaan
daftar_kunci_nilai = dataSiswa.items()
for k, v in daftar_kunci_nilai:
    print(f'{k} = {v}')

# Mengubah nilai pada data dictionary
print("\n", dataSiswa)
dataSiswa['Nilai UTS'] = 70
print(f'Ubah nilai UTS \n{dataSiswa}\n')

# Menambah key & value baru pada data dictionary
print("\n", dataSiswa)
dataSiswa['Gender'] = 'Laki-Laki'
print(f'Tambah K&V Gender \n{dataSiswa}\n')

# Menambah key & value baru menggunakan method update
dataSiswa.update({
        'Nama':'Andrianto',
        'Nilai UTS':100, # Penulisan nama key harus sama, jika berbeda akan membuat key baru
        'Program Studi':'Informatika'
    }
)
print(f'Ubah dengan method update \n{dataSiswa}\n')

# Menghapus / mengeluarkan data dari dalam dictionary
hapusDataSiswa = dataSiswa.pop('Nilai UAS')
print(f'Hapus dengan method pop \n{hapusDataSiswa}')
print(f'Nilai UAS dikeluarkan \n{dataSiswa}\n')

# Concatenation / menggabungkan dua dictionary
dataTambahan = {
    'Bidang Minat' : 'Data Science',
    'Programming' : 'Python'
}
join_dictionary = {**dataSiswa, **dataTambahan} # karakter ** (asterix) menandakan keyword argument
print(f'Concatenation dictionary \n{join_dictionary}\n')

# Tipe data python dictionary sangat erat berkaitan dengan file type JSON (JavaScript Object Notation)
