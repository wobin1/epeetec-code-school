def calculate(num1, num2, operator):
  """Performs basic calculations on two numbers based on the given operator.

  Args:
    num1: The first number.
    num2: The second number.
    operator: The operator to perform the calculation.

  Returns:
    The result of the calculation.
  """

  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == '/':
    if num2 == 0:
      return "Cannot divide by zero."
    else:
      return num1 / num2
  else:
    return "Invalid operator."

def main():
  """Main function to get user input and perform the calculation."""

  while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")

    result = calculate(num1, num2, operator)
    print("Result:", result)

    choice = input("Do you want to perform another calculation? (y/n): ")
    if choice.lower() != 'y':
      break

if __name__ == "__main__":
  main()