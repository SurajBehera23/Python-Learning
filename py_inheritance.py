# Define class A
class A():
    def isA(self):
        print("Name is A")


# Define class B
class B():
    def isB(self):
        print("Name is B")


# Define class C, which inherits from class A and class B
class C(A, B):
    def isC(self):
        print("Name is C")


# Create an instance 'obj' of class C
obj = C()

# Call the isA() method from class A using the instance 'obj'
obj.isA()

# Call the isB() method from class B using the instance 'obj'
obj.isB()
