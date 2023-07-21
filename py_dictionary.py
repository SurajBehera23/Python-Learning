name = {"First name": "Suraj", "Last name": "Behera", "Middle Name": "Kumar"}
print(type(name))
print(name)
print(name["First name"])

# pop method
name.pop("Middle Name")  # Corrected key name
print(name)

# Get method
print(name.get("Last name"))  # Added print statement

# keys method
print(name.keys())

# for loop
for every, values in name.items():
    print(every, values,sep="-")#Added separator
