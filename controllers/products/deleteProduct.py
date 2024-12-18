from models.productsModel import loadProducts, saveProducts

def hapusProduk():        
    data_produk = loadProducts()
    while True:
        
        id_produk = input("Masukkan ID produk: ").upper()

        original_length = len(data_produk)

        # menulis ulang semua data produk kecuali produk yang ingin dihapus
        data_produk = [product for product in data_produk if product["id"] != id_produk]

        if len(data_produk) == original_length:
            print("Error: ID produk tidak ditemukan.")
            pilihan = input("apakah anda ingin menghapus produk lain?")
            if pilihan == "y":
                continue
            else:
                print("Penghapusan dibatalkan")
                return
        else:

            saveProducts(data_produk)

            print("Produk berhasil dihapus")
            break
