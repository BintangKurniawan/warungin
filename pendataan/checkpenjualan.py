from InquirerPy import inquirer
import os
import tabulate
from pendataan.searchpenjualan import cari_penjualan
penjualanfile = "pendataan.txt"
per_page = 5


def load_data_penjualan():
    with open(penjualanfile, "r") as f:
            return [line.strip().split(",") for line in f]
# fungsi ini untuk ngecek penjualan
def cek_penjualan():
    cur_page = 0

    while True:
        os.system('cls')

        data_penjualan = load_data_penjualan()
        
        # variabel ini untuk menghitung total rows
        total_rows = len(data_penjualan)
        total_pages = (total_rows + per_page - 1)

        start = cur_page * per_page
        end = start + per_page
        page_data = data_penjualan[start:end]

        print(tabulate.tabulate(page_data, headers=["ID", "NAMA", "STOK", "HARGA"], tablefmt="grid", stralign="center", numalign="center"))

        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=["Next Page", "Previous Page", "Cari Penjualan", "Keluar"],
            default="Next Page"
        ).execute()

        if answer == "Next Page" and cur_page < total_pages - 1:
            cur_page += 1
        elif answer == "Previous Page" and cur_page > 0:
            cur_page -= 1
        elif answer == "Cari Penjualan":
            cari_penjualan()
        elif answer == "Keluar":
            break