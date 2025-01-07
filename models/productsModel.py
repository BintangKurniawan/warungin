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


def reverse_list(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])

def quick_sort(arr, key):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2][key]
        
        left = [x for x in arr if x[key] < pivot]
        middle = [x for x in arr if x[key] == pivot]
        right = [x for x in arr if x[key] > pivot]
        
        return quick_sort(left, key) + middle + quick_sort(right, key)

def getPaginatedProducts(page, perPage=5):
    products = loadProducts()
    # Membalik urutan data produk
    products = quick_sort(products, "nama")
    totalRows = len(products)
    totalPages = (totalRows + perPage - 1) // perPage

    start = page * perPage
    end = start + perPage
    paginatedProducts = products[start:end]

    return paginatedProducts, totalPages
