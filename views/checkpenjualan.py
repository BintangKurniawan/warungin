from InquirerPy import inquirer
import os
import tabulate
from controllers.pendataan.addDailySale import addDailySale
from controllers.pendataan.showDailySaleByDate import dailySaleByDate
from models.dailySalesModel import loadDailyData

perPage = 5  # Jumlah entri yang ditampilkan per halaman

def cekPenjualan():
    while True:
        data = loadDailyData()  # Muat ulang data penjualan harian dari file JSON
        
        # Mengumpulkan semua entri penjualan dalam satu daftar
        tableData = []
        for date, items in data.items():
            for item in items:
                tableData.append([date, item["Nama Produk"], item["Jumlah"], f"Rp. {item["Profit"]}"])
        
        curPage = 0  # Halaman awal
        totalEntries = len(tableData)  # Total entri penjualan
        totalPages = (totalEntries + perPage - 1) // perPage  # Hitung total halaman
        
        
        while True:
            os.system('cls')  # Bersihkan layar 
            # Mengambil data untuk halaman saat ini
            start = curPage * perPage
            end = start + perPage
            pageData = list(reversed(tableData))
            paginatedData = pageData[start:end]
            
            # Menampilkan data untuk halaman saat ini
            headers = ["Tanggal", "Nama Produk", "Jumlah", "Profit"]
            print(tabulate.tabulate(paginatedData, headers=headers, tablefmt="grid", stralign="center", numalign="center"))
            print(f"\nHalaman {curPage + 1} dari {totalPages}")
            
            # Opsi yang dapat dipilih
            answer = inquirer.select(
                message="Pilih salah satu opsi:",
                choices=["Next Page", "Previous Page", "Filter tanggal", "Tambah Penjualan", "Keluar"],
                default="Next Page"
            ).execute()

            # Logika navigasi
            if answer == "Next Page" and curPage < totalPages - 1:
                curPage += 1
            elif answer == "Previous Page" and curPage > 0:
                curPage -= 1
            elif answer == "Tambah Penjualan":
                addDailySale()
                break  # Keluar dari loop tabel untuk memuat ulang data
            elif answer == "Filter tanggal":
                dailySaleByDate()
            elif answer == "Keluar":
                return
