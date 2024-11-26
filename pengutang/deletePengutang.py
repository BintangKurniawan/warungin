from data.data import pengutangfile

def hapus_pengutang():        
    data_pengutang = load_data_pengutang()

    id_pengutang = input("Masukkan ID pengutang: ").upper()

    nama_ditemukan = False
    for pengutang in data_pengutang:
        if pengutang[0] == id_pengutang:
            nama_ditemukan = True
            break

    if not nama_ditemukan:
        print("Error: ID pengutang tidak ditemukan.")
        return

    with open(pengutangfile, "w") as f:
        for pengutang in data_pengutang:
            if pengutang[0] != id_pengutang:
                f.write(f"{pengutang[0]},{pengutang[1]}\n")

    print("Pengutang berhasil dihapus")
