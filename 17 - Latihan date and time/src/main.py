import datetime as dt

# # mengambil waktu hari ini
hari_ini = dt.date.today()
# print(hari_ini)
# print(f"Tanggal {hari_ini} adalah hari {hari_ini:%A}") # %A untuk menampilkan nama hari sesuai tanggal

print("\n", 10*"=")
print('Masukkan tanggal, bulan, dan tahun lahir anda')
input_tanggal = int(input("Tanggal: "))
input_bulan = int(input("Bulan: "))
input_tahun = int(input("Tahun: "))

tanggal_lahir = dt.date(input_tahun, input_bulan, input_tanggal)
print(f"Anda lahir pada hari {tanggal_lahir:%A}, tanggal {tanggal_lahir}")

# Program menghitung umur
umur_hari = hari_ini - tanggal_lahir # umur dalam satuan hari
umur_tahun = umur_hari.days // 365 # umur_hari.days untuk mengambil jumlah hari dibagi 365
print(f"Umur anda saat ini {umur_hari.days} hari ({umur_tahun} tahun).")
