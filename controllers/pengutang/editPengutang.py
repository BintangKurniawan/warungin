from InquirerPy import inquirer
from models.pengutangModel import loadDataPengutang, savePengutang

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
                pengutangTerpilih["nama pengutang"] = input("Masukkan nama pengutang baru: ").title()
                print("Nama pengutang berhasil diedit")
            elif answer == "Total hutang":
                pengutangTerpilih["total hutang"] = input("Masukkan total hutang baru: ")
                print("Total hutang berhasil diedit")
            elif answer == "Barang":
                while True:
                    barangAnswer = inquirer.select(
                        message="Pilih aksi untuk barang:",
                        choices=["Tambah barang", "Edit barang", "Hapus barang", "Kembali"],
                        default="Tambah barang"
                    ).execute()

                    if barangAnswer == "Tambah barang":
                        namaProduk = input("Masukkan nama produk: ").title()
                        jumlahProduk = int(input("Masukkan jumlah produk: "))
                        tanggalHutang = input("Masukkan tanggal hutang (YYYY-MM-DD): ")
                        
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

                        for i, barang in enumerate(pengutangTerpilih["barang"]):
                            print(f"{i + 1}. {barang}")

                        indexBarang = int(input("Pilih nomor barang yang akan diedit: ")) - 1
                        if 0 <= indexBarang < len(pengutangTerpilih["barang"]):
                            barangTerpilih = pengutangTerpilih["barang"][indexBarang]
                            
                            barangTerpilih["nama produk"] = input("Masukkan nama produk baru: ").title()
                            barangTerpilih["jumlah produk"] = int(input("Masukkan jumlah produk baru: "))
                            barangTerpilih["tanggal hutang"] = input("Masukkan tanggal hutang baru (YYYY-MM-DD): ")
                            print("Barang berhasil diedit.")
                        else:
                            print("Nomor barang tidak valid.")

                    elif barangAnswer == "Hapus barang":
                        if not pengutangTerpilih["barang"]:
                            print("Tidak ada barang untuk dihapus.")
                            continue

                        for i, barang in enumerate(pengutangTerpilih["barang"]):
                            print(f"{i + 1}. {barang}")

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