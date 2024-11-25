import json
productsfile = "products.json"
dailySalesfile = "dailySales.json"

# def loadDataProduk():
#     with open(productsfile, "r") as f:
#             return [line.strip().split(",") for line in f]

def loadDataProduk():
    with open(productsfile, "r") as f:
        return json.load(f)
    

def loadDailyData():
    with open(dailySalesfile, "r") as f:
        return json.load(f)