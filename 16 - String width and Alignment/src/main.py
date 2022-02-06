# width and multiline

# === Data ===
nama = "Faqihza Mukhlish"
umur = 25
tinggiBadan = 170
ukuranSepatu = 45

# Bentuk 1 tanpa alignment dan karakter khusus
dataStr = f"nama: {nama}, umur: {umur}, tinggiBadan: {tinggiBadan}, ukuranSepatu: {ukuranSepatu}"
print("\nBentuk 1 (tanpa alignment)\n", dataStr)

# Bentuk 2 menggunakan karakter khusus
dataStr = f"nama: {nama} \numur: {umur} \ntinggiBadan: {tinggiBadan} \nukuranSepatu: {ukuranSepatu}"
print("\nBentuk 2 (dengan karakter khusus)\n", dataStr)

# Bentuk 3 menggunakan multiline
dataStr = f"""\nBentuk 3 (dengan multiline)
nama: {nama}
umur: {umur}
tinggiBadan: {tinggiBadan}
ukuranSepatu: {ukuranSepatu}
"""
print(dataStr)

# Bentuk 4 menggunakan multiline, teks alignment, karakter khusus
dataStr = f"""\nBentuk 4 (multiline, teks alignment, karakter khusus)
nama: {nama}
nama\t\t: {nama:>5}
umur\t\t: {umur:<0}
tinggiBadan\t: {tinggiBadan:<1}
ukuranSepatu\t: {ukuranSepatu:<1}
"""
print(dataStr)


