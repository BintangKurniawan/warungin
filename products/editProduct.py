from data.data import load_data_produk
import json
productsfile = "products.json"

def edit_produk():
    data_produk = load_data_produk()

    id_produk = input("Masukkan ID produk: ").upper()

    produk_ditemukan = False
    for product in data_produk:
        if product["id"] == id_produk:
            produk_ditemukan = True

            nama_produk = input("Masukkan nama produk baru: ") or product["nama"]
            stok_produk = input("Masukkan stok produk baru: ") or product["stok"]
            harga_produk = input("Masukkan harga produk baru: ") or product["harga"]
        
            product["nama"] = nama_produk
            product["stok"] = stok_produk
            product["harga"] = harga_produk
            break

    if not produk_ditemukan:
        print("Error: ID produk tidak ditemukan.")
        return

    with open(productsfile, "w") as f:
        json.dump(data_produk, f, indent=4)

    print("Produk berhasil diedit")