from datas.dataProducts import load_data_produk
productsfile = "products.txt"

# fungsi ini untuk mengedit produk
def edit_produk():
    data_produk = load_data_produk()

    id_produk = input("Masukkan ID produk: ").upper()

    produk_ditemukan = False
    for product in data_produk:
        if product[0] == id_produk:
            produk_ditemukan = True
            break

    if not produk_ditemukan:
        print("Error: ID produk tidak ditemukan.")
        return

    nama_produk = input("Masukkan nama produk: ")
    stok_produk = input("Masukkan stok produk: ")
    harga_produk = input("Masukkan harga produk: ")

    with open(productsfile, "w") as f:
        for product in data_produk:
            if product[0] == id_produk:
                f.write(f"{id_produk},{nama_produk},{stok_produk},{harga_produk}\n")
            else:
                f.write(f"{product[0]},{product[1]},{product[2]},{product[3]}\n")

    print("Produk berhasil diedit")
