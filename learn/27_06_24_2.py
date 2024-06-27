class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ClothesProduct:
    def __init__(self,name,price, size, battery):
        self.name = name
        self.price = price
        self.battery = battery

        
product_list = [
    Product('Смарт часы', 16900),
]