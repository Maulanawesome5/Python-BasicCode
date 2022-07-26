# Function dengan return

# Function pangkat
def kuadrat(x):
    result = x ** 2
    return result

# karena di dalam function tidak pakai print
# maka untuk menampilkan hasilnya, harus ditampung ke dalam variabel
hasil = kuadrat(2)
print(f"Kuadrat {hasil}")

# atau seperti ini
print(kuadrat(60))

# ini pun juga bisa
hasil = 10 + kuadrat(2)
print(f"10 + Kuadrat(2) = {hasil}")


# Function tambah
def tambah(num1, num2):
    return num1 + num2

jumlah = tambah(10, 40)
print(jumlah)


# Function multi return
def kalkulator(num1, num2):
    addiction = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2

    return addiction, subtraction, multiplication, division

a,s,m,d = kalkulator(9,5)

print(f"Result = {a}")
print(f"Result = {s}")
print(f"Result = {m}")
print(f"Result = {d}")
