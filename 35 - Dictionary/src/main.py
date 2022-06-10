# Tipe data collection List, Tuple, Set, Dictionary

# Dictionary == Associative array
# indentifier -> key
data_dictionary = {
    'nama' : 'maulana',
    'gender' : 'pria',
    'umur' : 23,
    'menikah' : False,
    'tinggi' : 1.6,
    'hobi' : ["membaca", "stream YouTube", "tidur"]
}

print(f"Data Dictionary : {type(data_dictionary)}")
print(f"Data Dictionary : {data_dictionary}")

print("\n")

print(f"Nama : {data_dictionary['nama']}")
print(f"Saya {data_dictionary['gender']}, berusia {data_dictionary['umur']} tahun.")
print(f"Sudah menikah ? {data_dictionary['menikah']}")
print(f"Hobi saya {data_dictionary['hobi']}")
