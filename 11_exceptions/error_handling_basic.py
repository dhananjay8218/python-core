# IndexError example
items = ["A", "B"]
try:
    print(items[2])   # invalid index
except IndexError:
    print("Index not available")

print("Continue...\n")


# KeyError and ValueError examples
menu = {"item1": 30, "item2": 40}

try:
    print(menu["missing"])
except KeyError:
    print("Key not found in menu")

try:
    x = int("abc")
except ValueError:
    print("Invalid number conversion")

print("Continue...\n")


# try / except / else / finally example
def process_item(name):
    try:
        print("Processing:", name)
        if name == "invalid":
            raise ValueError("Invalid item type")
    except ValueError as e:
        print("Error:", e)
    else:
        print("Completed:", name)
    finally:
        print("Cleanup done")

process_item("item1")
process_item("invalid")

print("\n")


# multiple exception handling example
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:
        print("Both values must be numbers")

print(divide(10, 0))
print(divide("x", 5))


# additional multiple-exception example (cleaned)
def process_order(item, quantity):
    try:
        price = {"itemA": 20}[item]
        total = price * quantity
        print(total)
    except KeyError:
        print("Item not available")
    except TypeError:
        print("Invalid quantity")

process_order("itemX", 1)
process_order("itemA", "two")
