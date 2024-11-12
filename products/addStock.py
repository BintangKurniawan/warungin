from datas.dataProducts import load_data_produk
import json
productsfile = "products.json"

# fungsi ini untuk menambah stok
def tambah_stok():
    data_produk = load_data_produk()

    id_produk = input("Masukkan ID produk: ").upper()

    stok_produk = int(input("Masukkan stok produk: "))

    produk_ditemukan = False

    for product in data_produk:
        if product["id"] == id_produk:
            product["stok"] = product["stok"] + stok_produk
            produk_ditemukan = True
            break

    if not produk_ditemukan:
        print("Error: ID produk tidak ditemukan.")
        return


    with open(productsfile, "w") as f:
        json.dump(data_produk, f, indent=4)

    print("Stok berhasil ditambahkan")
