# Tipe data collection List, Tuple, Set, Dictionary

# Dictionary
data_dict = {
    "cup" : "ucup surucup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung",
}
print(f"Data dict = {data_dict}")

# panjang dictionary
LENDICT = len(data_dict)
print(f"Panjang data = {LENDICT}")

# mendeteksi key yang dicari ada atau tidak
KEYS = "cup"
CHECK_KEYS = KEYS in data_dict
print(f"Apakah '{KEYS}' ada di dalam data? {CHECK_KEYS}")

# mengakses value dengan get() method
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis", "key tidak ditemukan")) # mencari key dengan default argumen

# update data dictionary
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "asep si kasep"
print(data_dict)

# jika key sudah ada, maka value akan diganti baru
data_dict.update({"cup" : "ucup surucup"})
print(data_dict)

# jika key belum ada, maka akan ditambakan ke data
data_dict.update({"qih" : "faqihza mukhlish"})
print(data_dict)

# menghapus data di dalam dictionary
del data_dict["qih"]
print(data_dict)
