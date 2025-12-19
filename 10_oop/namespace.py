# The class namespace stores attributes shared by all objects.
# Each object has its own instance namespace for per-object values.

class Item:
    origin = "Global"     # class attribute

print(Item.origin)

Item.is_active = True     # adding attribute to class namespace
print(Item.is_active)

# Creating object from class Item
obj1 = Item()
print(obj1.origin)        # accessing class attribute
print(obj1.is_active)

obj1.is_active = False    # instance-level override
print("Class value:", Item.is_active)
print("Object value:", obj1.is_active)

obj1.label = "Sample"     # instance-only attribute
print(obj1.label)
