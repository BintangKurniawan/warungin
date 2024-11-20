from data.data import loadDailyData, load_data_produk
import json
dailyFile = "dailySales.json"
productsFile = "products.json"

def addDailySale():
  dataDaily = loadDailyData()
  dataProducts = load_data_produk()
  
  productMap = {
    product["nama"].lower(): product for product in dataProducts
  }
  
  tanggal = input("Masukkan tanggal penjualan (YYYY-MM-DD): ").strip()
  
  if tanggal not in dataDaily:
    dataDaily[tanggal] = []
  
  while True:
    namaProduk = input("Masukkan nama produk: ").strip().title()
    if namaProduk.lower() in productMap:
        if any(item["Nama Produk"].lower() == namaProduk.lower() for item in dataDaily[tanggal]):
          print(f"Produk '{namaProduk}' sudah tercatat pada tanggal {tanggal}! Silakan input produk lain atau.")
          continue
        break  # Keluar dari loop jika produk ditemukan
    print("Nama produk tidak ditemukan dalam daftar produk! Silakan coba lagi.")
    
  productDetail = productMap[namaProduk.lower()]
  
  jumlah = int(input("Masukkan jumlah produk: ").strip())
  profit = productDetail["harga"] * jumlah
  
  newData = {
    "Nama Produk" : namaProduk,
    "Jumlah": jumlah,
    "Profit": profit
  }
  
      
  dataDaily[tanggal].append(newData)
  
  productDetail["stok"] -= jumlah
  
  with open(dailyFile, "w") as f:
    json.dump(dataDaily, f, indent=4)
    
  with open(productsFile, "w") as f:
        json.dump(dataProducts, f, indent=4)