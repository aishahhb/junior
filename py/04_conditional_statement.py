# Exercise:
# 1.Write  a  program  that  categorizes  BMI  (Body  Mass  Index)  
#   intounderweight(<18.5),  
#   normal  weight(<24.9),  
#   overweight(<29.9),  and
#   obesity(<30.0). 
# (formula = kg/m^2)

name = str(input("Please enter your name: "))
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): "))

#input validation
while True:
    try:
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers!")

        #must to convert cm → meter
        height = height / 100

        #calculate bmi
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal"
        elif bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
        break

    except ValueError:
        print(f"Please enter the valid value for weight and height")

#output validation
print(f"Weight: {weight}kg, Height: {height}m")
print(f"{name}, your BMI is {round(bmi,2)}, category: {category}")

