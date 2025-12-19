class InvalidItemError(Exception):
    pass

def calculate_bill(item, quantity):
    menu = {"itemA": 20, "itemB": 40}

    try:
        if item not in menu:
            raise InvalidItemError("Item not available in menu")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")

        total = menu[item] * quantity
        print(f"Total cost for {quantity} units of {item}: {total}")

    except Exception as e:
        print("Error:", e)
    finally:
        print("Process complete")

calculate_bill("unknown", 2)
calculate_bill("itemA", "three")
calculate_bill("itemB", 3)
