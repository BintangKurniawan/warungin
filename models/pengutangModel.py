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

def generateRandomID(existing_ids, length=4):
    while True:
        new_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        if new_id not in existing_ids:  # Pastikan ID unik
            return new_id