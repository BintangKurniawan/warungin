from InquirerPy import inquirer
import os
from products.checkProduct import cek_produk
from products.manageProduct import kelola_produk
from pendataan.checkpenjualan import cek_penjualan

def control():
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
            cek_penjualan()
        elif answer == "Cek Pengutang":
            print("Cek pengutang")
        elif answer == "Keluar":
            print("Exit")
            break