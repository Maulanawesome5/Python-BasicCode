import os

def app_header():
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40}")

# input user
def app_input():
    lebar = int(input("Input lebar : "))
    panjang = int(input("Input panjang : "))

    return lebar, panjang

# proses hitung
def hitung_luas(panjang, lebar):
    return panjang * lebar

def hitung_keliling(panjang, lebar):
    return 2 * (panjang + lebar)

# tampilkan hasilnya
while(True):
    app_header()

    PANJANG,LEBAR = app_input()
    LUAS = hitung_luas(PANJANG, LEBAR)
    KELILING = hitung_keliling(PANJANG, LEBAR)

    print(f"LUAS = {LUAS} cm2")
    print(f"KELILING = {KELILING} cm")

    is_continue = input("\nLanjutkan aplikasi (y/n) ? ")
    if is_continue == "n":
        break

print("Aplikasi selesai")
