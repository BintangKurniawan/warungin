from inquirerPy import inquirer
import os
import tabulate
import random
import string
from pengutang.checkpengutang import cek_pengutang
pengutangfile = "pengutang.txt"
per_page = 2

# fungsi ini untuk membuat id random
def randomizer_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

# fungsi ini untuk load data pengutang
def load_data_pengutang():
    with open(pengutangfile, "r") as f:
            return [line.strip().split(",") for line in f]



# fungsi ini untuk menambah pengutang
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

        pengutang.append((nama_pengutang, jumlah_mengutang))

    print("pengutang berhasil ditambahkan")

# fungsi ini untuk mengedit pengutang
def edit_pengutang():
    data_pengutang = load_data_pengutang()

    id_pengutang = input("Masukkan ID pengutang: ").upper()

    nama_ditemukan = False
    for hutang in data_pengutang:
        if pengutang[0] == id_pengutang:
            nama_ditemukan = True
            break

    if not nama_ditemukan:
        print("Error: ID nama tidak ditemukan.")
        return

    nama_pengutang = input("Masukkan nama pengutang: ")
    jumlah_mengutang = input("Masukkan jumlah mengutang: ")

    with open(pengutangfile, "w") as f:
        for pengutang in data_pengutang:
            if pengutang[0] == id_pengutang:
                f.write(f"{id_pengutang},{nama_pengutang},{jumlah_mengutang}\n")
            else:
                f.write(f"{hutang[0]},{hutang[1]}\n")

    print("Data pengutang berhasil diedit")

# fungsi ini untuk menghapus pengutang
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

# fungsi ini untuk mengelola pengutang
def kelola_pengutang():
    cur_page = 0

    while True:
        os.system('cls')

        data_pengutang = load_data_pengutang()
        total_rows = len(data_pengutang)
        total_pages = (total_rows + per_page - 1)

        start = cur_page * per_page
        end = start + per_page
        page_data = data_pengutang[start:end]

        print(tabulate.tabulate(page_data, headers=["ID", "NAMA", "JUMLAH MENGUTANG"], tablefmt="grid", stralign="center", numalign="center"))

        answer = inquirer.select(
            message="Pilih salah satu opsi:",
            choices=["Next Page", "Previous Page", "Tambah Pengutang", "Edit Pengutang", "Hapus Pengutang", "Keluar"],
            default="Next Page"
        ).execute()

        if answer == "Next Page" and cur_page < total_pages - 1:
            cur_page += 1
        elif answer == "Previous Page" and cur_page > 0:
            cur_page -= 1
        elif answer == "Tambah Pengutang":
            tambah_pengutang()
        elif answer == "Edit Pengutang":
            edit_pengutang()
        elif answer == "Hapus Pengutang":
            hapus_pengutang()
        elif answer == "Keluar":
            break
