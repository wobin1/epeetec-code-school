import math  # Import the math module for trigonometric functions
import pyfiglet
from colorama import init, Fore, Back, Style
# Define the Calculator class
#---------------- Calculator class begins------------------------------------
class Calculator:
    def __init__(self):
        pass

    # Initialize colorama
    init()
    
    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the quotient of a and b. Raises an error if dividing by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def modulo(self, a, b):
        """Return the remainder of a divided by b. Raises an error if modulo by zero."""
        if b == 0:
            raise ValueError("Cannot modulo by zero.")
        return a % b

    def sine(self, angle, mode='degrees'):
        """Return the sine of the angle in the specified mode (degrees or radians)."""
        return math.sin(math.radians(angle)) if mode == 'degrees' else math.sin(angle)

    def cosine(self, angle, mode='degrees'):
        """Return the cosine of the angle in the specified mode (degrees or radians)."""
        return math.cos(math.radians(angle)) if mode == 'degrees' else math.cos(angle)

#------------------------- Calculor class ends here -------------------------------------------



# Function to perform calculations based on user input
def perform_calculations(calculator):
    # Define the prompt with colored text
    prompt_message = (
        f"{Style.RESET_ALL}Enter operation ("
        f"{Fore.YELLOW}add{Style.RESET_ALL}, "
        f"{Fore.LIGHTRED_EX}subtract{Style.RESET_ALL}, "
        f"{Fore.GREEN}multiply{Style.RESET_ALL}, "
        f"{Fore.CYAN}divide{Style.RESET_ALL}, "
        f"{Fore.LIGHTMAGENTA_EX}modulo{Style.RESET_ALL}, "
        f"{Fore.LIGHTYELLOW_EX}sine{Style.RESET_ALL}, "
        f"{Fore.LIGHTBLUE_EX}cosine{Style.RESET_ALL}, "
        f"or {Fore.RED}'exit'{Style.RESET_ALL} to quit): {Style.RESET_ALL}"
    )
    """Prompt user for calculations until they choose to exit."""
    while True:
        # Prompt user for the operation they want to perform
        operation = input(prompt_message.strip().lower())

        # Exit the loop if the user wants to quit
        if operation == 'exit':
            print("Exiting the calculator.")
            break

        # Handle basic arithmetic operations
        if operation in ['add', 'subtract', 'multiply', 'divide', 'modulo']:
            a = float(input("Enter first number: "))  # Get the first number from the user
            b = float(input("Enter second number: ")) if operation != 'modulo' else float(input("Enter second number (modulo): "))  # Get the second number
            result = getattr(calculator, operation)(a, b)  # Call the appropriate method
            print(f"Result: {result}")  # Print the result

        # Handle trigonometric operations
        elif operation in ['sine', 'cosine']:
            angle = float(input("Enter angle: "))  # Get the angle from the user
            mode = input("Enter mode (degrees/radians): ").strip().lower()  # Get the mode (degrees or radians)
            result = getattr(calculator, operation)(angle, mode)  # Call the appropriate method
            print(f"Result: {result}")  # Print the result
        else:
            print("Invalid operation. Please try again.")  # Handle invalid input

# Welcome message and calculator initialization
# Create a fancy ASCII art welcome message
welcome_message = pyfiglet.figlet_format("SENTINEL CK") 
print(welcome_message)  # Display welcome message
calc = Calculator()  # Create an instance of the Calculator class
perform_calculations(calc)  # Start performing calculations
