import json
import string
import random

productsFile = "data/products.json"

def loadProducts():
    with open(productsFile, "r") as f:
        return json.load(f)

def saveProducts(products):
    with open(productsFile, "w") as f:
        json.dump(products, f, indent=4)
        
def generateRandomID(existing_ids, length=4):
    while True:
        new_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        if new_id not in existing_ids:  # Pastikan ID unik
            return new_id

def getPaginatedProducts(page, perPage=5):
    products = loadProducts()
    # Membalik urutan data produk
    products = list(reversed(products))
    totalRows = len(products)
    totalPages = (totalRows + perPage - 1) // perPage

    start = page * perPage
    end = start + perPage
    paginatedProducts = products[start:end]

    return paginatedProducts, totalPages
