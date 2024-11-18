from InquirerPy import inquirer
import os
import tabulate
from pengutang.addPengutang import tambah_pengutang
from pengutang.editPengutang import edit_pengutang
pengutangfile = "pengutang.txt"
per_page = 2

def load_data_pengutang():
    with open(pengutangfile, "r") as f:
            return [line.strip().split(",") for line in f]

def kelola_pengutang():

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
            tambah_pengutang()
        elif answer == "Edit Pengutang":
            edit_pengutang()
        elif answer == "Hapus Pengutang":
            print()
        elif answer == "Keluar":
            break
