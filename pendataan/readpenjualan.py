from data.data import loadDailyData
from InquirerPy import inquirer
import tabulate
import os

perPage = 5  # Jumlah entri yang ditampilkan per halaman

def showAllDailySalesDates():
    data = loadDailyData()  # Memuat data penjualan harian
    allDates = list(data.keys())  # Mendapatkan semua tanggal dari data
    curPage = 0  # Halaman awal

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Membersihkan layar

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

        # Menampilkan opsi navigasi
        answer = inquirer.select(
            message="Pilih salah satu opsi",
            choices=["Next Page", "Previous Page", "Keluar"],
            default="Next Page"
        ).execute()

        if answer == "Next Page" and curPage < totalPages - 1:
            curPage += 1
        elif answer == "Previous Page" and curPage > 0:
            curPage -= 1
        elif answer == "Keluar":
            return

# Contoh pemanggilan fungsi
if __name__ == "__main__":
    showAllDailySalesDates()