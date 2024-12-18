from InquirerPy import inquirer
from datetime import datetime
from models.pengutangModel import savePengutang
from models.pengutangModel import loadDataPengutang
from models.pengutangModel import generateRandomID

def tambahPengutang():
    dataPengutang = loadDataPengutang()
    batasHutang = 50000
    existing_ids = {data["id"] for data in dataPengutang}
    idPengutang = generateRandomID(existing_ids)

    while True:
                namaPengutang = input("Masukkan nama pengutang: ").title()

                if not namaPengutang.strip():
                    print("Nama pengutang tidak boleh kosong, silahkan masukkan nama pengutang.")
                else:
                    break
    namaPengutang = input("Masukkan nama pengutang: ")

    while True:
        try:
            hutang = int(input(f"Masukkan jumlah hutang {namaPengutang} (maksimal {batasHutang}): "))
            if hutang < 0:
                print("Jumlah hutang tidak boleh kurang dari 0 rupiah.")
            elif hutang > batasHutang:
                print(f"Jumlah hutang melebihi batas maksimal {batasHutang}. Silakan kurangi jumlah hutang.")
            else:
                break
        except ValueError:
            print("Input tidak valid. Harap masukkan data dengan benar.")
    
    newData = {
        "id": idPengutang,
        "nama pengutang": namaPengutang,
        "total hutang": hutang,
        "barang": []
    }

    while True:
        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=["Tambah Barang", "Selesai"],
            default="Tambah Barang"
        ).execute()
        
        if answer == "Selesai":
            break
        

        namaBarang = input("Masukkan nama barang: ")

        jumlahBarang = int(input("Masukkan jumlah barang: "))
        tanggalHutang = datetime.now().strftime("%Y-%m-%d")

        barang = {
            "nama produk": namaBarang,
            "jumlah produk": jumlahBarang,
            "tanggal hutang": tanggalHutang
        }

        newData["barang"].append(barang)

    dataPengutang.append(newData)

    savePengutang(dataPengutang)

def checkPengutang():
    dataPengutang = loadDataPengutang()
    while True:
        if len(dataPengutang) == 2:
            print("Jumlah pengutang sudah mencapai batas maksimum. Mohon maaf tidak bisa menambah pengutang yang baru")

            
            answer = inquirer.select(
                message= "Tekan untuk keluar",
                choices=["Keluar"],
                default="Keluar"
            ).execute()

            if answer == "Keluar":
                break
        else:
            
            tambahPengutang()
            break