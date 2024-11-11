from InquirerPy import inquirer
import os
import tabulate
from products.addProduct import tambah_produk
productsfile = "products.txt"
per_page = 5

def load_data_produk():
    with open(productsfile, "r") as f:
            return [line.strip().split(",") for line in f]

# fungsi ini untuk ngelola produk
def kelola_produk():
    cur_page = 0

    while True:
        os.system('cls')

        data_produk = load_data_produk()
        total_rows = len(data_produk)

        start = cur_page * per_page
        end = start + per_page
        page_data = data_produk[start:end]

        print(tabulate.tabulate(page_data, headers=["ID", "NAMA", "STOK", "HARGA"], tablefmt="grid", stralign="center", numalign="center"))

        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=["Next Page", "Previous Page", "Tambah Produk", "Tambah Stok", "Edit Produk", "Hapus Produk", "Keluar"],
            default="Next Page"
        ).execute()

        if answer == "Next Page" and (cur_page + 1) * per_page < total_rows:
            cur_page += 1
        elif answer == "Previous Page" and cur_page > 0:
            cur_page -= 1
        elif answer == "Tambah Produk":
            tambah_produk()
        elif answer == "Tambah Stok":
            # tambah_stok()
            print("Tambah stok")
        elif answer == "Edit Produk":
            # edit_produk()
            print("Edit produk")
        elif answer == "Hapus Produk":
            # hapus_produk()
            print("Hapus produk")
        elif answer == "Keluar":
            break