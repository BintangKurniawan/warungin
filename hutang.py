def tambah_utang():
    pengutang = []
    batas_hutang_perorang= 50000

    for i in range(2):
        nama_pengutang = input(f"Masukkan nama pengutang ke-{i + 1}: ")

        while True:
            try:
                hutang = int(input(f"Masukkan jumlah hutang {nama_pengutang} (maksimal {batas_hutang_perorang}): "))
                if hutang < 0:
                    print("Jumlah hutang tidak boleh kurang dari 0 rupiah.")
                elif hutang > batas_hutang_perorang:
                    print(f"Jumlah hutang melebihi batas maksimal {batas_hutang_perorang}. Silakan kurangi jumlah hutang Anda.")
                else:
                    break
            except ValueError:
                print("Input tidak valid. Harap masukkan data dengan benar.")

        pengutang.append((nama_pengutang, hutang))

    print("Data-data orang yang menghutang:")
    for nama_pengutang, hutang in pengutang:
        print(f"Nama: {nama_pengutang}, Jumlah Hutang: {hutang}")

if __name__ == "__main__":
    tambah_utang()
