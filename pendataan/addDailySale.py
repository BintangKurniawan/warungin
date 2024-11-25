from data.data import loadDailyData, loadDataProduk
import json
dailyFile = "dailySales.json"
productsFile = "products.json"

def addDailySale():
  # Memuat data penjualan harian dan data produk dari file JSON
  dataDaily = loadDailyData()
  dataProducts = loadDataProduk()
  
  # Membuat mapping produk berdasarkan nama produk (huruf kecil) untuk mempermudah pencarian
  productMap = {
    product["nama"].lower(): product for product in dataProducts
  }
  
  tanggal = input("Masukkan tanggal penjualan (YYYY-MM-DD): ").strip()
  
  # Jika tanggal belum ada di data harian, tambahkan entri baru
  if tanggal not in dataDaily:
    dataDaily[tanggal] = []
  
  # Loop untuk memastikan input nama produk valid
  while True:
    namaProduk = input("Masukkan nama produk: ").strip().title()
    # Cek apakah nama produk ada di daftar produk
    if namaProduk.lower() in productMap:
        if any(item["Nama Produk"].lower() == namaProduk.lower() for item in dataDaily[tanggal]):
          print(f"Produk '{namaProduk}' sudah tercatat pada tanggal {tanggal}! Silakan input produk lain atau.")
          continue
        break  # Keluar dari loop jika produk ditemukan
    print("Nama produk tidak ditemukan dalam daftar produk! Silakan coba lagi.")
  
  # Ambil detail produk berdasarkan nama  
  productDetail = productMap[namaProduk.lower()]
  
  jumlah = int(input("Masukkan jumlah produk: ").strip())
  # Hitung profit berdasarkan harga produk dikalikan jumlah
  profit = productDetail["harga"] * jumlah
  
  newData = {
    "Nama Produk" : namaProduk,
    "Jumlah": jumlah,
    "Profit": profit
  }
  
  # Tambahkan entri penjualan baru ke dalam data harian    
  dataDaily[tanggal].append(newData)
  
  # Kurangi stok produk sesuai jumlah yang dijual
  productDetail["stok"] -= jumlah
  
  # Simpan perubahan data harian ke file JSON
  with open(dailyFile, "w") as f:
    json.dump(dataDaily, f, indent=4)
  
  # Simpan perubahan stok produk ke file JSON  
  with open(productsFile, "w") as f:
        json.dump(dataProducts, f, indent=4)