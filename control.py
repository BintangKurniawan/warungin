from InquirerPy import inquirer
import os
from products.checkProduct import cekProduk
from products.manageProduct import kelolaProduk
from pendataan.checkpenjualan import cekPenjualan
from pengutang.checkpengutang import kelola_pengutang
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
            cekProduk()
        elif answer == "Kelola Produk":
            kelolaProduk()
        elif answer == "Cek Pendataan Harian":
            cekPenjualan()
        elif answer == "Cek Pengutang":
            kelola_pengutang()
        elif answer == "Keluar":
            print("Exit")
            break