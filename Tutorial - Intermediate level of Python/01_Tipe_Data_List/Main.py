# Beberapa tombol keyboard saya rusak. copy paste -> g, G, h, H, '_', "_"
# List : Ordered, mutable, allows duplicate number

my_list = ["banana", "cherry", "apple"]  # list berisi data str
your_list = list()  # list kosong

print(my_list)
print(your_list)

# akses isi list pakai index system
item0 = my_list[0]
item1 = my_list[1]
print("Item on index 0 : ", item0)
print("Item on index 1 : ", item1)

# akses list pakai loop
for isi_data in my_list:
    print("Isi data :", isi_data)

# periksa isi list
item2 = "banana"
if item2 in my_list:
    print(item2, "ADA di dalam list")
else:
    print(item2, "TIDAK ADA di dalam list")

item3 = "lemon"
if item3 in my_list:
    print(item3, "ADA di dalam list")
else:
    print(item3, "TIDAK ADA di dalam list")

# periksa berapa jumlah data dalam list
jumlah_list = len(my_list)
print("Jumlah data dalam list :", jumlah_list, "\n\n")


# method / function bawaan untuk tipe data list

my_list.append("lemon")
print(my_list)

my_list.insert(1, "strawberry")
print(my_list)

item4 = my_list.pop()  # pop() itu dikeluarkan dari list, tapi data masih ada
print(my_list)
print("Pop data ->", item4)

item5 = my_list.remove("cherry")  # remove() itu benar-benar dihapus, setelahnya akan None
print("Remove data ->", item5)
print(my_list, "\n\n")

number_list = [0, 1, 3, 5, 2, -1, -5, -10]
print(number_list)

number_list.sort()
print(number_list)
