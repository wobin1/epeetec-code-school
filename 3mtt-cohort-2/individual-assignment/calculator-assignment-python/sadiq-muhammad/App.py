# Basic Calculator in Python

# Function to perform the operations
def calculator():
    # Ask user for input
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    # Perform calculation based on operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        # Check if the second number is not zero for division
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operator! Please use +, -, *, or /."

    # Return the result
    return f"The result is: {result}"

# Call the calculator function
print(calculator())
