# FIRDAUSI IBRAHIM
# SOFTWARE DEVELOPMENT
import math

print("Welcome to the CalcWorm")
print("What can we do for you today? ")
print("Options:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exponential")
print("7. Logarithm")

operation = input("Enter the operation you wish to perform [1 - 7]: ")
if operation.isnumeric():
    operation = int(operation)
    if 1 <= operation <= 7:
        pass
    else:
        print("Invalid operation choice selected. Please try again")
else:
    operation = 0
    print("Invalid input entered.")

if 1 <= operation <= 7:
    print("If Logarithm operation is selected, enter the base as the first number "
          "and the target number as the second.")

    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    if num1.isnumeric():
        num1 = float(num1)
    else:
        print("Invalid input to number 1. Number 1 can only contain numbers. Please try again.")
        operation = 0

    if num2.isnumeric():
        num2 = float(num2)
    else:
        print("Invalid input to number 2. Number 2 can only contain numbers. Please try again.")
        operation = 0
else:
    num1 = 0
    num2 = 0


if operation == 1:
    result = num1 + num2
elif operation == 2:
    result = num1 - num2
elif operation == 3:
    result = num1 * num2
elif operation == 4:
    result = num1 / num2
elif operation == 5:
    result = num1 % num2
elif operation == 6:
    result = num1 ** num2
elif operation == 7:
    result = math.log(num2, num1)
else:
    result = None

if result is None:
    pass
else:
    print(f"The result is {result}")