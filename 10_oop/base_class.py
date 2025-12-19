class Product:
    def __init__(self, category, strength):
        self.category = category
        self.strength = strength


# class SpecialProduct(Product):  # inheritance
#     def __init__(self, category, strength, level):
#         self.category = category
#         self.strength = strength
#         self.level = level


# class SpecialProduct(Product):  # explicit call
#     def __init__(self, category, strength, level):
#         Product.__init__(self, category, strength)
#         self.level = level

class SpecialProduct(Product):
    def __init__(self, category, strength, level):
        super().__init__(category, strength)
        self.level = level

p = SpecialProduct('TypeA', 'Medium', 'High')
print(p.strength)


