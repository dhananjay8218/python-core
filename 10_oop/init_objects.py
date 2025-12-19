# init_objects.py — Object initialization using __init__

class Order:
    def __init__(self, item, amount):  #constructor
        self.item = item
        self.amount = amount

    def summary(self):
        return f"{self.amount} units of {self.item}"

o1 = Order("Notebook", 200)
print(o1.summary())

o2 = Order("Pen", 220)
print(o2.summary())
