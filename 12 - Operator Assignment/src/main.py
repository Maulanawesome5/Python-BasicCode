# Operator assignment (penugasan)
# Operator aritmatika dan sama dengan

a = 5 # contoh assignment
print('Nilai a =', a)

# ==================== Assignment aritmatika
a += 1 # artinya 5 + 1 = 6
print('Nilai a += 1 =', a)
a -= 2 # artinya 6 - 2 = 4
print('Nilai a -= 2 =', a)
a *= 5 # artinya 4 * 5 = 20
print('Nilai a *= 5 =', a)
a /= 2 # artinya 20 / 2 = 10
print('Nilai a /= 2 =', a)

# ==================== Modulus dan floor division
b = 10
print('\nNilai b =', b)
b %= 3 # 10 mod 3 = 1
print('Nilai b %= 3 =', b)
b = 10
print('Nilai b =', b)
b //= 3 # 10 floor division 3 = 1
print('Nilai b //= 3 =', b)

# ==================== Eksponensial / pangkat
a = 5
print('\nNilai a =', a)
a **= 3
print('Nilai a **= 3 =', a)

# Operasi bitwise
# OR
c = True
print('\nNilai c =', c)
c |= False
print('Nilai c |= False =', c)
c = False
print('Nilai c =', c)
c |= False
print('Nilai c |= False =', c)

# AND
c = True
print('\nNilai c =', c)
c &= False
print('Nilai c &= False =', c)
c = True
print('Nilai c =', c)
c &= True
print('Nilai c &= True =', c)

# XOR
c = True
print('\nNilai c =', c)
c ^= False
print('Nilai c ^= False =', c)
c = True
print('Nilai c =', c)
c ^= True
print('Nilai c ^= True =', c)

# Shifting / menggeser nilai bit
d = 0b0100
print('\nNilai d =', format(d, '04b'))
d >>= 2 # Shift right
print('Nilai d >>= 2 =', format(d, '04b'))
d <<= 1 # Shift left
print('Nilai d <<= 1 =', format(d, '04b'))
