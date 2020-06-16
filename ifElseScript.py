# Equals (sama dengan): a == b
# Not Equals (tidak sama dengan): a != b
# Less than (kurang dari): a < b
# Less than or equal to (Kurang dari atau sama dengan): a <= b
# Greater than (lebih besar): a > b
# Greater tha or equal to (lebih besar atau sama dengan): a >= b

# Statement if
a = 33
b = 200
if b > a:
    print("B Lebih besar dari A")

# Statement Else If (Elif)
c = 33
d = 33
if d > c:
    print("D lebih besar dari C")
elif c == d:
    print("C dan D sama besar")

# Statement Else
e = 200
f = 33
if f > e:
    print("F lebih besar dari E")
elif e == f:
    print("E dan F sama besar")
else:
    print("E lebih besar dari F")

# Statement singkat If
if a > b: print("A lebih besar dari B")

# Statement singkat If ... Else
print("A") if a > b else print("B")

# Statement singkat dengan tiga kondisi
print("C") if c > d else print("=") if c == d else print("D")

# Statement And
g = 200
h = 33
i = 500
if g > h and i > g:
    print("Kedua kondisi adalah Benar")

# Statement Or
if g > h or g > i:
    print("Satu kondisi saja yang Benar")

# Statement Nested If (If bersarang)
x = 41
y = 15
if x > 10:
    print("X Diatas 10,")
    if x > 20:
        print("dan X juga datas 20.")
    else:
        print("Tapi X tidak diatas 20.")
if y > 10:
    print("Y Diatas 10,")
    if y > 20:
        print("dan Y juga diatas 20.")
    else:
        print("Tapi Y tidak diatas 20.")