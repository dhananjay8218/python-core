# tokenize_text.py — using modules, imports, and functions

from data import get_item_list, item_description
from utils import calculate_price, apply_discount

items = get_item_list()
print("Available:", items)

desc = item_description("Notebook")
print(desc)

total = calculate_price(quantity=3, rate=20)
print("Total:", total)

final_amount = apply_discount(total, percent=10)
print("After discount:", final_amount)
