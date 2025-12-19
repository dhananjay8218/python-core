# loops_basic.py — For loop examples

# Simple range loop
for token in range(1, 11):
    print(f"Token #{token}")

# Second range loop
for batch in range(1, 5):
    print(f"Batch #{batch}")

# Loop over list
users = ["Riya", "Aman", "Becky", "Carlos"]
for user in users:
    print(f"User: {user}")

# Loop with index using enumerate
options = ["Basic", "Standard", "Premium", "Enterprise"]
for idx, option in enumerate(options, start=1):
    print(f"{idx}: {option}")

# Loop over two lists with zip
names = ["Riya", "Meera", "Sam", "Ali"]
amounts = [50, 70, 100, 55]

for name, amount in zip(names, amounts):
    print(f"{name} paid {amount}")