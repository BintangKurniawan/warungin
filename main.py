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

# fungsi ini untuk load data produk
def load_data_produk():
    with open(productsfile, "r") as f:
            return [line.strip().split(",") for line in f]


# fungsi ini untuk menghapus produk
def hapus_produk():        
    data_produk = load_data_produk()

    id_produk = input("Masukkan ID produk: ").upper()

    produk_ditemukan = False
    for product in data_produk:
        if product[0] == id_produk:
            produk_ditemukan = True
            break

    if not produk_ditemukan:
        print("Error: ID produk tidak ditemukan.")
        return

    with open(productsfile, "w") as f:
        for product in data_produk:
            if product[0] != id_produk:
                f.write(f"{product[0]},{product[1]},{product[2]},{product[3]}\n")

    print("Produk berhasil dihapus")


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