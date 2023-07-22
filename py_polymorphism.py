# Class demonstrating Method Overloading
class Name:
    # Method 'myname' with default parameter 'title'
    def myname(self, title=""):
        # Printing the name with the specified title
        print("Suraj Kumar " + title)


# Creating an instance of the 'Name' class
obj = Name()

# Calling the 'myname' method without passing any title (using default parameter)
obj.myname()

# Calling the 'myname' method with the title "Behera"
obj.myname("Behera")


# Class demonstrating Method Overwriting
class game:
    # Method 'game1' in the base class
    def game1(self):
        print("Battle")

# Class 'game2' inheriting from the base class 'game'
class game2(game):
    # Overwritten method 'game1' in the derived class 'game2'
    def game1(self):
        super().game1()  # Calling the 'game1' method of the base class
        print("Tanks")

# Creating an instance of the 'game2' class
obj = game2()

# Calling the 'game1' method of the 'game2' class
obj.game1()

