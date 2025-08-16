# 🧮 Basic Python Calculator

A simple calculator program in Python that performs:

- Addition ➕  
- Subtraction ➖  
- Multiplication ✖️  
- Division ➗  

This project was created as part of my internship project.

---

## 📋 Requirements

- Python 3.x installed on your system

---

## 📜 Code

```python
# Basic Calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("\n🔹 Welcome to the Basic Calculator 🔹")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Exit")

    while True:
        choice = input("\nEnter choice (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} × {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} ÷ {num2} = {divide(num1, num2)}")

        elif choice == '5':
            print("Exiting calculator. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice! Please select a valid option (1-5).")

if __name__ == "__main__":
    calculator()



##⚙️ **How to Run**

Save the code as calculator.py

Open terminal and run: python calculator.py


##📸 **Example Output**
🔹 Welcome to the Basic Calculator 🔹
Select operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (×)
4. Division (÷)
5. Exit

Enter choice (1/2/3/4/5): 1
Enter first number: 12
Enter second number: 8
Result: 12.0 + 8.0 = 20.0


##👤** Author **

Mayank Sharma
