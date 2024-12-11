from InquirerPy import inquirer
import os
import tabulate
from controllers.pengutang.addPengutang import checkPengutang
from controllers.pengutang.deletePengutang import hapusPengutang
from controllers.pengutang.editPengutang import editPengutang
from models.pengutangModel import loadDataPengutang

def kelolaPengutang():
    while True:
        os.system('cls')

        dataPengutang = loadDataPengutang()
        
        pageData = [
    [
        item['id'],
        item['nama pengutang'],
        f"Rp. {item['total hutang']}",
        ", ".join(
            f"{barang['nama produk']}"
            for barang in item['barang']
        )
    ]
    for item in dataPengutang
]
        
       

        print(tabulate.tabulate(pageData, headers=["ID", "Nama", "Jumlah Hutang", "Barang"], tablefmt="grid", stralign="center", numalign="center"))

        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=[ "Tambah Pengutang", "Edit Pengutang", "Hapus Pengutang", "Keluar"],
            default="Tambah Pengutang"
        ).execute()

        if answer == "Tambah Pengutang":
            checkPengutang()
        elif answer == "Edit Pengutang":
            editPengutang()
        elif answer == "Hapus Pengutang":
            hapusPengutang()
        elif answer == "Keluar":
            break