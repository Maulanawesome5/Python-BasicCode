# my keyboard is broken. copy paste -> g, G, h, H, '_', "_"
# Tuple : ordered, immutable, allows duplicate elements

my_tuple = ("Max", 28, "Boston")
print(my_tuple)
print(type(my_tuple))

your_tuple = "Marry", 27, "Chicago"
print(your_tuple)
print(type(your_tuple))

another_tuple = tuple(["Bobby", 24, "California"])  # konversi list menjadi tuple
print(another_tuple)
print(type(another_tuple), "\n\n")

# cara akses tipe data tuple
item0 = my_tuple[0]
print("Item at index 0 :", item0)
item1 = my_tuple[1]
print("Item at index 1 :", item1)

# akses item di tuple pakai loop
for nilai in another_tuple:
    print(nilai)

# periksa item di dalam tuple
item2 = "Max"
if item2 in my_tuple:
    print(item2, "ADA di dalam tuple")
else:
    print(item2, "TIDAK ADA di dalam tuple")

item3 = "Chicago"
if item3 in your_tuple:
    print(item3, "ADA")
else:
    print(item3, "TIDAK ADA")

