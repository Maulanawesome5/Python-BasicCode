# Tipe data collection List, Tuple, Set, Dictionary
# g, G, h, H, '_', "_"

import datetime


# Multi keys dan Nesting dictionary
# Multi keys dictionary
mahasiswa1 = {
    "nama" : "Ucup Surucup",
    "nim" : "1914311001",
    "sks_lulus" : 130,
    "beasiswa" : False,
    "lahir" : datetime.datetime(2001,4,10)
}

mahasiswa2 = {
    "nama" : "Otong Surotong",
    "nim" : "1914311002",
    "sks_lulus" : 140,
    "beasiswa" : True,
    "lahir" : datetime.datetime(2002,10,10)
}

mahasiswa3 = {
    "nama" : "Asep Salep",
    "nim" : "1914311003",
    "sks_lulus" : 130,
    "beasiswa" : False,
    "lahir" : datetime.datetime(2000,2,29)
}

# Nesting dictionary
data_Mahasiswa = {
    "MAH001" : mahasiswa1,
    "MAH002" : mahasiswa2,
    "MAH003" : mahasiswa3
}

print(f"{'KEY':<6} {'Nama':<17} {'NIM':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*65)

for mahasiswa in data_Mahasiswa:
    KEY = mahasiswa

    NAMA = data_Mahasiswa[KEY]['nama']
    NIM = data_Mahasiswa[KEY]['nim']
    SKS = data_Mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_Mahasiswa[KEY]['beasiswa']
    LAHIR = data_Mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<17} {NIM:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")

