productsfile = "products.txt"

# fungsi ini untuk load data produk
def load_data_produk():
    with open(productsfile, "r") as f:
            return [line.strip().split(",") for line in f]

# fungsi ini untuk menghapus produk
def hapus_produk():        
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

    with open(productsfile, "w") as f:
        for product in data_produk:
            if product[0] != id_produk:
                f.write(f"{product[0]},{product[1]},{product[2]},{product[3]}\n")

    print("Produk berhasil dihapus")
