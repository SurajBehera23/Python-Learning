# List
name = ["Suraj", 1000, 50.5, True, 1000]
print(type(name))
# Range
print(name[0:3])
# count
print(name.count(1000))
# index
print(name.index(1000))
# insert method
name.insert(2, "Test")
print(name)
# delete Method
name.pop(2)
print(name)

# extend
name2 = [500, 1000]
name.extend(name2)
print(name)
# Copy Method
name3 = name.copy()
print(name3)
# sort
name4 = [100, 200, 50, 3000]
name4.sort()
print(name4)
# reverse sort
name4 = [100, 200, 50, 3000]
name4.sort(reverse=True)
print(name4)
# List comprehension
name5 = ["Suraj", "sicky", "Tina"]
a = [word for word in name5 if word.startswith("T") or word.startswith("S")]
print(a)
# list unpacking
b = [1100, 3000]
n1, n2 = b
print(n1)
