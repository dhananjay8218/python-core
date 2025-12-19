# classmethod_example.py — Class method constructors

class Order:
    def __init__(self, item, quality, size):
        self.item = item
        self.quality = quality
        self.size = size

    @classmethod
    def from_dict(cls, data):
        return cls(data["item"], data["quality"], data["size"])

    @classmethod
    def from_string(cls, text):
        item, quality, size = text.split("-")
        return cls(item, quality, size)

class Utils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]

print(Utils.is_valid_size("Medium"))

o1 = Order.from_dict({"item": "Notebook", "quality": "High", "size": "Large"})
o2 = Order.from_string("Pen-Low-Small")
o3 = Order("Marker", "Medium", "Large")

print(o1.__dict__)
print(o2.__dict__)
print(o3.__dict__)
