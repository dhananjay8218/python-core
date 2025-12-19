# conditionals.py — Basic condition examples

# Boolean check
is_ready = False
if is_ready:
    print("System is ready.")
else:
    print("System is not ready.")

# Number input check
amount = int(input("Enter amount: "))

if amount > 1000:
    print("High amount")
elif amount > 500:
    print("Medium amount")
else:
    print("Low amount")

# Category choice
size = input("Choose size (s/m/l): ").lower()

if size == "s":
    print("You selected Small")
elif size == "m":
    print("You selected Medium")
elif size == "l":
    print("You selected Large")
else:
    print("Unknown size")

# OR condition
item = input("Enter item (chips/cookies): ").lower()
if item == "chips" or item == "cookies":
    print(f"Item selected: {item}")
else:
    print("Item not available")
