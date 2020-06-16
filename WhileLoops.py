# Python memiliki dua primitive perintah loop
# while loops
# for loops

# Statement while loop
i = 1
while i < 6:
    print(i)
    i += 1
print()

# The break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print()

# The continue Statement
a = 0
while a < 6:
    a += 1
    if a == 3:
        continue
    print(a)
print()

#The else statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer than 6")
print()

# Statement For loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
print()

# Looping through a String
for x in "banana":
    print(x)
print()

# The break statement
for x in fruits:
    print(x)
    if x == "banana":
        break
print()

# The continue statement
for x in fruits:
    if x == "banana":
        continue
    print(x)
print()

# The range() function
for x in range(6):
    print(x)
print()
for x in range(2, 6):
    print(x)
print()
for x in range(2, 30, 3):
    print(x)
print()

# Else in for loop
for x in range(6):
    print(x)
else:
    print("Selesai cuk !")
print()

# Nested Loops
adj = ["red", "fresh", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
print()

# The pass statement
for x in [0, 1, 2]:
    pass