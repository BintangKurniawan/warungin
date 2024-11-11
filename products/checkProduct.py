from InquirerPy import inquirer
import os
import tabulate
from products.searchProduct import cari_produk
from datas.dataProducts import load_data_produk
productsfile = "products.txt"
per_page = 5

# fungsi ini untuk ngecek produk
def cek_produk():
    cur_page = 0

    while True:
        os.system('cls')

        data_produk = load_data_produk()
        
        # variabel ini untuk menghitung total rows
        total_rows = len(data_produk)

        start = cur_page * per_page
        end = start + per_page
        page_data = data_produk[start:end]

        print(tabulate.tabulate(page_data, headers=["ID", "NAMA", "STOK", "HARGA"], tablefmt="grid", stralign="center", numalign="center"))

        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=["Next Page", "Previous Page", "Cari Produk", "Keluar"],
            default="Next Page"
        ).execute()

        if answer == "Next Page" and (cur_page + 1) * per_page < total_rows:
            cur_page += 1
        elif answer == "Previous Page" and cur_page > 0:
            cur_page -= 1
        elif answer == "Cari Produk":
            cari_produk()
        elif answer == "Keluar":
            break