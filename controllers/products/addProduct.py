from models.productsModel import loadProducts, generateRandomID, saveProducts

def tambahProduk():
    dataProduct = loadProducts()
    while True:
        namaProduk = input("Masukkan nama produk: ").title()

        if not namaProduk.strip():
            print("Nama produk tidak boleh kosong. Silakan masukkan nama produk.")
        elif namaProduk in [item["nama"] for item in dataProduct]:
            print("Nama produk sudah ada. Silakan masukkan nama produk lain.")
        else:
            break

    while True:
        try:
            stokProduk = int(input("Masukkan stok produk: "))
            if stokProduk <= 0 :
                print("Stok produk harus bernilai postif dan tak boleh nol. Silakan maasukkan lagi stok produk dengan benar.")
            else:
                break
        except ValueError: print("Stok produk harus berupa angka.")

    while True:
        try:
            hargaProduk = int(input("Masukkan harga produk: "))
            if hargaProduk <= 0:
                print("Harga produk harus bernilai positif dan tak boleh nol. Silakan masukkan lagi harga produk dengan benar.")
            else:
                break
        except ValueError: print("Harga produk harus berupa angka.")

    existing_ids = {item["id"] for item in dataProduct}

    newProduct = {
        "id": generateRandomID(existing_ids),
        "nama": namaProduk,
        "stok": stokProduk,
        "harga": hargaProduk
    }
    
    dataProduct.append(newProduct)
    
    saveProducts(dataProduct)

    print("Produk berhasil ditambahkan")
