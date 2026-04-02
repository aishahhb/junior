# Exercises:
# 1.Create a simple calculator that takes two number and an operation from user.
# 2.Create  a  simple  quiz  program  with  3  questions.  At  the  end  of  the  quiz, display score.

operations = ["+", "-", "*", "/"]

while True:
    try:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: ")) 
        operation = input(f"Choose operation ({', '.join(operations)}): ")

        # Perform calculation
        if operation not in operations:
            print("Invalid operation! Exiting calculator.")
            break

        match operation:
            case '+':
                result = num1 + num2
            case '-':
                result = num1 - num2
            case '*':
                result = num1 * num2
            case '/':
                result = num1 / num2 if num2 != 0 else "Error: Division by zero!"
            case _:
                result = "Invalid operation"

        print(f"{num1} {operation} {num2} = {result}")
        
    except ValueError:
        print("Please enter the correct value!")