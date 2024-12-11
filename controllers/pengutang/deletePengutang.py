from models.pengutangModel import loadDataPengutang
from models.pengutangModel import savePengutang

def hapusPengutang():
    dataPengutang = loadDataPengutang()

    idPengutang = input("Masukkan ID pengutang: ").upper()

    pengutang = next((data for data in dataPengutang if data['id'] == idPengutang), None)

    if pengutang is None:
        print("Error: ID pengutang tidak ditemukan.")
        return
    
    konfirmasi = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ").lower()
    if konfirmasi == 'y':
        # Hapus data pengutang dari daftar
        dataPengutang.remove(pengutang)
        savePengutang(dataPengutang)
        print("Data pengutang berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")