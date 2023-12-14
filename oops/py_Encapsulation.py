class learn_encap():
    # Private class variable '__name'
    __name = "Suraj"

    # Constructor method to initialize the class
    def __init__(self):
        # Printing the value of the private variable '__name'
        print(self.__name)
        # Calling the private method '__game'
        self.__game()

    # Private method '__game'
    def __game(self):
        # Printing a test message
        print("Test")


# Creating an instance of the 'learn_encap' class
obj = learn_encap()
