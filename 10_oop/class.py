# A class is a blueprint for creating objects.
# An object is an instance of a class.
# type() shows the type or class of any object.

class Item:
    pass

class Product:
    pass

print(type(Item))          # type of class
obj = Item()

print(type(obj))           # type of object
print(type(obj) is Item)   # True
print(type(obj) is Product)  # False
