# my keyboard is broken. copy paste -> g, G, h, H, '_', "_"
# Tuple : ordered, immutable, allows duplicate elements
# Karena tuple bersifat immutable / tidak bisa diubah, maka tidak banyak builtin method milik tuple

my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(my_tuple, "Panjang data =", len(my_tuple))

# mekanisme slicing pada tuple

baca_Tuple = my_tuple[0:]
print(baca_Tuple)

baca_Tuple = my_tuple[:5]
print(baca_Tuple)

baca_Tuple = my_tuple[::2]
print(baca_Tuple)

baca_Tuple = my_tuple[::3]
print(baca_Tuple)

baca_Tuple = my_tuple[::-1]  # negative step slicing
print(baca_Tuple)
