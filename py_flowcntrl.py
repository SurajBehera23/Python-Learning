user_input = int(input("Enter a number - "))
if user_input < 100:
    print("less than 100")

elif user_input == 100:
    print("Value is equal to 100")
else:
    print("Value is greater than 100")


#login
input_password = "8093479088"
input_UserName = "Vicky"

my_inputUser = input("Enter UserName - ")
my_inputPass = input("Enter Password - ")

if my_inputUser != input_UserName and my_inputPass != input_password:
    print("Invalid username and password")
elif my_inputUser != input_UserName:
    print("Invalid username")
elif my_inputPass != input_password:
    print("Invalid password")
else:
    print("Login Success")
    #test
