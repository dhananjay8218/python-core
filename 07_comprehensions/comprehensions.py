# comprehensions_basic.py — List, Set, Dict comprehensions

# List comprehension with filter
items = ["File A", "Temp B", "File C", "Temp D"]
temp_items = [x for x in items if "Temp" in x]
print(temp_items)

# Set comprehension to get unique values
names = ["Alex", "Sam", "Alex", "Riya", "Sam", "John"]
unique_names = {n for n in names}
print(unique_names)

# Nested set comprehension
library = {
    "Fiction": ["Book1", "Book2"],
    "Science": ["Book3", "Book4"],
    "Math": ["Book1", "Book5"]
}

unique_books = {book for group in library.values() for book in group}
print(unique_books)

# Dictionary comprehension
prices_inr = {"A": 80, "B": 120, "C": 200}
prices_usd = {k: v / 80 for k, v in prices_inr.items()}
print(prices_usd)

# Using comprehension inside sum()
sales = [3, 8, 2, 10, 6, 12]
total = sum(x for x in sales if x > 5)
print(total)
