# Function dengan default argument

# Function 1
#                 ini default
def say_hello(nama = "tampan"):
    print(f"Hallo {nama}")

say_hello("Ucup")
say_hello()

# Function 2
#                   satu default saja
def say_hello(nama, pesan = "Apa kabar ?"):
    print(f"Halo {nama}, {pesan}")

say_hello("Ayu", "I Love You")
say_hello("Indah")

# Function 3
def pangkat(num, eksponen):
    result = num ** eksponen
    return result

print(pangkat(9,2))

result = pangkat(eksponen = 4, num = 2)  # dimasukkan ke variabel
print(result)

# Function 4
def kalkulator(num1 = 1, num2 = 2, num3 = 3, num4 = 4):
    result = num1 + num2 + num3 + num4
    return result

print(kalkulator())
print(kalkulator(num3=15))
