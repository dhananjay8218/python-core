# Chapter 8: List operations
data = ["alpha", "beta", "gamma"]
data.append("delta")
print("List:", data)

data.remove("alpha")
print("List:", data)

opt = ["x", "y"]
main = ["a", "b"]
main.extend(opt)
print("Extend:", main)

main.insert(1, "z")
print("Insert:", main)

last = main.pop()
print("Popped:", last)
print("List:", main)

main.reverse()
print("Reverse:", main)

main.sort()
print("Sort:", main)

nums = [3, 7, 1, 9]
print("Max:", max(nums))
print("Min:", min(nums))

l1 = ["p", "q"]
l2 = ["r"]
print("Merge:", l1 + l2)

repeat = ["tag"] * 3
print("Repeat:", repeat)

raw = bytearray(b"HELLO")
raw = raw.replace(b"HE", b"GO")
print("Bytes:", raw)
