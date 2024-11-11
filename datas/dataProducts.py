productsfile = "products.txt"

def load_data_produk():
    with open(productsfile, "r") as f:
            return [line.strip().split(",") for line in f]