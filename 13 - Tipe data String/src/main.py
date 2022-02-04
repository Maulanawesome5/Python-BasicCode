data = "ini adalah string"
print(data, type(data))
data = 'menggunakan single quote'
print(data, type(data))
data = "menggunakan double quote"
print(data, type(data))

# 1. Bentuk string dengan quote
print("'Halo apa kabar?'")
print('"Halo apa kabar?"')
print("Ini adalah hari jum'at")

# 2. Penggunaan tanda backslash untuk format string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')
# Backslash untuk menulis direktori folder
print("C:\\Users\\Lenovo\\Desktop")
# Backslash untuk indentasi tab
print("ucup \t\totong, semakin jauh")
# Backslash untuk newline
print("Baris pertama. \nBaris kedua.") # LF -> Line Feed
print("Baris pertama. \rBaris kedua.") # CR -> Carriage Return
print("Baris pertama. \r\nBaris kedua.") # CRLF -> Carriage Return Line Feed

# 3. String literal atau raw string
print(r"C:\Users\new folder\teknik2021") # Menggunakan r

# Multiline literal string dan raw string
print(r"""
Tugas : Mengaduk beton
Deadline : 3 Hari
Kumpulkan di C:\Users\new folder\teknik2021\betonB
""")

