# Control flow menggunakan break, continue, dan pass
# fungsi control flow untuk :
# break -> berhenti ketika syarat atau aksi tercapai
# continue -> melewati suatu syarat atau aksi tercapai
# pass -> tidak akan dieksekusi (untuk dummy program/function)

angka = 0

while angka < 10:
    angka += 1
    
    if angka == 3:
        print(f"{angka} ditemukan")
    
    elif angka == 4:
        pass # tetap akan melakukan aksi, tujuan pass untuk menguji apakah terdapat error
        print(f"{angka} ditemukan")

    elif angka == 5:
        continue # aksi akan dilewati, tidak menampilkan angka 5
        print(f"{angka} ditemukan")
        # sebenarnya ini tergantung meletakkan posisi continue diatas aksi atau dibawahnya
        # jika continue ditulis dibawah aksi, maka aksi akan dilakukan
        # jika continue ditulis diatas aksi, maka aksi tidak akan dilakukan

    elif angka == 7:
        print("7, 8, 9, 10 telah di break")
        break
    
    print(angka)

print('Loop Selesai')
