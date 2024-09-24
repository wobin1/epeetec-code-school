# 
def add (x,y):
  return x + y

def sub (x,y):
  return x - y

def mult (x,y):
  return x * y

def div (x,y):
  if y != 0:
    return x /y
  else:
    return "Error! invalid divisor"
def calculator ():

  first_number= float(input("Enter the first number: "))
  second_number= float(input("Enter the second number: "))
  Operator= (input("Enter your operator: "))

  addition = add (first_number, second_number)
  substraction = sub (first_number, second_number)
  multiplication = mult (first_number, second_number)
  division= div (first_number, second_number)

  if Operator == "+":
    print(addition)
  elif Operator == '_':
    print (substraction)
  elif Operator == "*":
    print (multiplication)
  elif Operator == "/":
    print (division)
  else:
    print("Invalid Input")
  
if __name__ == "__main__":
  calculator()


