from InquirerPy import inquirer
from models.productsModel import loadProducts, saveProducts
def editProduk():
    from control import control
    data_produk = loadProducts()
    while True:
        # Loop khusus untuk memastikan ID produk yang valid dimasukkan
        produk_ditemukan = False
        while not produk_ditemukan:
            id_produk = input("Masukkan ID produk: ").upper()
            for product in data_produk:
                if product["id"] == id_produk:
                    produk_ditemukan = True
                    produk_terpilih = product
                    break
            if not produk_ditemukan:
                print("Error: ID produk tidak ditemukan. Silakan coba lagi.")

        while True:
            answer = inquirer.select(
                message="Pilih salah satu yang akan diedit:",
                choices=["Nama", "Stok", "Harga", "Keluar"],
                default="Nama"
            ).execute()
            
            # Proses pengeditan sesuai pilihan
            if answer == "Nama":
                produk_terpilih["nama"] = input("Masukkan nama produk baru: ").title()
                print("Nama produk berhasil diedit")
            elif answer == "Stok":
                produk_terpilih["stok"] = input("Masukkan stok produk baru: ") 
                print("Stok produk berhasil diedit")
            elif answer == "Harga":
                produk_terpilih["harga"] = input("Masukkan harga produk baru: ") 
                print("Harga produk berhasil diedit")
            elif answer == "Keluar":
                return 
            
            edit_lagi = inquirer.select(
                message="Apakah ingin mengedit lagi?",
                choices=["Ya", "Tidak"],
                default="Ya"
            ).execute()
            
            if edit_lagi == "Tidak":
                # Simpan perubahan ke file JSON dan keluar dari loop pengeditan
                saveProducts(data_produk)
                print("Produk berhasil disimpan.")
                return


