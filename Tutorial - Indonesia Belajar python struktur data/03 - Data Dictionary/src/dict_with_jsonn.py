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
print(f'Data Siswa: \n{dataSiswa}\n')

# dataSiswa yang sudah menjadi file json, akan dibaca kembali oleh python
# dengan cara berikut ini
with open('data_siswa.json', 'r') as fileku: # r adalah mode read
    myDictionary = json.load(fileku)
    print(f'external file json \n{myDictionary}\n')


