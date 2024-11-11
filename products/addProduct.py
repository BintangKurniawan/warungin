import random
import string
productsfile = "products.txt"

# fungsi ini untuk membuat id random
def randomizer_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
  
def load_data_produk():
    with open(productsfile, "r") as f:
            return [line.strip().split(",") for line in f]

# fungsi ini untuk menambah produk
def tambah_produk():
    data_produk = load_data_produk()

    nama_produk = input("Masukkan nama produk: ").title()
    stok_produk = input("Masukkan stok produk: ")
    harga_produk = input("Masukkan harga produk: ")

    # variabel ini untuk membuat id random
    id_produk = randomizer_id()

    # variabel ini untuk mengecek apakah id produk sudah ada
    existing_ids = {product[0] for product in data_produk}
    while id_produk in existing_ids:
        id_produk = randomizer_id()

    # variabel ini untuk menambahkan produk
    with open(productsfile, "a") as f:
        f.write(f"{id_produk},{nama_produk},{stok_produk},{harga_produk}\n")

    print("Produk berhasil ditambahkan")
