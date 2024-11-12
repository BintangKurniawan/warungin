from datas.dataProducts import load_data_produk
import json
productsfile = "products.json"

# fungsi ini untuk menghapus produk
def hapus_produk():        
    data_produk = load_data_produk()

    id_produk = input("Masukkan ID produk: ").upper()

    original_length = len(data_produk)

    data_produk = [product for product in data_produk if product["id"] != id_produk]

    if len(data_produk) == original_length:
        print("Error: ID produk tidak ditemukan.")
        return

    with open(productsfile, "w") as f:
        json.dump(data_produk, f, indent=4)

    print("Produk berhasil dihapus")
