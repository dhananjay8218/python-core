# mro_example.py — Method Resolution Order

class A:
    label = "A: Base"

class B(A):
    label = "B: Blend1"

class C(A):
    label = "C: Blend2"

class D(C, B):
    pass

obj = D()
print(obj.label)
print(D.__mro__)
