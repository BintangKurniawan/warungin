from models.productsModel import loadProducts, saveProducts

def tambahStok():
    dataProduk = loadProducts()

    while True:
        idProduk = input("Masukkan ID produk: ").upper()

        produkDitemukan = False
        for product in dataProduk:
            if product["id"] == idProduk:
                while True:
                    try:
                        stokProduk = int(input("Masukkan stok produk: "))
                        if stokProduk < 0 :
                            print("Stok produk harus bernilai postif. Silakan maasukkan lagi stok produk dengan benar.")
                        else:
                            break
                    except ValueError: print("Stok produk harus berupa angka.")

                product["stok"] = product["stok"] + stokProduk
                produkDitemukan = True
                break

        if produkDitemukan:
            saveProducts(dataProduk)
            print("Stok berhasil ditambahkan")
            konfirm = input("Ketik 'y' untuk melanjutkan: ").lower()
            if konfirm == 'y':
                break
        else:
            print(f"Error: ID produk '{idProduk}' tidak ditemukan. Coba lagi.")