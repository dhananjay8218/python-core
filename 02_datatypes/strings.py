# Chapter 6: String operations
msg = "System Update"
user = "Alex"

print(f"{user}: {msg}")

desc = "Performance Boost"
print("Slice 1:", desc[:11])
print("Slice 2:", desc[12:])
print("Reverse:", desc[::-1])

text = "Data Résumé"
enc = text.encode("utf-8")
print("Encoded:", enc)
print("Decoded:", enc.decode("utf-8"))
