import json
import string
import random

pengutangFile = "data/pengutang.json"

def loadDataPengutang():
    with open(pengutangFile, "r") as f:
        return json.load(f)
    