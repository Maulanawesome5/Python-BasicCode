# my keyboard is broken. copy paste -> g, G, h, H, '_', "_"
# Tuple : ordered, immutable, allows duplicate elements
# Karena tuple bersifat immutable / tidak bisa diubah, maka tidak banyak builtin method milik tuple

my_tuple = ('a', 'p', 'p', 'l', 'e')

print(my_tuple)
print(len(my_tuple))  # 5
print(my_tuple.count('p'))  # 2
print(my_tuple.index('e'))  # 4

# konversi tuple ke list
my_list = list(my_tuple)
print(my_list)
