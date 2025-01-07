from models.dailySalesModel import loadDailyData
from InquirerPy import inquirer
import tabulate
import os
import re
from datetime import datetime
perPage = 5

def dailySaleByDate():
    data = loadDailyData()
    curPage = 0
    tableData = []
    for date, items in data.items():
            for item in items:
                tableData.append([date, item["Nama Produk"], item["Jumlah"], f"Rp. {item["Profit"]}"])
            headers = ["Tanggal", "Nama Produk", "Jumlah", "Profit"]

    while True:
        os.system('cls')

        while True:
        # Meminta tanggal dari pengguna
        
            print(tabulate.tabulate(tableData, headers=headers, tablefmt="grid", stralign="center", numalign="center"))
            date = input("Masukkan tanggal yang ingin dilihat (YYYY-MM-DD): ").strip()

            try:
                datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:

                print("Format tanggal tidak valid. Harap masukkan dalam format YYYY-MM-DD dan tanpa huruf.")
        # Memastikan tanggal ada dalam data
        if date not in data:
            print(f"Tidak ada data penjualan untuk tanggal {date}")
            answer = inquirer.select(
                message="Pilih salah satu opsi",
                choices=["Cari tanggal lain", "Keluar"],
                default="Cari tanggal lain"
            ).execute()
            if answer == "Keluar":
                break
            else:
                continue

        # Memfilter data berdasarkan tanggal
        filteredData = [
            [date, item["Nama Produk"], item["Jumlah"], f"Rp. {item['Profit']}"]
            for item in data[date]
        ]

        # Pagination setup
        totalRows = len(filteredData)
        totalPages = (totalRows + perPage - 1) // perPage  # Hitung total halaman

        while True:
            os.system('cls')
            start = curPage * perPage
            end = start + perPage
            pageData = filteredData[start:end]

            # Menampilkan data untuk halaman saat ini
            headers = ["Tanggal", "Nama Produk", "Jumlah", "Profit"]
            print(tabulate.tabulate(pageData, headers=headers, tablefmt="grid", stralign="center", numalign="center"))
            print(f"\nHalaman {curPage + 1} dari {totalPages}")

            # Menampilkan opsi
            answer = inquirer.select(
                message="Pilih salah satu opsi",
                choices=["Next Page", "Previous Page", "Cari tanggal lain", "Keluar"],
                default="Next Page"
            ).execute()

            if answer == "Next Page" and curPage < totalPages - 1:
                curPage += 1
            elif answer == "Previous Page" and curPage > 0:
                curPage -= 1
            elif answer == "Cari tanggal lain":
                curPage = 0  # Reset halaman ke awal saat mencari tanggal baru
                break
            elif answer == "Keluar":
                return