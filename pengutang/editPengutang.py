pengutangfile = "pengutang.txt"


def load_data_pengutang():
    with open(pengutangfile, "r") as f:
            return [line.strip().split(",") for line in f]
def edit_pengutang():
    data_pengutang = load_data_pengutang()

    id_pengutang = input("Masukkan ID pengutang: ").upper()

    nama_ditemukan = False
    for hutang in data_pengutang:
        if hutang[0] == id_pengutang:
            nama_ditemukan = True
            break

    if not nama_ditemukan:
        print("Error: ID nama tidak ditemukan.")
        return

    nama_pengutang = input("Masukkan nama pengutang: ")
    jumlah_mengutang = input("Masukkan jumlah mengutang: ")

    with open(pengutangfile, "w") as f:
        for hutang in data_pengutang:
            if hutang[0] == id_pengutang:
                f.write(f"{id_pengutang},{nama_pengutang},{jumlah_mengutang}\n")
            else:
                f.write(f"{hutang[0]},{hutang[1]},{hutang[2]}\n")

    print("Data pengutang berhasil diedit")
