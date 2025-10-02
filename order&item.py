class Item:
    def __init__(self, name, price):
        self.name = name 
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total(self):
        return sum(item.price for item in self.items)
    
items1=Item("Apple", 0.58)
items2=Item("Banana", 2.50)
items3=Item("Mango", 0.45)
items4=Item("orange", 5.60)
    
order = Order()
order.add_item(items1)
order.add_item(items2)
order.add_item(items3)
order.add_item(items4)

print("Total order amount:", order.total())
 

 