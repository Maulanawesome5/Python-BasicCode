# my keyboard is broken. copy paste -> g, G, h, H, '_', "_"
# Tuple : ordered, immutable, allows duplicate elements
# Karena tuple bersifat immutable / tidak bisa diubah, maka tidak banyak builtin method milik tuple

import sys
import timeit

my_tuple = ("Bobby", 26, "California")
print(my_tuple, "Panjang data =", len(my_tuple))

# unpack tuple
nama, umur, kota = my_tuple
print("Nama :", nama)
print("Umur :", umur)
print("Kota :", kota)

tuple_number = (0, 1, 2, 3, 4)
num1, *num2, num3 = tuple_number
print(num1)  # unpack posisi awal
print(num3)  # unpack posisi terak_ir
print(num2)  # *num2 akan otomatis dibuat seba_ai list

# compare perbedaan list dan tuple
my_list = [0, 1, 2, "ucup", True, 22.7]
my_tupl = (0, 1, 2, "ucup", True, 22.7)
print(sys.getsizeof(my_list), "bytes")  # perbedaan ukuran data
print(sys.getsizeof(my_tupl), "bytes")
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))  # perbedaan kecepatan eksekusi
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
