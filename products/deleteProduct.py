from data.data import load_data_produk
import json
productsfile = "products.json"

def hapus_produk():        
    data_produk = load_data_produk()

    id_produk = input("Masukkan ID produk: ").upper()

    original_length = len(data_produk)

    # menulis ulang semua data produk kecuali produk yang ingin dihapus
    data_produk = [product for product in data_produk if product["id"] != id_produk]

    if len(data_produk) == original_length:
        print("Error: ID produk tidak ditemukan.")
        return

    with open(productsfile, "w") as f:
        json.dump(data_produk, f, indent=4)

    print("Produk berhasil dihapus")
