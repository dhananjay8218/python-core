# Class attributes are shared by all objects.
# Instance attributes belong only to a specific object.

class Item:
    status = "active"
    grade = "high"

obj = Item()
print(obj.status)

obj.status = "low"      # instance-level override
obj.tag = "small"       # instance-only attribute

print("After change:", obj.status)
print("Tag:", obj.tag)
print("Class value:", Item.status)

del obj.status          # remove instance override
del obj.tag             # remove instance-only attribute

print(obj.status)       # falls back to class attribute
print(obj.tag)          # raises AttributeError
