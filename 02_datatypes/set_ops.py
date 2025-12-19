# Chapter 9: Set operations

primary_tags = {"alpha", "beta", "gamma"}
secondary_tags = {"beta", "delta", "epsilon"}

# Union → both sets combined (unique values)
all_tags = primary_tags | secondary_tags
print("All tags:", all_tags)

# Intersection → common elements
common_tags = primary_tags & secondary_tags
print("Common tags:", common_tags)

# Difference → only in primary
unique_primary = primary_tags - secondary_tags
print("Only primary:", unique_primary)

# Membership → check element present
print("Has 'delta'? :", "delta" in secondary_tags)

# Frozenset → immutable set
fixed_tags = frozenset(["alpha", "beta"])
print("Frozen tags:", fixed_tags)
