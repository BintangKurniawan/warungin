import json
import string
import random

pengutangFile = "data/pengutang.json"

def loadDataPengutang():
    with open(pengutangFile, "r") as f:
        return json.load(f)
    
def savePengutang(pengutang):
    with open(pengutangFile, "w") as f:
        json.dump(pengutang, f, indent=4)

