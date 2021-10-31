# Operator bitwise

# variabel
a = 9
b = 5
print("Angka", a, "binary", format(a, '08b'))
print("Angka", b, "binary", format(b, '08b'))

# bitwise OR
a = 9
b = 5
c = a | b
print(15*"=", "OR")
print(a, 'OR', b, '=', c, "binary", format(c, '08b'))

# bitwise AND
a = 9
b = 5
c = a & b
print(15*"=", "AND")
print(a, 'AND', b, '=', c, "binary", format(c, '08b'))

# bitwise XOR
a = 9
b = 5
c = a ^ b
print(15*"=", "XOR")
print(a, 'XOR', b, '=', c, "binary", format(c, '08b'))

# bitwise NOT
c = ~a
print(15*"=", "NOT")
print('NOT', a, '=', c, "binary", format(c, '08b'))

# bitwise Shift Right
a = 9
c = a >> 1
print(15*"=", "Shift Right")
print(a, "binary", format(a, '08b'))
print(">>")
print(c, "binary", format(c, '08b'))

# bitwise Shift Left
a = 9
c = a << 1
print(15*"=", "Shift Left")
print(a, "binary", format(a, '08b'))
print("<<")
print(c, "binary", format(c, '08b'))