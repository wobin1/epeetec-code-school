# Function to perform the basic calculations
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator. Please use +, -, *, or /."

# Main program
def main():
    try:
        # Get input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /): ")

        # Perform the calculation and display the result
        result = calculate(num1, num2, operator)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")

# Run the program
if __name__ == "__main__":
    main()