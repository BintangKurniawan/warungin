from InquirerPy import inquirer
import os
import tabulate
from pendataan.searchpenjualan import cari_penjualan
from pendataan.addDailySale import addDailySale
from pendataan.showDailySaleByDate import dailySaleByDate
from pendataan.readpenjualan import showAllDailySalesDates
from data.data import loadDailyData

# fungsi ini untuk ngecek penjualan
def cekPenjualan():
    os.system('cls')  # Membersihkan layar

    data = loadDailyData()  # Memuat data penjualan

    # Mengumpulkan data penjualan dalam format yang diinginkan
    filteredData = [
        [date, item["Nama Produk"], item["Jumlah"], item["Profit"]]
        for date in data for item in data[date]
    ]

    # Pastikan ada data untuk ditampilkan
    if not filteredData:
        print("Tidak ada data untuk ditampilkan.")
        inquirer.text(message="Tekan Enter untuk kembali ke menu utama.").execute()
        return

    # Menampilkan keseluruhan data penjualan
    print(tabulate.tabulate(filteredData, headers=["Tanggal", "Nama Produk", "Jumlah", "Profit"], tablefmt="grid", stralign="center", numalign="center"))

    while True:
        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=["Cek Penjualan", "Filter tanggal", "Tambah Penjualan", "Update Penjualan", "Cari Penjualan", "Keluar"],
            default="Cek Penjualan"
        ).execute()

        if answer == "Tambah Penjualan":
            addDailySale()
        elif answer == "Cari Penjualan":
            cari_penjualan()
        elif answer == "Cek Penjualan":
            showAllDailySalesDates()
        elif answer == "Filter tanggal":
            dailySaleByDate()
        elif answer == "Keluar":
            break

# Contoh pemanggilan fungsi
if __name__ == "__main__":
    cekPenjualan()