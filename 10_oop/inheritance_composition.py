# inheritance + composition

class BaseItem:
    def __init__(self, category):
        self.category = category

    def prepare(self):
        print("Preparing:", self.category)

class SpecialItem(BaseItem):  # inheritance
    def add_features(self):
        print("Adding extra features")

class Store:
    item_cls = BaseItem # composition

    def __init__(self):
        self.item = self.item_cls("Regular")  # composition

    def serve(self):
        print("Serving:", self.item.category)
        self.item.prepare()

class PremiumStore(Store):  # inheritance
    item_cls = SpecialItem

s1 = Store()
s2 = PremiumStore()

s1.serve()
s2.serve()
s2.item.add_features()
