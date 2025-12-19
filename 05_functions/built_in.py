# docstrings_basics.py — Docstring and built-in function examples

def get_label(label="default"):
    """Return the given label."""
    temp = "placeholder"
    return label

print(get_label.__doc__)
print(get_label.__name__)

help(len)

def calculate_total(item1=0, item2=0):
    """
    Calculate a simple bill.

    :param item1: Quantity of item1 (price 10 each)
    :param item2: Quantity of item2 (price 15 each)
    :return: (total_amount, message)
    """
    total = item1 * 10 + item2 * 15
    return total, "Thank you for your visit"
