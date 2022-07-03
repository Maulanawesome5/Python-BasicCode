# Latihan list
# data koleksi buku

list_buku = []

while True:
    print("\n\nInput data koleksi buku")
    judul = input("Judul buku: ")
    penulis = input("Nama penulis: ")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)

    print("-"*10, "Koleksi Buku", "-"*10)
    for indeks, buku in enumerate(list_buku):
        print(f"{indeks+1} | {buku[0]} | {buku[1]}")
    print("-"*34)

    lanjutkan = input("Lanjut input (y/n)? : ")
    if lanjutkan == "n": break

print("Selesai. Terima kasih")
