def calculator(a, b):  # creating function
    print("Add - ", (a + b))
    print("Sub - ", (a - b))
    print("multi - ", (a * b))
    print("Divide - ", (a / b))


calculator(5, 5)  # calling function and passing parameter


# return

def word():
    return "Suraj"


msg = word()  # assigning variable to defined function
print(msg)


# passing parameter in function
def word2(name):
    print("My name is", name)


word2("Suraj")  # passed parameter in argument


# Argument types
def word3(name, name2):  # Positional Argument
    print("My name is", name, name2)


word3("Suraj", "Behera")


def word4(First_name, Last_name):  # keyword Argument
    print("My name is", First_name, Last_name)


word4(First_name=Suraj, Last_name=Behera)


def word5(default_name="Guest"):  # default Argument
    print("My name is", default_name)


word5()
