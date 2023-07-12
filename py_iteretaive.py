# for loop
myinput = eval(input("Enter number here : "))
for table in range(2, 6):
    print(myinput * table)

# while Loop
password = 123456
mypass = int(input("Enter Password"))
while mypass != password:
    mypass = int(input("enter password again"))
else:
    print("Login Success")
