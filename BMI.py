height=float(input("Enter your height"))
weight=float(input("Enter your weight"))
BMI=weight/(height**2)
print("Your BMI is",BMI)
if BMI<18.5:
    print("You are underweight")
elif BMI<25.0:
    print("you are normal")
elif BMI<30.0:
    print("You are overweight")
elif BMI<35.0:
    print("You are obesse")
else:
    print("You are severly obesse")