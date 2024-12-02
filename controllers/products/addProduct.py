from models.productsModel import loadProducts, generateRandomID, saveProducts

def tambahProduk():
    dataProduct = loadProducts()

    namaProduk = input("Masukkan nama produk: ").title()
    stokProduk = int(input("Masukkan stok produk: "))
    hargaProduk = int(input("Masukkan harga produk: "))

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
