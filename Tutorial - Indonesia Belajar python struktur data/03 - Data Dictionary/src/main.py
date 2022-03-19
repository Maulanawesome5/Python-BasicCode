# Tipe data DICTIONARY
# Dictionary merupakan struktur data dasar dari bahasa Python
# yang terdiri dari pasangan 'key' dan 'value'
# Dictionary termasuk tipe data collection yang dapat menampung berbagai macam
# tipe data lainnya

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
print(f'Key dalam Data Siswa: {daftar_kunci}')

# Key yang terdapat dalam dictionary bersifat iterable, bisa diakses menggunakan looping
for kunci in daftar_kunci:
    print(kunci)


daftar_nilai = dataSiswa.values()
print(f'Value dalam Data Siswa: {daftar_nilai}')

# Value yang terdapat dalam dictionary bersifat iterable, bisa diakses menggunakan looping
for nilai in daftar_nilai:
    print(nilai)

# Tutorial sampai menit ke 17:20
