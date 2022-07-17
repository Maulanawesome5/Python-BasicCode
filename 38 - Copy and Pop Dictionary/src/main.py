# Tipe data collection List, Tuple, Set, Dictionary
# g, G, h, H, '_', "_"

# Dictionary
teman_teman = {
    "cup" : "ucup surucup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung",
    "sep" : "asep si kasyep",
    "cuy" : "ucuy surucuy"
}
# # Assign biasa variabel teman_teman ke variabel friends
# friends = teman_teman

# Assign pakai method copy
friends = teman_teman.copy()

print(teman_teman)
print(friends)

# Ubah isi data dictionary
teman_teman["cup"] = "ucup si keren"
print(teman_teman)
print(friends)

print("\n\n")  # enter

# Pop method dictionary
sementara = friends.pop("sep")
print(f"Data yang di pop -> {sementara}")
print(friends)

print("\n")  # enter

# Popitem method dictionary
sementara_1 = friends.popitem()
print(f"Data yang di popitem -> {sementara_1}")
print(friends)

