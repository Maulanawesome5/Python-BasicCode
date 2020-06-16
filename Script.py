# Syntax python operator sebagai percobaan untuk perhitungan sederhana
# Semoga gue gak lupa caranya :v

x = 30
y = 20
z = 60

# Python Operator
# Syntax penambahan
print("Ini hasil penambahan :")
print(x + y)
print(y + x)
print(x + z)
print(y + z)
print()

# Syntax pengurangan
print("Ini hasil pengurangan :")
print(x - y)
print(y - x)
print(x - z)
print(y - z)
print()

# Syntax perkalian
print("Ini hasil perkalian :")
print(x * y)
print(y * x)
print(x * z)
print(y * z)
print()

# Syntax pembagian
print("Ini hasil pembagian :")
print(x / y)
print(y / x)
print(z / x)
print(z / y)
print(z / z)
print()

# Syntax modulus
print("Ini hasil modulus :")
print(x % y)
print(y % x)
print(x % z)
print(y % z)

# Python comparison operator
print(x == y == z)  # sama dengan
print(x != y != z)  # tidak sama dengan
print(x > y > z)    # lebih dari
print(y < x < z)    # kurang dari
print(x >= y >= z)  # lebih dari sama dengan
print(y <= x <= z)  # kurang dari sama dengan
print()

# Python Logical Operator
print(x < 50 and x < 60) # Return "True" if both statements are true
print(x < 50 or x < 10) # Return "True" if one of the statements is true
print(not(x > 20 and x < 50)) # Return "False" because not is used to reverse the result
print()



x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) # Return "True" because Z is the same object as X
print(x is y) # Return "False" because X is not the same object as Y, even if the have the same content
print(x == y) # to demonstrate the difference beetween "is" and "==" : this comparison returns True because x is equal to y

