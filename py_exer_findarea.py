# Class demonstrating flexible area calculation
class Area:
    # Method to calculate area based on given inputs
    def areamulti(self, a=None, b=None):
        if a is not None and b is not None:
            print(a * b)  # Calculate area for rectangle if both 'a' and 'b' are provided
        elif a is not None:
            print(a * a)  # Calculate area for square if only 'a' is provided
        else:
            print("No input found")  # If no input is provided, print an appropriate message

# Creating an instance of the 'Area' class
obj = Area()

# Calling the 'areamulti' method without any input
obj.areamulti()

# Calling the 'areamulti' method with one input (a=10)
obj.areamulti(10)

# Calling the 'areamulti' method with two inputs (a=10, b=5)
obj.areamulti(10, 5)
