import json
productsfile = "products.json"

# def load_data_produk():
#     with open(productsfile, "r") as f:
#             return [line.strip().split(",") for line in f]

def load_data_produk():
    with open(productsfile, "r") as f:
        return json.load(f)
    
