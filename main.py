from InquirerPy import inquirer
import os
import tabulate
import random
import string
from products.checkProduct import cek_produk
from products.manageProduct import kelola_produk
productsfile = "products.txt"
per_page = 5

# fungsi ini untuk membuat id random
def randomizer_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

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