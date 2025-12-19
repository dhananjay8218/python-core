# Continue & break example
items = ["A", "Skip", "B", "Stop", "C"]

for item in items:
    if item == "Skip":
        continue
    if item == "Stop":
        print("Stop found.")
        break
    print("Item:", item)

print("Loop ended.")
