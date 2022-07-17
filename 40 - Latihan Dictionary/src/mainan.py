# Tipe data collection List, Tuple, Set, Dictionary
# g, G, h, H, '_', "_"

import datetime
import os
import random
import string


mahasiswa_template = {
    "nama" : "nama",
    "nim" : "0000000000",
    "sks_lulus" : 0,
    "lahir" : datetime.datetime(1111,1,11)
}

# empty dictionary
data_mahasiswa = {}

while True:
    os.system("cls")
    print(f"{'SELAMAT DATANG':<20}")
    print(f"{'DATA MAHASISWA':<20}")
    print("-"*20)

    # mengisi data dictionary dari input user
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa["nama"] = input("Nama mahasiswa: ")
    mahasiswa["nim"] = input("NIM mahasiswa: ")
    mahasiswa["sks_lulus"] = int(input("SKS Lulus: "))
    TAHUN_LAHIR = int(input("Tahun Lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan Lahir (1-12): "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir (1-31): "))
    mahasiswa["lahir"] = datetime.datetime(year=TAHUN_LAHIR, month=BULAN_LAHIR, day=TANGGAL_LAHIR)

    # Menghasilkan string alfabet random sebanyak 6 digit
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    print(f"{'KEY':<6} {'Nama':<17} {'NIM':<15} {'SKS':^10} {'Tanggal Lahir':^10}")
    print("-"*65)

    for mahasiswak in data_mahasiswa:
        KEY = mahasiswak

        NAMA = data_mahasiswa[KEY]["nama"]
        NIM = data_mahasiswa[KEY]["nim"]
        SKS = data_mahasiswa[KEY]["sks_lulus"]
        LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")

        print(f"{KEY:<6} {NAMA:<17} {NIM:<15} {SKS:^10} {LAHIR:^10}")

    print("\n")

    is_lanjut = input("Tambahkan data lagi (y/n) ? ")
    if is_lanjut == "y": continue
    else: break

print("Akhir dari program.")
