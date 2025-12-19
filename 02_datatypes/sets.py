# Chapter 2: Working with sets
items = set()
print("Initial set ID:", id(items))
print("Initial set:", items)

items.add("File")
items.add("Folder")
items.add("Document")

print("Updated set ID:", id(items))
print("Updated set:", items)
