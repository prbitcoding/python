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
    
order = Order()
order.add_item(Item("Apple", 0.58))
order.add_item(Item("Banana", 2.50))
order.add_item(Item("Mango", 0.45))
order.add_item(Item("orange", 5.60))

print("Total price:", order.total())