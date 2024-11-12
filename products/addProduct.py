import random
import string
import json
from datas.dataProducts import load_data_produk
productsfile = "products.json"

# fungsi ini untuk membuat id random
def randomizer_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

# fungsi ini untuk menambah produk
def tambah_produk():
    data_produk = load_data_produk()

    nama_produk = input("Masukkan nama produk: ").title()
    stok_produk = int(input("Masukkan stok produk: "))
    harga_produk = int(input("Masukkan harga produk: "))

    # variabel ini untuk membuat id random
    id_produk = randomizer_id()

    # variabel ini untuk mengecek apakah id produk sudah ada
    existing_ids = {item["id"] for item in data_produk}
    while id_produk in existing_ids:
        id_produk = randomizer_id()

    new_product = {
        "id": id_produk,
        "Nama": nama_produk,
        "stok": stok_produk,
        "harga": harga_produk
    }

    data_produk.append(new_product)

    with open(productsfile, "w") as f:
        json.dump({"products": data_produk}, f, indent=4)

    print("Produk berhasil ditambahkan")
