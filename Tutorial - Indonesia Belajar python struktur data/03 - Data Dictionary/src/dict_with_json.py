# Tipe data DICTIONARY
# Dictionary merupakan struktur data dasar dari bahasa Python
# yang terdiri dari pasangan 'key' dan 'value'
# Dictionary termasuk tipe data collection yang dapat menampung berbagai macam
# tipe data lainnya
# Dictionary bersifat mutable, jadi isi datanya bisa ditambah, diubah, dihapus
import json

dataSiswa = {
    'Nama': 'Andri', # Value tipe data string
    'Nilai UTS': 80, # Value tipe data integer
    'Nilai UAS':80, # Mendukung data yang kembar untuk bagian value, sedangkan key tidak boleh kembar
    'Lulus': True, # value tipe data boolean
    'Hobby': ['Selfie', 'Belajar'] # value tipe data list
}
print(f'Data Siswa: {dataSiswa}')

# Tipe data python dictionary sangat erat berkaitan dengan file type JSON (JavaScript Object Notation)
# dataSiswa akan di export menjadi file json
with open('data_siswa.json', 'w') as fileku: # w artinya mode write
    json.dump(dataSiswa, fileku) # parameter dump(dictionary, file pointer)

