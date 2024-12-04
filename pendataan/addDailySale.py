from data.data import loadDailyData, loadDataProduk
import json

dailyFile = "dailySales.json"
productsFile = "data/products.json"

dataProducts = loadDataProduk()

def addDailySale():
    # Memuat data penjualan harian dan data produk dari file JSON
    global dataProducts
    dataDaily = loadDailyData()
    
    # Membuat mapping produk berdasarkan nama produk (huruf kecil) untuk mempermudah pencarian
    productMap = {
        product["nama"].lower(): product for product in dataProducts
    }
    
    tanggal = input("Masukkan tanggal penjualan (YYYY-MM-DD): ").strip()
    
    # Jika tanggal belum ada di data harian, tambahkan entri baru
    if tanggal not in dataDaily:
        dataDaily[tanggal] = []
    
    while True:
        namaProduk = input("Masukkan nama produk: ").strip().title()
        # Cek apakah nama produk ada di daftar produk
        if namaProduk.lower() in productMap:
            # Cari produk dalam data harian pada tanggal tertentu
            existingProduct = next((item for item in dataDaily[tanggal] if item["Nama Produk"].lower() == namaProduk.lower()), None)
            if existingProduct:
                print(f"Produk '{namaProduk}' sudah tercatat pada tanggal {tanggal}.")
                tambahJumlah = int(input("Masukkan tambahan jumlah produk: ").strip())
                
                stokTersedia = productMap[namaProduk.lower()]["stok"]        
                
                if tambahJumlah > stokTersedia:
                    print(f"Stok tidak mencukupi! Hanya tersedia {stokTersedia} unit.")
                    continue 
                
                # Update jumlah pada entri yang ada di dailySales.json
                existingProduct["Jumlah"] += tambahJumlah
                
                # Hitung ulang profit untuk entri tersebut
                existingProduct["Profit"] = existingProduct["Jumlah"] * productMap[namaProduk.lower()]["harga"]
                
                # Kurangi stok di products.json
                productMap[namaProduk.lower()]["stok"] -= tambahJumlah
                
                print(f"Jumlah produk '{namaProduk}' berhasil ditambahkan.")
            else:
                # Jika produk belum tercatat, tambahkan sebagai entri baru
                jumlah = int(input("Masukkan jumlah produk: ").strip())
                
                stokTersedia = productMap[namaProduk.lower()]["stok"]
                
                if jumlah > stokTersedia:
                    print(f"Stok tidak mencukupi! Hanya tersedia {stokTersedia} unit.")
                    continue 
                
                profit = productMap[namaProduk.lower()]["harga"] * jumlah
                
                newData = {
                    "Nama Produk": namaProduk,
                    "Jumlah": jumlah,
                    "Profit": profit
                }
                
                # Tambahkan entri penjualan baru ke dalam data harian    
                dataDaily[tanggal].append(newData)
                
                # Kurangi stok produk sesuai jumlah yang dijual
                productMap[namaProduk.lower()]["stok"] -= jumlah
                
                print(f"Produk '{namaProduk}' berhasil ditambahkan ke penjualan tanggal {tanggal}.")
        
            # Simpan perubahan data harian ke file JSON
            with open(dailyFile, "w") as f:
                json.dump(dataDaily, f, indent=4)

            # Simpan perubahan stok produk ke file JSON  
            with open(productsFile, "w") as f:
                json.dump(dataProducts, f, indent=4)
            
            # Keluar dari loop setelah pembaruan selesai
            break
        else:
            print("Nama produk tidak ditemukan dalam daftar produk! Silakan coba lagi.")
