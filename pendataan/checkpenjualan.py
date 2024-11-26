from InquirerPy import inquirer
import os
import tabulate
from pendataan.addDailySale import addDailySale
from pendataan.showDailySaleByDate import dailySaleByDate
from data.data import loadDailyData
perPage = 5  # Jumlah entri yang ditampilkan per halaman


# fungsi ini untuk ngecek penjualan
def cekPenjualan():
    data = loadDailyData()  # Memuat data penjualan harian
    allDates = list(data.keys())  # Mendapatkan semua tanggal dari data
    curPage = 0  # Halaman awal
    while True:
        os.system('cls') 
        # Pagination setup
        totalDates = len(allDates)
        totalPages = (totalDates + perPage - 1) // perPage  # Hitung total halaman
        start = curPage * perPage
        end = start + perPage
        pageDates = allDates[start:end]
        # Menampilkan semua tanggal dan data penjualan terkait
        tableData = []
        for date in pageDates:
            for item in data[date]:
                tableData.append([date, item["Nama Produk"], item["Jumlah"], item["Profit"]])
        # Menampilkan data untuk halaman saat ini
        headers = ["Tanggal", "Nama Produk", "Jumlah", "Profit"]
        print(tabulate.tabulate(tableData, headers=headers, tablefmt="grid", stralign="center", numalign="center"))
        print(f"\nHalaman {curPage + 1} dari {totalPages}")
            

        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=["Next Page", "Previous Page", "Filter tanggal", "Tambah Penjualan", "Update Penjualan", "Keluar"],
            default="Next Page"
        ).execute()

        if answer == "Next Page" and curPage < totalPages - 1:
            curPage += 1
        elif answer == "Previous Page" and curPage > 0:
            curPage -= 1
        elif answer == "Tambah Penjualan":
            addDailySale()
        elif answer == "Filter tanggal":
            dailySaleByDate()
        elif answer == "Keluar":
            break
