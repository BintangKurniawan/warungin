from InquirerPy import inquirer
import os
import tabulate
from controllers.products.searchProduct import cariProduk
from models.productsModel import getPaginatedProducts
perPage = 5

def cekProduk():
    curPage = 0

    while True:
        os.system('cls')
        
        dataProduct, totalPages = getPaginatedProducts(curPage, perPage)
        
        pageData = [[item["id"], item["nama"], item["stok"], item["harga"]] for item in dataProduct]

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