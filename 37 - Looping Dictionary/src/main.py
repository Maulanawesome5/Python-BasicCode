# Tipe data collection List, Tuple, Set, Dictionary

# Dictionary
teman_teman = {
    "cup" : "ucup surucup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung",
    "sep" : "asep si kasyep",
    "cuy" : "ucuy surucuy"
}

# cara loop isi tipe data dictionary
kunci = teman_teman.keys()  # ambil key
print(kunci)

nilai = teman_teman.values()  # ambil value
print(nilai)

dict_item = teman_teman.items()  # ambil key dan value
print(dict_item)

for k in kunci:  # Bentuk 1
    print(f"Kunci = {k}")

for k in teman_teman.keys():  # Bentuk 2
    print(f"Nilai = {teman_teman.get(k)}")

for v in teman_teman.values():  # Bentuk 3
    print(f"Values = {v}")

for k,v in teman_teman.items():
    print(f"Key = {k}, Val = {v}")


