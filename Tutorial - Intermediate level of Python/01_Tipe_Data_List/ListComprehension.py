# Beberapa tombol keyboard saya rusak. copy paste -> g, G, h, H, '_', "_"
# List : Ordered, mutable, allows duplicate number

# membuat list pakai cara biasa
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list)

# membuat list pakai list comprehension
new_list_1 = [i for i in range(1, 10)]
print(new_list_1)

new_list_2 = [i*2 for i in range(1, 10)]  # element list dikali 2
print(new_list_2)

new_list_3 = [i**2 for i in range(1, 10)]  # element_list dipangkat 2
print(new_list_3)

new_list_4 = [i for i in range(1, 10) if i % 2 == 0]  # element_list genap
print(new_list_4)

new_list_5 = [i for i in range(1, 10) if i % 2 != 0]  # element_list ganjil
print(new_list_5)
