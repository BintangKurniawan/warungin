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

            for pengutang in dataPengutang:
                if pengutang["id"] == idPengutang:
                    pengutang["total hutang"] = pengutang["total hutang"] - pelunasan

                    if pelunasan < 0:
                        print("Jumlah pelunasan hutang tidak boleh kurang dari 0 rupiah.")
                        answer = input("Ketik 'y' untuk melanjutkan: ").lower()
                        if answer == 'y':
                            return
                    elif pengutang["total hutang"] < 0:
                        print("Jumlah pelunasan hutang melebihi total hutang.")
                        answer = input("Ketik 'y' untuk melanjutkan: ").lower()
                        if answer == 'y':
                            return
                    elif pengutang['total hutang'] == 0:
                        dataPengutang.remove(pengutang)
                        break
                    
        except ValueError:
            print("Input tidak valid. Harap masukkan data dengan benar.")

        savePengutang(dataPengutang)
        
        return