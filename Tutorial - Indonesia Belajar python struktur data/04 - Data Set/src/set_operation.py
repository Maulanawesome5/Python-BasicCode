set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {5, 6, 7, 8}
print(f"""\nOriginal Data
set1 {set1}
set2 {set2}
set3 {set3}\n""")

# Operasi UNION pada struktur data SET
join_set = set1.union(set2, set3) # setelah di join, data yang kembar akan dipilih satu saja
print(f'Joined set data {join_set}')

# Operasi intersection / irisan pada struktur data SET
intersect_set = set1.intersection(set2, set3)
print(f'Intersection set data {intersect_set}')

# Operasi selisih / difference
diff_set = set1.difference(set2)
print(f'Difference set data {diff_set}')
# Hasilnya {1, 2} artinya nilai yang dikembalikan adalah
# nilai dari set1 yang tidak terdapat pada set2, ini tergantung penulisan set1.difference(set2)
# Jika dibalik set2.difference(set1) maka hasilnya akan berbeda

# Operasi Beda Setangkup / Symmetric Difference
# menampilkan nilai yang tidak kembar/berpotongan antara sekian set data
sim_diff = set1.symmetric_difference(set2)
print(f'Symmetrical Difference set data {sim_diff}')

