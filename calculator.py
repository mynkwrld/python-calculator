# ---------------------------------------------------------
# Calculator Project
# Author: Mayank Sharma
# Description: A simple calculator that performs
#              addition, subtraction, multiplication,
#              and division using Python.
# ---------------------------------------------------------

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def calculator():
    print("🔹 Welcome to the Basic Calculator 🔹")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Exit")

    while True:
        choice = input("\nEnter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")
            continue

        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} × {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {num1} ÷ {num2} = {result}")
        else:
            print("❌ Invalid choice! Please select a valid option (1-5).")

if __name__ == "__main__":
    calculator()
