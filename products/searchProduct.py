from InquirerPy import inquirer
import os
import tabulate
from data.data import load_data_produk
productsfile = "products.txt"

def cari_produk():
    # variabel ini untuk menyimpan hasil pencarian
    hasil = []
    table_data = [[product["id"], product["Nama"], product["stok"], product["harga"]] for product in hasil]

    # variabel ini untuk menyimpan data produk
    data_produk = load_data_produk()
    
    while True:
        os.system('cls')

        # logika ini untuk menampilkan hasil pencarian
        if hasil:
            print(tabulate.tabulate(table_data, headers=["ID", "NAMA", "STOK", "HARGA"], tablefmt="grid", stralign="center", numalign="center"))

        # variabel ini untuk menampung pilihan user
        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=["Cari Produk", "Keluar"],
            default="Cari Produk"
        ).execute()

        if answer == "Cari Produk":
            quary = input("Masukkan nama produk: ").title()

            # variabel ini untuk mengosongkan variabel hasil sebelumnya
            hasil = []
            for product in data_produk:
                if quary.lower() in product["Nama"].lower():
                    hasil.append(product)

            # logika ini untuk menampilkan data yang ditemukan
            if hasil:
                table_data = [[product["id"], product["Nama"], product["stok"], product["harga"]] for product in hasil]

                print(tabulate.tabulate(table_data, headers=["ID", "NAMA", "STOK", "HARGA"], tablefmt="grid", stralign="center", numalign="center"))
            else:
                print("Produk tidak ditemukan")
        elif answer == "Keluar":
            break