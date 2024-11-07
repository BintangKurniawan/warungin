from InquirerPy import prompt
from InquirerPy import inquirer
import os
import tabulate
productsfile = "products.txt"

with open(productsfile, "r") as f:
        data = [line.strip().split(",") for line in f]


def cari_produk():
    hasil = []
    
    while True:
        os.system('cls')

        if hasil:
            print(tabulate.tabulate(hasil, headers=["ID", "NAMA", "STOK", "HARGA"], tablefmt="grid", stralign="center", numalign="center"))

        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=["Cari Produk", "Keluar"],
            default="Cari Produk"
        ).execute()

        if answer == "Cari Produk":
            quary = input("Masukkan nama produk: ")
            hasil = []
            for product in data:
                if quary.lower() in product[1].lower():
                    hasil.append(product)

            if hasil:
                print(tabulate.tabulate(hasil, headers=["ID", "NAMA", "STOK", "HARGA"], tablefmt="grid", stralign="center", numalign="center"))
            else:
                print("Produk tidak ditemukan")
        elif answer == "Keluar":
            break

def cek_produk():
    per_page = 5
    cur_page =0
    

    total_rows = len(data)
    total_pages = (total_rows + per_page - 1)

    while True:
        os.system('cls')

        start = cur_page * per_page
        end = start + per_page
        page_data = data[start:end]

        print(tabulate.tabulate(page_data, headers=["ID", "NAMA", "STOK", "HARGA"], tablefmt="grid", stralign="center", numalign="center"))

        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=["Next Page", "Previous Page", "Cari Produk", "Keluar"],
            default="Next Page"
        ).execute()

        if answer == "Next Page" and cur_page < total_pages - 1:
            cur_page += 1
        elif answer == "Previous Page" and cur_page > 0:
            cur_page -= 1
        elif answer == "Cari Produk":
            cari_produk()
        elif answer == "Keluar":
            break
        
def main():
    lanjut = True
    while lanjut == True:
        os.system('cls')
        print("========Welcome to Warungin========")

        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=["Cek Produk", "Kelola Produk", "Cek Pendataan Harian", "Cek Pengutang", "Keluar"],
            default="Next Page"
        ).execute()

        if answer == "Cek Produk":
            cek_produk()
        elif answer == "Kelola produk":
            print("Cek produk")
        elif answer == "Cek Pendataan Harian":
            print("Cek pengutang")
        elif answer == "Cek Pengutang":
            print("Cek pengutang")
        elif answer == "Keluar":
            print("Exit")
            lanjut = False

if __name__ == "__main__":
    main()