from InquirerPy import inquirer
import os
import tabulate
productsfile = "products.txt"

def load_data_produk():
    with open(productsfile, "r") as f:
            return [line.strip().split(",") for line in f]

per_page = 5

def cari_produk():
    hasil = []

    data_produk = load_data_produk()
    
    while True:
        os.system('cls')

        if hasil:
            print(tabulate.tabulate(hasil, headers=["ID", "NAMA", "STOK", "HARGA"], tablefmt="grid", stralign="center", numalign="center"))

        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=["Cari Produk", "Keluar"],
            default="Cari Produk"
        ).execute()

        if answer == "Cari Produk":
            quary = input("Masukkan nama produk: ")
            hasil = []
            for product in data_produk:
                if quary.lower() in product[1].lower():
                    hasil.append(product)

            if hasil:
                print(tabulate.tabulate(hasil, headers=["ID", "NAMA", "STOK", "HARGA"], tablefmt="grid", stralign="center", numalign="center"))
            else:
                print("Produk tidak ditemukan")
        elif answer == "Keluar":
            break

def tambah_produk():
    data_produk = load_data_produk()

    nama_produk = input("Masukkan nama produk: ")
    stok_produk = input("Masukkan stok produk: ")
    harga_produk = input("Masukkan harga produk: ")

    

    with open(productsfile, "a") as f:
        f.write(f"{len(data_produk) + 1},{nama_produk},{stok_produk},{harga_produk}\n")

    print("Produk berhasil ditambahkan")

def edit_produk():
    data_produk = load_data_produk()

    id_produk = input("Masukkan ID produk: ")

    produk_ditemukan = False
    for product in data_produk:
        if product[0] == id_produk:
            produk_ditemukan = True
            break

    if not produk_ditemukan:
        print("Error: ID produk tidak ditemukan.")
        return

    nama_produk = input("Masukkan nama produk: ")
    stok_produk = input("Masukkan stok produk: ")
    harga_produk = input("Masukkan harga produk: ")

    with open(productsfile, "w") as f:
        for product in data_produk:
            if product[0] == id_produk:
                f.write(f"{id_produk},{nama_produk},{stok_produk},{harga_produk}\n")
            else:
                f.write(f"{product[0]},{product[1]},{product[2]},{product[3]}\n")

    print("Produk berhasil diedit")

def tambah_stok():
    data_produk = load_data_produk()

    id_produk = input("Masukkan ID produk: ")

    produk_ditemukan = False
    for product in data_produk:
        if product[0] == id_produk:
            produk_ditemukan = True
            break

    if not produk_ditemukan:
        print("Error: ID produk tidak ditemukan.")
        return

    stok_produk = input("Masukkan stok produk: ")

    with open(productsfile, "w") as f:
        for product in data_produk:
            if product[0] == id_produk:
                f.write(f"{id_produk},{product[1]},{int(product[2]) + int(stok_produk)},{product[3]}\n")
            else:
                f.write(f"{product[0]},{product[1]},{product[2]},{product[3]}\n")

    print("Stok berhasil ditambahkan")

def cek_produk():
    cur_page = 0

    while True:
        os.system('cls')

        data_produk = load_data_produk()
        
        total_rows = len(data_produk)
        total_pages = (total_rows + per_page - 1)

        start = cur_page * per_page
        end = start + per_page
        page_data = data_produk[start:end]

        print(tabulate.tabulate(page_data, headers=["ID", "NAMA", "STOK", "HARGA"], tablefmt="grid", stralign="center", numalign="center"))

        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=["Next Page", "Previous Page", "Cari Produk", "Keluar"],
            default="Next Page"
        ).execute()

        if answer == "Next Page" and cur_page < total_pages - 1:
            cur_page += 1
        elif answer == "Previous Page" and cur_page > 0:
            cur_page -= 1
        elif answer == "Cari Produk":
            cari_produk()
        elif answer == "Keluar":
            break

def kelola_produk():
    cur_page = 0

    while True:
        os.system('cls')

        data_produk = load_data_produk()
        total_rows = len(data_produk)
        total_pages = (total_rows + per_page - 1)

        start = cur_page * per_page
        end = start + per_page
        page_data = data_produk[start:end]

        print(tabulate.tabulate(page_data, headers=["ID", "NAMA", "STOK", "HARGA"], tablefmt="grid", stralign="center", numalign="center"))

        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=["Next Page", "Previous Page", "Tambah Produk", "Tambah Stok", "Edit Produk", "Hapus Produk", "Keluar"],
            default="Next Page"
        ).execute()

        if answer == "Next Page" and cur_page < total_pages - 1:
            cur_page += 1
        elif answer == "Previous Page" and cur_page > 0:
            cur_page -= 1
        elif answer == "Tambah Produk":
            tambah_produk()
        elif answer == "Tambah Stok":
            tambah_stok()
        elif answer == "Edit Produk":
            edit_produk()
        elif answer == "Hapus Produk":
            print("Hapus produk")
        elif answer == "Keluar":
            break

        

def main():
    
    while True:
        os.system('cls')
        print("========Welcome to Warungin========")

        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=["Cek Produk", "Kelola Produk", "Cek Pendataan Harian", "Cek Pengutang", "Keluar"],
            default="Next Page"
        ).execute()

        if answer == "Cek Produk":
            cek_produk()
        elif answer == "Kelola Produk":
            kelola_produk()
        elif answer == "Cek Pendataan Harian":
            print("Cek pengutang")
        elif answer == "Cek Pengutang":
            print("Cek pengutang")
        elif answer == "Keluar":
            print("Exit")
            break

if __name__ == "__main__":
    main()