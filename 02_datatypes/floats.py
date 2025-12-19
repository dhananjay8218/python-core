# Chapter 5: Float precision
import sys

ideal = 10.5
current = 10.48

print("Ideal:", ideal)
print("Current:", current)
print("Diff:", ideal - current)

print(sys.float_info)
