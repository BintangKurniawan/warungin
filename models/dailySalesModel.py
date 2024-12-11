import json

dailySalesFile = "data/dailySales.json"

def loadDailyData():
    with open(dailySalesFile, "r") as f:
        return json.load(f)
    