from InquirerPy import inquirer
import os
import tabulate
from controllers.products.addProduct import tambahProduk
from controllers.products.addStock import tambahStok
from controllers.products.editProduct import editProduk
from products.deleteProduct import hapusProduk
from models.productsModel import getPaginatedProducts
perPage = 5

def kelolaProduk():
    curPage = 0

    while True:
        os.system('cls')

        dataProduct, totalPages = getPaginatedProducts(curPage, perPage)

        pageData = [[item["id"], item["nama"], item["stok"], item["harga"]] for item in dataProduct]

        print(tabulate.tabulate(pageData, headers=["ID", "NAMA", "STOK", "HARGA"], tablefmt="grid", stralign="center", numalign="center"))
        print(f"\nHalaman {curPage + 1} dari {totalPages}")
        

        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=["Next Page", "Previous Page", "Tambah Produk", "Tambah Stok", "Edit Produk", "Hapus Produk", "Keluar"],
            default="Next Page"
        ).execute()

        if answer == "Next Page" and curPage < totalPages - 1:
            curPage += 1
        elif answer == "Previous Page" and curPage > 0:
            curPage -= 1
        elif answer == "Tambah Produk":
            tambahProduk()
        elif answer == "Tambah Stok":
            tambahStok()
        elif answer == "Edit Produk":
            editProduk()
        elif answer == "Hapus Produk":
            hapusProduk()
        elif answer == "Keluar":
            break