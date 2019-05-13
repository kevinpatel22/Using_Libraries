class Product:

    def __init__(self, name, base_price, tax_rate):
        self.name = name
        self.base_price = base_price
        self.tax_rate = tax_rate
    
    def __str__(self):
        return

    def calculate_total_price(self):
        total_price = 0
        total_price = self.base_price + (self.base_price * self.tax_rate / 100)
        return total_price



    
     