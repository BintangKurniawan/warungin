from InquirerPy import inquirer
from models.pengutangModel import loadDataPengutang, savePengutang
from datetime import datetime
from tabulate import tabulate
import re
import os
def editPengutang():
    dataPengutang = loadDataPengutang()

    while True:
        pengutangDitemukan = False

        while not pengutangDitemukan:
            idPengutang = input("Masukkan ID pengutang: ").upper()
            for pengutang in dataPengutang:
                if pengutang['id'] == idPengutang:
                    pengutangDitemukan = True
                    pengutangTerpilih = pengutang
                    break
            if not pengutangDitemukan:
                print("ID pengutang tidak ditemukan. Silakan coba lagi.")

        while True:
            answer = inquirer.select(
                message="Pilih salah satu yang akan diedit:",
                choices=["Nama pengutang", "Total hutang", "Barang", "Keluar"],
                default="Nama pengutang"
            ).execute()

            if answer == "Nama pengutang":
                while True:
                    pengutangTerpilih["nama pengutang"] = input("Masukkan nama pengutang baru: ").title()

                    if not pengutangTerpilih["nama pengutang"].strip():
                        print("Nama pengutang tidak boleh kosong. Silakan masukkan kembali nama pengutang.")
                    else:
                        print("Nama pengutang berhasil diedit")
                        break
            elif answer == "Total hutang":
                while True:
                    try:
                        pengutangTerpilih["total hutang"] = int(input("Masukkan total hutang baru: "))
                        if pengutangTerpilih["total hutang"] < 0:
                            print("Total hutang tidak boleh kurang dari 0 rupiah. Silakan masukkan kembali total hutang.")
                        elif pengutangTerpilih["total hutang"] > 50000:
                            print("Total hutang melebihi batas maksimal 50000 rupiah. Silakan masukkan kembali total hutang.")
                        else:
                            break
                    except ValueError:
                        print("Total hutang harus berupa angka. Silakan masukkan kembali total hutang.")

                
            elif answer == "Barang":
                while True:
                    os.system('cls')
                    headers = ["No", "Nama Produk", "Jumlah Produk", "Tanggal Hutang"]
                    table = [[i + 1, barang["nama produk"], barang["jumlah produk"], barang["tanggal hutang"]] for i, barang in enumerate(pengutangTerpilih["barang"])]
                    print(tabulate(table, headers=headers, tablefmt="grid", stralign="center", numalign="center"))
                    barangAnswer = inquirer.select(
                        message="Pilih aksi untuk barang:",
                        choices=["Tambah barang", "Edit barang", "Hapus barang", "Kembali"],
                        default="Tambah barang"
                    ).execute()

                    if barangAnswer == "Tambah barang":

                        while True:
                            namaProduk = input("Masukkan nama produk: ").title()

                            if not namaProduk.strip():
                                print("Nama produk tidak boleh kosong. Silakan masukkan kembali nama produk.")
                            else:
                                break

                        while True:
                            try:
                                jumlahProduk = int(input("Masukkan jumlah produk: "))
                                if jumlahProduk < 0:
                                    print("Jumlah produk tidak boleh kurang dari 0. Silakan masukkan kembali jumlah produk.")
                                else:
                                    break
                            except ValueError:
                                print("Jumlah produk harus berupa angka. Silakan masukkan kembali jumlah produk.")

                        tanggalHutang = datetime.now().strftime("%Y-%m-%d")
                        
                        barangBaru = {
                            "nama produk": namaProduk,
                            "jumlah produk": jumlahProduk,
                            "tanggal hutang": tanggalHutang
                        }
                        pengutangTerpilih["barang"].append(barangBaru)
                        print("Barang berhasil ditambahkan.")

                    elif barangAnswer == "Edit barang":
                        if not pengutangTerpilih["barang"]:
                            print("Tidak ada barang untuk diedit.")
                            continue

                        indexBarang = int(input("Pilih nomor barang yang akan diedit: ")) - 1
                        if 0 <= indexBarang < len(pengutangTerpilih["barang"]):
                            barangTerpilih = pengutangTerpilih["barang"][indexBarang]
                        
                            while True:
                                os.system('cls')
                                headers = ["No", "Nama Produk", "Jumlah Produk", "Tanggal Hutang"]
                                table = [[i + 1, barang["nama produk"], barang["jumlah produk"], barang["tanggal hutang"]] for i, barang in enumerate(pengutangTerpilih["barang"])]
                                print(tabulate(table, headers=headers, tablefmt="grid", stralign="center", numalign="center"))
                                answer = inquirer.select(
                                    message="Pilih salah satu opsi:",
                                    choices=["Nama produk", "Jumlah produk", "Tanggal hutang", "Kembali"],
                                    default="Nama produk"
                                ).execute()

                                if answer == "Nama produk":

                                    while True:
                                        barangTerpilih["nama produk"] = input("Masukkan nama produk baru: ").title()

                                        if not barangTerpilih["nama produk"].strip():
                                            print("Nama produk tidak boleh kosong. Silakan masukkan kembali nama produk.")
                                        else:
                                            print("Barang berhasil diedit.")
                                            break
                                
                                elif answer == "Jumlah produk":
                                    while True:
                                        try:
                                            barangTerpilih["jumlah produk"] = int(input("Masukkan jumlah produk baru: "))
                                            if barangTerpilih["jumlah produk"] < 0:
                                                print("Jumlah produk tidak boleh kurang dari 0. Silakan masukkan kembali jumlah produk.")
                                            else:
                                                print("Barang berhasil diedit.")
                                                break
                                        except ValueError:
                                            print("Jumlah produk harus berupa angka. Silakan masukkan kembali jumlah produk.")  

                                elif answer == "Tanggal hutang":        
                                    while True:
                                        barangTerpilih["tanggal hutang"] = input("Masukkan tanggal hutang baru (YYYY-MM-DD): ").strip()

                                        if not re.match(r'^\d{4}-\d{2}-\d{2}$', barangTerpilih["tanggal hutang"]):
                                            print("Format tanggal tidak valid. Harap masukkan dalam format YYYY-MM-DD dan tanpa huruf.")
                                        else:
                                            print("Barang berhasil diedit.")
                                            break
                                
                                elif answer == "Kembali":
                                    break
                        else:
                            print("Nomor barang tidak valid.")

                    elif barangAnswer == "Hapus barang":
                        if not pengutangTerpilih["barang"]:
                            print("Tidak ada barang untuk dihapus.")
                            continue


                        indexBarang = int(input("Pilih nomor barang yang akan dihapus: ")) - 1
                        if 0 <= indexBarang < len(pengutangTerpilih["barang"]):
                            pengutangTerpilih["barang"].pop(indexBarang)
                            print("Barang berhasil dihapus.")
                        else:
                            print("Nomor barang tidak valid.")

                    elif barangAnswer == "Kembali":
                        break

            elif answer == "Keluar":
                savePengutang(dataPengutang)
                return

            editLagi = inquirer.select(
                message="Apakah ingin mengedit lagi?",
                choices=["Ya", "Tidak"],
                default="Ya"
            ).execute()

            if editLagi == 'Tidak':
                savePengutang(dataPengutang)
                return