
# Part C - List Report

# 1. Start with the given list
items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# 2. Print each item with a number
print("SHOPPING LIST REPORT")

for index in range(len(items)):
    print(f"{index + 1}. {items[index]}")

# 3. Count item names with more than 4 letters
count = 0

for item in items:
    if len(item) > 4:
        count += 1

print("\nItems with more than 4 letters:", count)

# 4. Find the longest item name using loop comparison
longest = items[0]

for item in items:
    if len(item) > len(longest):
        longest = item

print("Longest item name:", longest)
