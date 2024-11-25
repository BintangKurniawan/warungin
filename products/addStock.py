from data.data import loadDataProduk
import json
productsfile = "products.json"

def tambahStok():
    dataProduk = loadDataProduk()

    idProduk = input("Masukkan ID produk: ").upper()
    stokProduk = int(input("Masukkan stok produk: "))

    produkDitemukan = False
    for product in dataProduk:
        if product["id"] == idProduk:
            product["stok"] = product["stok"] + stokProduk
            produkDitemukan = True
            break

    if not produkDitemukan:
        print("Error: ID produk tidak ditemukan.")
        return

    with open(productsfile, "w") as f:
        json.dump(dataProduk, f, indent=4)

    print("Stok berhasil ditambahkan")
