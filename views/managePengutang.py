from InquirerPy import inquirer
import os
import tabulate
from controllers.pengutang.addPengutang import checkPengutang
from controllers.pengutang.deletePengutang import hapusPengutang
from controllers.pengutang.editPengutang import editPengutang
from controllers.pengutang.pelunasanHutang import pelunasanHutang
from models.pengutangModel import loadDataPengutang

def quick_sort(arr, key):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2][key]
        
        left = [x for x in arr if x[key] < pivot]
        middle = [x for x in arr if x[key] == pivot]
        right = [x for x in arr if x[key] > pivot]
        
        return quick_sort(left, key) + middle + quick_sort(right, key)


def kelolaPengutang():
    while True:
        os.system('cls')

        dataPengutang = loadDataPengutang()
        
        dataPengutang = quick_sort(dataPengutang, 'nama pengutang')

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
        
        print(tabulate.tabulate(pageData, headers=["ID", "Nama", "Total Hutang", "Barang"], tablefmt="grid", stralign="center", numalign="center"))

        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=[ "Tambah Pengutang", "Pelunasan", "Edit Pengutang", "Hapus Pengutang", "Keluar"],
            default="Tambah Pengutang"
        ).execute()

        if answer == "Tambah Pengutang":
            checkPengutang()
        elif answer == "Pelunasan":
            pelunasanHutang()
        elif answer == "Edit Pengutang":
            editPengutang()
        elif answer == "Hapus Pengutang":
            hapusPengutang()
        elif answer == "Keluar":
            break