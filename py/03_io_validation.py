name = str(input("Please enter your name: "))
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): "))

#must to convert cm → meter
height = height / 100

#input validation
while True:
    try:
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers!")

        #calculate bmi
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        break

    except ValueError:
        print(f"Please enter the valid value for weight and height")

#output validation
print(f"Weight: {weight}kg, Height: {height}m")
print(f"{name}, your BMI is {round(bmi,2)}, category: {category}")

