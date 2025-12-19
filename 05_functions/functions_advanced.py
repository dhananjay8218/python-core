# functions_advanced.py — Advanced function examples

# Mutable argument example
data = [1, 2, 3]

def edit_list(values):
    values[1] = 42

edit_list(data)
print(data)

# Positional and keyword arguments
def describe_item(a, b, c):
    print(a, b, c)

describe_item("A", "B", "C")
describe_item(a="X", c="Z", b="Y") #keywords

# *args and **kwargs
def show_details(*items, **settings):
    print("Items:", items)
    print("Settings:", settings)

show_details("A", "B", option="on", mode="fast")

# Safe default argument
def add_item(lst=None):
    if lst is None:
        lst = []
    print(lst)

add_item()
add_item()

# pass example
def do_nothing():
    pass

print(do_nothing())

# Simple return
def get_total():
    return 120

total = get_total()
print(total)

# Conditional return
def status_check(count):
    if count == 0:
        return "No items left"
    return "Items available"

print(status_check(0))
print(status_check(5))

# Multiple return values
def report():
    return 100, 20, 10

sold, remaining, pending = report()
print("Sold:", sold)
print("Remaining:", remaining)

# Global update (not recommended)
total_units = 0

def update_units(n):
    global total_units
    total_units += n

# Recursion example
def countdown(n):
    print(n)
    if n == 0:
        return "Done"
    return countdown(n - 1)

print(countdown(3))

# Lambda with filter
items = ["alpha", "beta", "gamma", "beta"]
filtered = list(filter(lambda x: x != "beta", items))
print(filtered)
