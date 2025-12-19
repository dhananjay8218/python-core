# Writing (creates or overwrites file)
with open("order.txt", "w") as file:
    file.write("ItemA - 4 units\n")
    file.write("ItemB - 2 units\n")

# Appending more data to the file
with open("order.txt", "a") as file:
    file.write("ItemC - 10 units\n")

# Reading the entire file
with open("order.txt", "r") as file:
    content = file.read()
    print("Full file content:\n", content)

# Reading line by line
with open("order.txt", "r") as file:
    print("Reading line by line:")
    for line in file:
        print(line.strip())

# Safe file read with error handling
try:
    with open("missing_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found: missing_file.txt")

# Writing structured data (list → file)
items = ["Notebook", "Pen", "Marker"]

with open("order.txt", "a") as file:
    for item in items:
        file.write(f"{item}\n")
