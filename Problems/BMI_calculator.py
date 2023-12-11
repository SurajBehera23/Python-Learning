# BMI Calculator

# Prompt the user to enter height and weight
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display the BMI with two decimal places
print(f"Your BMI is: {bmi:.2f}")

# Categorize BMI and provide a weight status summary
if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You have normal weight")
elif bmi < 30:
    print("You are overweight")
elif bmi < 35:
    print("You are Obese")
else:
    print("You are clinically obese")