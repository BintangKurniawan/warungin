from InquirerPy import inquirer
import os
import tabulate
from datas.dataProducts import load_data_produk
productsfile = "products.txt"

# fungsi ini untuk mencari produk
def cari_produk():
    # variabel ini untuk menyimpan hasil pencarian
    hasil = []

    # variabel ini untuk menyimpan data produk
    data_produk = load_data_produk()
    
    while True:
        os.system('cls')

        # logika ini untuk menampilkan hasil pencarian
        if hasil:
            print(tabulate.tabulate(hasil, headers=["ID", "NAMA", "STOK", "HARGA"], tablefmt="grid", stralign="center", numalign="center"))

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
                if quary.lower() in product[1].lower():
                    hasil.append(product)

            # logika ini untuk menampilkan data yang ditemukan
            if hasil:
                print(tabulate.tabulate(hasil, headers=["ID", "NAMA", "STOK", "HARGA"], tablefmt="grid", stralign="center", numalign="center"))
            else:
                print("Produk tidak ditemukan")
        elif answer == "Keluar":
            break