from InquirerPy import inquirer
from models.productsModel import loadProducts, saveProducts
def editProduk():
    data_produk = loadProducts()
    while True:
        # Loop khusus untuk memastikan ID produk yang valid dimasukkan
        produk_ditemukan = False
        while not produk_ditemukan:
            id_produk = input("Masukkan ID produk: ").upper().strip()
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
                while True:
                    produk_terpilih["nama"] = input("Masukkan nama produk baru: ").title()

                    if not produk_terpilih["nama"].strip():
                        print("Nama produk tidak boleh kosong. Silakan masukkan kembali nama produk.")
                    elif produk_terpilih["nama"] in [item["nama"] for item in data_produk]:
                        print("Nama produk sudah ada. Silakan masukkan kembali nama produk.")
                    else:
                        print("Nama produk berhasil diedit")
                        break
            elif answer == "Stok":
                while True:
                    try:
                        produk_terpilih["stok"] = int(input("Masukkan stok produk baru: "))

                        if produk_terpilih["stok"] <= 0:
                            print("Stok produk harus bernilai positif. Silakan masukkan kembali stok produk.")
                        else:
                            print("Stok produk berhasil diedit")
                            break
                    except ValueError:
                        print("Stok produk harus berupa angka. Silakan masukkan stok produk yang valid.")
            elif answer == "Harga":
                while True:
                    try:
                        produk_terpilih["harga"] = int(input("Masukkan harga produk baru: "))
                        if produk_terpilih["harga"] <= 0:
                            print("Harga produk harus bernilai positif. Silakan masukkan kembali harga produk.")
                        else:
                            print("Harga produk berhasil diedit")
                            break
                    except ValueError:
                        print("Harga produk harus berupa angka. Silakan masukkan harga produk yang valid.")
                    
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


