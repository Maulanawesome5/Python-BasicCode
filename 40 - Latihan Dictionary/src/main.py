# Tipe data collection List, Tuple, Set, Dictionary
# g, G, h, H, '_', "_"

import datetime
import os


mahasiswa_template = {
    "nama" : "nama",
    "nim" : "0000000000",
    "sks_lulus" : 0,
    "lahir" : datetime.datetime(1111,1,11)
}

# empty dictionary
data_mahasiswa = {}

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

print(mahasiswa)
