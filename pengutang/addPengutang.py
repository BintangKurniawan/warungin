import random
import string
import json
from InquirerPy import inquirer
from data.data import loadDataPengutang
pengutangFile = "pengutang.json"


def randomizer_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))


def tambah_pengutang():
    data_pengutang = loadDataPengutang()
    data ={}
    batas_hutang= 50000

    # variabel ini untuk membuat id random
    id_pengutang= randomizer_id()

    # variabel ini untuk mengecek apakah id pengutang sudah ada
    existing_ids = {pengutang[0] for pengutang in data_pengutang}
    while id_pengutang in existing_ids:
        id_pengutang = randomizer_id()

    if id_pengutang not in existing_ids:
        data[id_pengutang] = []

    nama_pengutang = input(f"Masukkan nama pengutang: ")

    while True:
        try:
            hutang = int(input(f"Masukkan jumlah hutang {nama_pengutang} (maksimal {batas_hutang}): "))
            if hutang < 0:
                print("Jumlah hutang tidak boleh kurang dari 0 rupiah.")
            elif hutang > batas_hutang:
                print(f"Jumlah hutang melebihi batas maksimal {batas_hutang}. Silakan kurangi jumlah hutang.")
            else:
                break
        except ValueError:
                print("Input tidak valid. Harap masukkan data dengan benar.")

    # variabel ini untuk menambahkan pengutang
    data_pengutang[id_pengutang] = {
        "Nama Pengutang": nama_pengutang,
        "Total Hutang": hutang,
        "Barang": []
    }

    while True:
        nama_barang = input("Masukkan nama barang (atau 'selesai' untuk keluar): ")
        if nama_barang.lower() == 'selesai':
            break

        jumlah_barang = int(input("Masukkan jumlah barang: "))
        tanggal_hutang = input("Masukkan tanggal hutang (YYYY-MM-DD): ")

        barang = {
            "Nama Produk": nama_barang,
            "Jumlah Produk": jumlah_barang,
            "Tanggal Hutang": tanggal_hutang
        }

        data_pengutang[id_pengutang]["Barang"].append(barang)
    
    with open(pengutangFile, "w") as f:
        json.dump(data_pengutang, f, indent=4)

    print("pengutang berhasil ditambahkan")

def tambahPengutang():
    pengutang = loadDataPengutang()
    while True:
        if len(pengutang) == 2:
            print("Jumlah pengutang sudah mencapai batas maksimum. Mohon maaf tidak bisa menambah pengutang yang baru")

            
            answer = inquirer.select(
                message= "Tekan untuk keluar",
                choices=["Keluar"],
                default="Keluar"
            ).execute()

            if answer == "Keluar":
                break
        else:
            tambah_pengutang()
            break


# def tambah_utang():
#     data_pengutang = load_data_pengutang()
    
#     while True:
#         nama = input("Masukkan nama pengutang (atau 'exit' untuk keluar): ")
#         if nama.lower() == 'exit':
#             break
        
#         jumlah_hutang = float(input("Masukkan jumlah hutang: "))

#         with open(pengutangfile, "w") as f:
#            f.write(f"{nama},{jumlah_hutang}\n")

#     print("jumlah hutang baru berhasil ditambahkan")