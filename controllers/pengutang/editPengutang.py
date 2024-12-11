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
                choices=["Nama pengutang", "Total hutang",  "Keluar"],
                default="Nama"
            ).execute()

            if answer == "Nama pengutang":
                pengutangTerpilih["nama pengutang"] = input("Masukkan nama pengutang baru: ").title()
                print("Nama pengutang berhasil diedit")
            elif answer == "Total hutang":
                pengutangTerpilih["total hutang"] = input("Masukkan total hutang baru: ")
                print("Total hutang berhasil diedit")
            elif answer == "Keluar":
                return
            
            editLagi = inquirer.select(
                message="Apakah ingin mengedit lagi?",
                choices=["Ya", "Tidak"],
                default="Ya"
            ).execute()

            if editLagi == 'Tidak':
                savePengutang(dataPengutang)
                return