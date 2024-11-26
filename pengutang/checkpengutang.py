from InquirerPy import inquirer
import os
import tabulate
from pengutang.addPengutang import tambahPengutang
from pengutang.editPengutang import edit_pengutang
from data.data import loadDataPengutang

def kelola_pengutang():
    while True:
        os.system('cls')
        data = loadDataPengutang()
        allId = list(data.keys())
        page_data = []
        for id in allId:
            nama_pengutang = data[id]["Nama Pengutang"]
            total_hutang = data[id]["Total Hutang"]
            barang_list = data[id]["Barang"]
        
        # Gabungkan nama produk dari daftar barang
            barang = ", ".join([barang["Nama Produk"] for barang in barang_list])
        
        # Tambahkan data ke page_data
            page_data.append([id, nama_pengutang, total_hutang, barang]) 

        print(tabulate.tabulate(page_data, headers=["ID", "Nama", "Jumlah Mengutang", "Barang"], tablefmt="grid", stralign="center", numalign="center"))

        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=[ "Tambah Pengutang", "Edit Pengutang", "Hapus Pengutang", "Keluar"],
            default="Tambah Pengutang"
        ).execute()

        if answer == "Tambah Pengutang":
            tambahPengutang()
        elif answer == "Edit Pengutang":
            edit_pengutang()
        elif answer == "Hapus Pengutang":
            print()
        elif answer == "Keluar":
            break
