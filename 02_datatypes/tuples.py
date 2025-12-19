# Chapter 7: Tuple usage
rgb = ("red", "green", "blue")
(r1, r2, r3) = rgb

print("Colors:", r1, r2, r3)

x, y = 2, 1
print("Before:", x, y)
x, y = y, x
print("After:", x, y)

print("Check 'blue':", "blue" in rgb)
