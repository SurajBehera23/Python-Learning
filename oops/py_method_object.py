# Define class A
class A:
    midage = int(input("enter mid age - "))  # Taking input for 'midage'
    topage = int(input("enter top age - "))  # Taking input for 'topage'
    total = midage + topage  # Calculate 'total' by summing 'midage' and 'topage'

    # print(total)  # Commented out to avoid unnecessary print statements

    # Define the 'multiply' method
    def multiply(self):
        midage = int(input("enter 1st num - "))  # Taking input for 'midage'
        topage = int(input("enter 2nd num - "))  # Taking input for 'topage'
        print(midage * topage)  # Print the multiplication result


# Create an instance 'obj' of class A
obj = A()

print(A.total)

# Call the 'mult' method of class A using the instance 'obj'
obj.multiply()


# Define class B
class B:
    a = 10
    b = 5

    # Define the 'minus' method
    def minus(self):
        print(self.a - self.b)  # Use of 'self' to print variables out of class

    # Define the 'passd' method
    def passd(self, a, b):  # passed argument
        print(a + b)

    # Define the constructor '__init__' method
    def __init__(self):
        print("My name is suraj kumar behera")  # Print a message when the instance of class B is created


# Create an instance 'obj' of class B
obj = B()

# Call the 'minus' method of class B using the instance 'obj'
obj.minus()

# Call the 'passd' method of class B with arguments 10 and 5
obj.passd(10, 5)
