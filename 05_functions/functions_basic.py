# functions_basic.py — Function examples

# Simple function with parameters
def print_order(name, item):
    print(f"{name} ordered {item}")


print_order("Aman", "Notebook")
print_order("Hitesh", "Pen")
print_order("Jia", "Laptop")


# User registration workflow
def fetch_input():
    print("Fetching user input")

def validate_input():
    print("Validating input")

def save_record():
    print("Saving record")

def register_user():
    fetch_input()
    validate_input()
    save_record()
    print("Registration complete")


register_user()


# Report generation workflow
def fetch_sales():
    print("Fetching sales data")

def filter_sales():
    print("Filtering sales")

def summarize():
    print("Summarizing data")

def generate_report():
    fetch_sales()
    filter_sales()
    summarize()
    print("Report ready")


generate_report()


# Function with return value
def calculate_total(quantity, price):
    return quantity * price


total_amount = calculate_total(3, 15)
print("Total:", total_amount)

print("Table 2:", calculate_total(2, 50))


# VAT example
def add_vat(amount, vat_rate):
    return amount * (100 + vat_rate) / 100


orders = [100, 150, 200]

for amount in orders:
    final_price = add_vat(amount, 10)
    print(f"Original: {amount}, With VAT: {final_price}")
