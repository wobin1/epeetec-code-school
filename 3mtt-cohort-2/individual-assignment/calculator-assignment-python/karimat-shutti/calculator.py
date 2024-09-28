def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed!!!"
    else:
        return num1 / num2


print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ("1", "2", "3", "4"):
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        if choice == "1":
            print(number1, "+", number2, "=", add(number1, number2))

        elif choice == "2":
            print(number1, "-", number2, "=", subtract(number1, number2))

        elif choice == "3":
            print(number1, "x", number2, "=", multiply(number1, number2))

        elif choice == "4":
            print(number1, "/", number2, "=", divide(number1, number2))

        next_calculation = input("Let's do next calculation? (yes/no): ")

        if next_calculation.lower() != "yes":
            break

    else:
        print("Invalid input")
