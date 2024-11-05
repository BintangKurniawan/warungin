from InquirerPy import prompt
import os

def main():
    opt = [
        {
            "type": "list",  # Menggunakan list prompt
            "name": "Option",  # Nama dari key yang digunakan di jawaban
            "message": "Pilih salah satu opsi:",  # Pesan yang ditampilkan ke pengguna
            "choices": ["1. Cek Produk", "2. Kelola Produk", "3. Cek Pendataan Harian", "4. Cek Pengutang", "5. Keluar"]  # Pilihan opsi
        }
    ]
    lanjut = True
    while lanjut == True:
        os.system('cls')
        print("========Welcome to Warungin========")
        answer = prompt(opt)
        if answer["Option"] == "1. Cek Produk":
            print("Cek produk")
        elif answer["Option"] == "2. Kelola produk":
            print("Cek produk")
        elif answer["Option"] == "3. Cek Pendataan Harian":
            print("Cek pengutang")
        elif answer["Option"] == "4. Cek Pengutang":
            print("Cek pengutang")
        elif answer["Option"] == "5. Keluar":
            print("Exit")
            lanjut = False

if __name__ == "__main__":
    main()
