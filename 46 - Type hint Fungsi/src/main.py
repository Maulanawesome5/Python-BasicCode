# Type Hint dari function
# Berguna untuk menetapkan tipe data dari parameter/argument
# supaya return atau kegunaan dari function sesuai

# Function 1
#          ini type hints
def pangkat(nomor:int):
    output = nomor ** 2
    return output

print(pangkat(10))
print(pangkat(True))

# Function 2
#           ini type hints
def display_str(nama:str) -> str:  # supaya hasil return akan bertipe str
    print(f"Halo {nama}")

display_str("Ucup")
ucup = display_str("surucup")
ucup


# Function 3
def say_hello(nama:str) -> str:
    return nama

result = say_hello("Ayu")
print(f"Halo {result}")
print(type(result))  # akan bertipe string


# Function 4
# Pakai type hints dan default value
def luas_kotak(panjang:int = 1, lebar:int = 1) -> int:
    '''Function untuk menghitung luas kotak'''
    return panjang * lebar

luasKotaks = luas_kotak(200, 80)
print(f"Luas kotak = {luasKotaks} cm\n", type(luasKotaks))