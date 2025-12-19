# utils/pricing.py — pricing and discount utilities

def calculate_price(quantity, rate):
    return quantity * rate

def apply_discount(amount, percent):
    return amount - (amount * percent / 100)
