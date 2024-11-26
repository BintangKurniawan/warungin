from data.data import loadDataPengutang
import json
pengutangfile = "pengutang.json"
def hapus_pengutang():        
    data_pengutang = loadDataPengutang()

    id_pengutang = input("Masukkan ID pengutang: ").upper()

    if id_pengutang not in data_pengutang:
        print("Error: ID pengutang tidak ditemukan.")
        return

    # Hapus pengutang berdasarkan ID
    del data_pengutang[id_pengutang]

    # Simpan data ke file
    with open(pengutangfile, "w") as f:
        json.dump(data_pengutang, f, indent=4)

    print("Pengutang berhasil dihapus")
