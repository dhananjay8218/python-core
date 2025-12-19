# self_args.py — self usage example
# Methods use 'self' to access instance attributes.

class Box:
    size = 150  # class attribute

    def describe(self):
        return f"A box of size {self.size}ml"

box1 = Box()
print(box1.describe())
print(Box.describe(box1))

box2 = Box()
box2.size = 100
print(Box.describe(box2))
