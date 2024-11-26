import json
productsfile = "products.json"
dailySalesfile = "dailySales.json"
pengutangfile = "pengutang.json"

def loadDataProduk():
    with open(productsfile, "r") as f:
        return json.load(f)
    

def loadDailyData():
    with open(dailySalesfile, "r") as f:
        return json.load(f)
    
def loadDataPengutang():
    with open(pengutangfile, "r") as f:
        return json.load(f)