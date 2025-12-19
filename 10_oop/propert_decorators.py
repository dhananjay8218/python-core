# property_decorator.py — Getter and setter example

class User:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age + 2

    @age.setter
    def age(self, value):
        if 1 <= value <= 5:
            self._age = value
        else:
            raise ValueError("Age must be between 1 and 5")

u = User(10)
print(u.age)
u.age = 18
print(u.age)
