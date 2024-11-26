from InquirerPy import inquirer
import os
import tabulate
from pengutang.addPengutang import tambah_pengutang
from pengutang.editPengutang import edit_pengutang
from data.data import loadDataPengutang

def kelola_pengutang():
    data = loadDataPengutang()
    allId = list(data.keys())
    while True:
        os.system('cls')
        page_data = []
        for id in allId:
            for item in data[id]:
                barang = ", ".join([barang["Nama Produk"] for barang in item["Barang"]])

                page_data.append(
                [id, item["Nama Pengutang"], item["Total Hutang"],  barang]
                ) 

        print(tabulate.tabulate(page_data, headers=["ID", "Nama", "Jumlah Mengutang", "Barang"], tablefmt="grid", stralign="center", numalign="center"))

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
