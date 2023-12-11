print("WC to Rollercoster")
height=int(input("Enter your height-"))
# Check if the user meets the height requirement
if height>120:
    print("You can ride")
# If eligible, prompt the user to enter their age
    age=int(input("enter your age-"))
# Determine the ticket price based on age
    if age<12:
        print("ticket price is 500rs")
    elif age<=18:
        print("ticket price is 700rs")
    else:
        print("ticket price is 800rs")

else:
    print("you cant ride")