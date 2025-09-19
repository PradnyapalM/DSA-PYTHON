# Hashmap Patterns
"""
Transform data into  keys  to group, count or find relationships (O(n))

#  When to use HashMap Pattern
-> Need to count frequency of element
-> To group items by some property
-> Need to find pair/combinator
-> Need to track seen/ Visited items

"""

# Level 1

# 1> Create Hashmap
hashmap = {}

# 2> Add key-value in Hashmap
hashmap["Apple"] = 5
hashmap["Banana"] = 3
hashmap["Orange"] = 8

# 3 Access values of Hashmap
print(f"Quantity of Apple {hashmap['Apple']}")

# 4 Check if key if exists:
if "Apple" in hashmap:
    print("Found")
else:
    print("Not found")

#  5 Get the Default values
print(f"Orange: {hashmap.get('Orange', 0)}")

#  Iterate through Hashmap
for fruit, count in hashmap.items():
    print(f"{fruit}:{count}")

