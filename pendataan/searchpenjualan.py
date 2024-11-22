from InquirerPy import inquirer
import os
import tabulate

penjualanfile = "pendataan.txt"

# fungsi ini untuk load data penjualan
def load_data_penjualan():
    with open(penjualanfile, "r") as f:
            return [line.strip().split(",") for line in f]

# fungsi ini untuk mencari penjualan
def cari_penjualan():
    # variabel ini untuk menyimpan hasil pencarian
    hasil = []

    # variabel ini untuk menyimpan data penjualan
    data_penjualan = load_data_penjualan()
    
    while True:
        os.system('cls')

        # logika ini untuk menampilkan hasil pencarian
        if hasil:
            print(tabulate.tabulate(hasil, headers=["ID", "NAMA", "STOK", "HARGA"], tablefmt="grid", stralign="center", numalign="center"))

        # variabel ini untuk menampung pilihan user
        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=["Cari Penjualan", "Keluar"],
            default="Cari Penjualan"
        ).execute()

        if answer == "Cari penjualan":
            quary = input("Masukkan nama produk: ").title()

            # variabel ini untuk mengosongkan variabel hasil sebelumnya
            hasil = []
            for product in data_penjualan:
                if quary.lower() in product[1].lower():
                    hasil.append(product)

            # logika ini untuk menampilkan data yang ditemukan
            if hasil:
                print(tabulate.tabulate(hasil, headers=["ID", "NAMA", "STOK", "HARGA"], tablefmt="grid", stralign="center", numalign="center"))
            else:
                print("Penjualan tidak ditemukan")
        elif answer == "Keluar":
            break