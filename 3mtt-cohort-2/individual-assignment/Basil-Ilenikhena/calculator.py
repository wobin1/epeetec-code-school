# Simple Calculator

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Prompt user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for the operation
operation = input("Enter an operator (+, -, *, /): ")

# Perform the desired operation and print the result
if operation == '+':
    print(f"The result is: {add(num1, num2)}")
elif operation == '-':
    print(f"The result is: {subtract(num1, num2)}")
elif operation == '*':
    print(f"The result is: {multiply(num1, num2)}")
elif operation == '/':
    print(f"The result is: {divide(num1, num2)}")
else:
    print("Invalid operator! Please enter one of +, -, *, /.")
