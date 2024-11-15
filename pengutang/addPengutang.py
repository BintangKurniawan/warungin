import random
import string
pengutangfile = "pengutang.txt"
def randomizer_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
def load_data_pengutang():
    with open(pengutangfile, "r") as f:
            return [line.strip().split(",") for line in f]

def tambah_pengutang():
    pengutang = []
    batas_hutang_perorang= 50000

    data_pengutang = load_data_pengutang()

    # variabel ini untuk membuat id random
    id_pengutang= randomizer_id()

    # variabel ini untuk mengecek apakah id pengutang sudah ada
    existing_ids = {pengutang[0] for pengutang in data_pengutang}
    while id_pengutang in existing_ids:
        id_pengutang = randomizer_id()

    # variabel ini untuk menambahkan pengutang
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

    print("pengutang berhasil ditambahkan")