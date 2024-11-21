class BasicCalculation:
    def __init__(self):
        pass

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 == 0:
            return "Error! Division by zero."
        return num1 / num2


def main():
    calculator = BasicCalculation()
    print("Welcome! Perform your basic arithmetic operations.")

    while True:
        print("\nChoose an option:")
        print("1. Perform Addition")
        print("2. Perform Subtraction")
        print("3. Perform Multiplication")
        print("4. Perform Division")
        print("5. Exit")
        
        user_choice = input("Enter your choice (1-5): ")

        if user_choice == "5":
            print("Exiting the program. Goodbye!")
            break

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! enter numeric values.")
            continue

        if user_choice == "1":
            result = calculator.addition(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif user_choice == "2":
            result = calculator.subtraction(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif user_choice == "3":
            result = calculator.multiplication(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif user_choice == "4":
            result = calculator.division(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Operation is invalid! Please enter a number between 1 and 5.")
            
if __name__ == "__main__":
    main()
