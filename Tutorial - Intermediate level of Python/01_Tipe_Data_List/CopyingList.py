# Beberapa tombol keyboard saya rusak. copy paste -> g, G, h, H, '_', "_"
# List : Ordered, mutable, allows duplicate number

my_list = ["banana", "cherry", "apple"]
print(my_list)


# mekanisme copy pada list
temp_list = my_list
print(temp_list, "\n\n")

temp_list.append("pineapple")
print(temp_list)
print(my_list, "\n\n")

new_temp_list = my_list.copy()  # pakai copy method
new_temp_list.remove("pineapple")
new_temp_list.append("strawberry")
new_temp_list.insert(1, "starfruit")
print(new_temp_list)
print(my_list)
