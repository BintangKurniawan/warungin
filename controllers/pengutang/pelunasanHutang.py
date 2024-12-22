import os
from models.pengutangModel import loadDataPengutang, savePengutang

def pelunasanHutang():
    dataPengutang = loadDataPengutang()

    idPengutang = input("Masukkan ID pengutang: ").upper()

    if idPengutang not in [pengutang["id"] for pengutang in dataPengutang]:
        print("Error: ID pengutang tidak ditemukan.")
        return

    while True:
        try:
            pelunasan = int(input("Masukkan jumlah pelunasan hutang: "))
            if pelunasan < 0:
                print("Jumlah pelunasan hutang tidak boleh kurang dari 0 rupiah.")
            else:
                break
        except ValueError:
            print("Input tidak valid. Harap masukkan data dengan benar.")

    for pengutang in dataPengutang:
        if pengutang["id"] == idPengutang:
            pengutang["total hutang"] = pengutang["total hutang"] - pelunasan
            savePengutang(dataPengutang)
            print("Pelunasan hutang berhasil dilakukan.")
            return