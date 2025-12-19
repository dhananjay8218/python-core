# Object-oriented programming (OOP) is a paradigm that models software as interacting objects.
# Key concepts shown here:
#  - class: blueprint that defines attributes and behavior
#  - object/instance: a concrete entity created from a class
#  - instance vs class attributes: per-object vs shared data
#  - encapsulation: controlling access to data (conventionally with _ or __)
#  - inheritance: subclass reuses and extends parent behavior
#  - polymorphism: same method name behaves differently on different classes
#  - composition: an object contains or uses another object
#  - staticmethod: utility function related to a class but not to an instance
#  - classmethod: constructor/alternative initializer that receives the class
#  - property: managed attribute with getter/setter logic
#  - MRO (Method Resolution Order): the order Python uses to find methods in multiple inheritance
#


# class and instance attributes
class Item:
    category = "General"            # class attribute shared by all instances

    def __init__(self, name, stock):
        self.name = name            # instance attribute unique per object
        self.stock = stock
        self._sku = None            # "protected" attribute by convention

    def __repr__(self):
        return f"Item(name={self.name!r}, stock={self.stock})"

    def summary(self):
        # a simple instance method
        return f"{self.name} — {self.stock} units"

# staticmethod and classmethod utilities
class StoreUtils:
    @staticmethod
    def normalize(text):
        # helper unrelated to any particular instance
        return text.strip().title()

    @classmethod
    def from_string(cls, text):
        # alternative constructor that returns an Item
        name, stock = text.split("-")
        name = cls.normalize(name)
        return Item(name, int(stock))

# composition: Warehouse contains an Item instance
class Warehouse:
    def __init__(self, item):
        self.item = item  # composition: Warehouse "has a" Item

    def dispatch(self, quantity=1):
        if self.item.stock >= quantity:
            self.item.stock -= quantity
            print(f"Dispatched {quantity} of {self.item.name}")
        else:
            print(f"Insufficient stock for {self.item.name}")

# inheritance + polymorphism: SpecialItem extends Item
class SpecialItem(Item):
    def __init__(self, name, stock, rating):
        super().__init__(name, stock)  # reuse parent initialization
        self.rating = rating           # new attribute in subclass

    def summary(self):
        # polymorphic override: different behavior for subclasses
        base = super().summary()
        return f"{base} | Rating: {self.rating}/5"

    @property
    def score(self):
        # property provides computed read-only attribute
        return self.rating * 10

    @score.setter
    def score(self, value):
        # setting score updates rating with validation
        rating = value / 10
        if not (0 <= rating <= 5):
            raise ValueError("Score must map to rating between 0 and 5")
        self.rating = rating

# multiple inheritance and MRO example
class A:
    label = "A"

    def describe(self):
        return "From A"

class B(A):
    label = "B"

    def describe(self):
        return "From B"

class C(A):
    label = "C"

    def describe(self):
        return "From C"

class D(C, B):
    # MRO: D -> C -> B -> A -> object
    pass

# encapsulation demonstration (private-like attribute)
class SecureItem(Item):
    def __init__(self, name, stock, secret):
        super().__init__(name, stock)
        self.__secret = secret   # name-mangled attribute

    def reveal_secret(self):
        return f"Secret: {self.__secret}"

# Usage examples (short, illustrative)

# basic items
i1 = Item("Notebook", 50)
print(i1.summary())            # instance method
print("repr:", repr(i1))

# using classmethod to create an item
i2 = StoreUtils.from_string("pen-100")
print(i2.summary())

# composition: warehouse dispatch
w = Warehouse(i2)
w.dispatch(10)
print("Remaining:", i2.stock)

# subclass and polymorphism
s = SpecialItem("Marker", 30, 4.5)
print(s.summary())
print("Score:", s.score)
try:
    s.score = 60   # sets rating to 6.0 (invalid) -> raises
except ValueError as exc:
    print("Score error:", exc)

s.score = 45      # valid -> rating = 4.5
print("Updated rating:", s.rating)

# MRO and polymorphic method resolution
d = D()
print("D label (from MRO):", d.label)
print("D describe():", d.describe())
print("D MRO:", D.__mro__)

# secure item and encapsulation
sec = SecureItem("SafeBox", 5, secret="top-secret")
print(sec.reveal_secret())
# trying to access __secret directly would fail (name mangled)
# print(sec.__secret)  # would raise AttributeError

# class vs instance attribute behavior
print("Class category:", Item.category)
i1.category = "Stationery"   # creates instance attribute that shadows class attribute
print("i1 category:", i1.category)
print("Item.category still:", Item.category)
del i1.category              # remove instance override
print("i1 category after delete:", i1.category)

# demonstrate dispatch when stock insufficient
w.dispatch(1000)

# final summary print to indicate end of demo
print("OOP revision demo complete.")
