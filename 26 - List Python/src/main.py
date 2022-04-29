# tipe data List
# merupakan tipe data collection, atau tipe data yang dapat
# menampung tipe data lainnya

# List angka
data_angka = [1, 2, 3]
print(data_angka)

# List string
data_string = ['ucup', 'otong', 'odah']
print(data_string)

# List boolean
data_bool = [True, False, True, False]
print(data_bool)

# List campuran
data_mix = [1, 'abcd', 2, 'efgh', True, 'ijkl', False]
print(data_mix)

# cara lain membuat list
data_range = range(0, 10, 2) # range(start, stop, step)
print(data_range)
data_list_range = list(data_range) # mengcasting range() menjadi list
print(data_list_range)

# membuat list menggunakan looping (list comprehension)
list_with_for = [i for i in range(0,10)]
print(list_with_for)

list_with_for = [i**2 for i in range(0,10)] # hasil loop dipangkatkan
print(list_with_for, '# dipangkatkan')

# membuat list dengan for dan if
list_with_loop_if = [i for i in range(0,10) if i != 5]
print(list_with_loop_if, '# if i != 5')

list_with_loop_if = [i for i in range(0,10) if i %2 == 0]
print(list_with_loop_if, '# angka genap')

list_with_loop_if = [i for i in range(0,10) if i %2 != 0]
print(list_with_loop_if, '# angka ganjil')

list_with_loop_if = [i**2 for i in range(0,10) if i %2 != 0]
print(list_with_loop_if, '# angka ganjil dipangkatkan')





