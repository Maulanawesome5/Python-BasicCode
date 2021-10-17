# Belajar tentang tipe data yang ada di dalam bahasa pemrograman python.

# Tipe data integer (bilangan bulat) / angka yang tidak berkoma
bil_integer = 10
print("Tipe data dari ", bil_integer, " adalah = ", type(bil_integer))

# Tipe data float (bilangan desimal) / angka yang memiliki koma
bil_float = 12.5
print("Tipe data dari ", bil_float, " adalah = ", type(bil_float))

# Tipe data string (karakter huruf)
kata_string = "Mawar"
print("Tipe data dari ", kata_string, " adalah = ", type(kata_string))

# Tipe data boolean (true / false)
data_boolean = True
print("Tipe data dari ", data_boolean, " adalah = ", type(data_boolean))
print()

##### Tipe data khusus #####

# Tipe data bilangan kompleks
bil_complex = complex(5,6)
print("Tipe data dari ", bil_complex, " adalah = ", type(bil_complex))

# Tipe data dari bahasa C++
from ctypes import c_double 
bil_c_double = c_double(10.5)
print("Tipe data dari ", bil_c_double, " adalah = ", type(bil_c_double))