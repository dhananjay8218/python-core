# Walrus with remainder
num = 13
if (rem := num % 5):
    print("Remainder:", rem)


# Walrus with input check
options = ['a', 'b', 'c', 'd', 'e']
if (opt := input("Enter option: ")) in options:
    print("Found:", opt)
else:
    print("Not found")


# While loop with walrus
valid_options = ["red", "blue", "green"]
print("Available:", valid_options)

while (choice := input("Choose color: ").lower()) not in valid_options:
    print("Invalid:", choice)

print("Selected:", choice)
