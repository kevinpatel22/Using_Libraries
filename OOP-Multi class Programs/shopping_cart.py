from buy import Product

class Cart: 

    def __init__(self):
        self.items = []
    
    def __str__(self):
        return f"You have {len(self.items)} items in your cart"

    def add_to_cart(self, product):
        self.items.append(product)
        return f"{product.name} has been added to your cart."
    
    def remove_from_cart(self, product):
        self.items.remove(product)
        return f"{product.name} has been removed from your cart."
    
    def aft(self):
        price_aft_tax = round(0)
        for prod in self.items:
            price_aft_tax += prod.base_price 
            price_aft_tax = price_aft_tax + (price_aft_tax * prod.tax_rate / 100)
        return f'Your total after tax is ${price_aft_tax:.2f}.'
    
    def b4t(self):
        price_b4t_tax = round(0)
        for prod in self.items:
            price_b4t_tax += prod.base_price 
        return f'Your total before tax is ${price_b4t_tax}.'


stella = Product('Stella', 5, 13)
cheese = Product('Cheese', 159.99, 8)
lays = Product ('lays', 2.47, 8)

shopping_cart = Cart()

print(shopping_cart.add_to_cart(stella))
print(shopping_cart.add_to_cart(cheese))
print(shopping_cart.add_to_cart(lays))
print(shopping_cart)
print(shopping_cart.remove_from_cart(lays))
print(shopping_cart.aft())
print(shopping_cart.b4t())
   
