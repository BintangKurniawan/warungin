from InquirerPy import inquirer
import os
import tabulate

pengutangfile = "pengutang.txt"
per_page = 2

def load_data_pengutang():
    with open(pengutangfile, "r") as f:
            return [line.strip().split(",") for line in f]

def kelola_pengutang():
    cur_page = 0

    while True:
        os.system('cls')

        data_pengutang = load_data_pengutang()
        
        page_data = data_pengutang

        print(tabulate.tabulate(page_data, headers=["ID", "NAMA", "JUMLAH MENGUTANG"], tablefmt="grid", stralign="center", numalign="center"))

        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=[ "Tambah Pengutang", "Edit Pengutang", "Hapus Pengutang", "Keluar"],
            default="Tambah Pengutang"
        ).execute()

        if answer == "Tambah Pengutang":
            print()
        elif answer == "Edit Pengutang":
            print()
        elif answer == "Hapus Pengutang":
            print()
        elif answer == "Keluar":
            break
