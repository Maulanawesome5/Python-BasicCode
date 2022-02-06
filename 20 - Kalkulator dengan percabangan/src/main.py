# percabangan if, elif, else

angka1 = float(input('Masukkan angka : '))
aritmatika = input('Operator (+, -, *, /) : ')
angka2 = float(input('Masukkan angka lagi : '))

# Logika percabangan
if aritmatika == "+":
    hasil = angka1 + angka2
    print(f"{angka1} {aritmatika} {angka2} = {hasil}")
elif aritmatika == "-":
    hasil = angka1 - angka2
    print(f"{angka1} {aritmatika} {angka2} = {hasil}")
elif aritmatika == "*" or aritmatika == "x":
    hasil = angka1 * angka2
    print(f"{angka1} {aritmatika} {angka2} = {hasil}")
elif aritmatika == "/" or aritmatika == ":":
    hasil = angka1 / angka2
    print(f"{angka1} {aritmatika} {angka2} = {hasil}")
else:
    print("Sorry, maybe you giving wrong input")

print("Selesai")