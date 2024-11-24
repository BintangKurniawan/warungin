from InquirerPy import inquirer
import os
import tabulate
from products.searchProduct import cariProduk
from data.data import loadDataProduk
perPage = 5

def cek_produk():
    curPage = 0

    while True:
        os.system('cls')

        dataProduk = loadDataProduk()
        dataProduk = list(reversed(dataProduk))
        # variabel ini untuk menghitung total rows
        totalRows = len(dataProduk)
        totalPages = (totalRows + perPage - 1) // perPage 

        start = curPage * perPage
        end = start + perPage
        pageData = [[item["id"], item["nama"], item["stok"], item["harga"]] for item in dataProduk[start:end]]

        print(tabulate.tabulate(pageData, headers=["ID", "NAMA", "STOK", "HARGA"], tablefmt="grid", stralign="center", numalign="center"))
        print(f"\nHalaman {curPage + 1} dari {totalPages}")

        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=["Next Page", "Previous Page", "Cari Produk", "Keluar"],
            default="Next Page"
        ).execute()

        if answer == "Next Page" and curPage < totalPages - 1:
            curPage += 1
        elif answer == "Previous Page" and curPage > 0:
            curPage -= 1
        elif answer == "Cari Produk":
            cariProduk()
        elif answer == "Keluar":
            break