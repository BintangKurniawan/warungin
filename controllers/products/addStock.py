from models.productsModel import loadProducts, saveProducts

def tambahStok():
    dataProduk = loadProducts()

    while True:
        idProduk = input("Masukkan ID produk: ").upper()

        produkDitemukan = False
        for product in dataProduk:
            if product["id"] == idProduk:
                stokProduk = int(input("Masukkan stok produk: "))
                product["stok"] = product["stok"] + stokProduk
                produkDitemukan = True
                break

        if produkDitemukan:
            saveProducts(dataProduk)
            print("Stok berhasil ditambahkan")
            break
        else:
            print(f"Error: ID produk '{idProduk}' tidak ditemukan. Coba lagi.")


