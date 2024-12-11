import json

dailySalesFile = "data/dailySales.json"

def loadDailyData():
    with open(dailySalesFile, "r") as f:
        return json.load(f)
    
def saveDailySale(dailySales):
    with open(dailySalesFile, "w") as f:
        json.dump(dailySales, f, indent=4)
    