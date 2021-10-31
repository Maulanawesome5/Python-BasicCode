# Operasi Logika Boolean / Aljabar Boolean
# not, or, and, xor

print(10*"=", "NOT")
a = True
c = not a
print('A =', a)
print('A (not) C =', c)

#==================================================
print()
print(10*"=", "OR ")
a = False
b = False
c = a or b
print(a, '(OR)', b, '=', c)

a = False
b = True
c = a or b
print(a, '(OR)', b, '=', c)

a = True
b = False
c = a or b
print(a, '(OR)', b, '=', c)

a = True
b = True
c = a or b
print(a, '(OR)', b, '=', c)

#==================================================
print()
print(10*"=", "AND")
a = False
b = False
c = a and b
print(a, '(AND)', b, '=', c)

a = False
b = True
c = a and b
print(a, '(AND)', b, '=', c)

a = True
b = False
c = a and b
print(a, '(AND)', b, '=', c)

a = True
b = True
c = a and b
print(a, '(AND)', b, '=', c)

#==================================================
print()
print(10*"=", "XOR")
a = False
b = False
c = a ^ b
print(a, '(XOR)', b, '=', c)

a = False
b = True
c = a ^ b
print(a, '(XOR)', b, '=', c)

a = True
b = False
c = a ^ b
print(a, '(XOR)', b, '=', c)

a = True
b = True
c = a ^ b
print(a, '(XOR)', b, '=', c)