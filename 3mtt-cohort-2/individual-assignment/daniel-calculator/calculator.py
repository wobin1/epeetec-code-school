A = """ _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""
print(A)

def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mult(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2

Operations = { "+": add, "-": sub, "*": mult, "/": div }

num1 = float(input("What is the first number?: "))

Should_continue = True
while Should_continue:
    for Operation in Operations:
        print(Operation)
    Op = input("Choose an operation: ")
    num2 = float(input("what is your next number: "))
    print(f"{num1} {Op} {num2} = {Operations[Op](num1,num2)}")
    continueORrestart = input(f"Type 'y' to continue calculating with {Operations[Op](num1,num2)}, or Type 'n' to start a new calculation: ").lower()
    if continueORrestart == "y":
        num1 = Operations[Op](num1,num2)
    elif continueORrestart == "n":
        print("\n" * 20)
        print(A)
        num1 = float(input("What is the first number?: "))
    else:
        Should_continue = False


