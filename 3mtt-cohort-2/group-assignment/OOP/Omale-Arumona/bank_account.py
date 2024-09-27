import random
import string
from datetime import datetime


class BankAccount:
    """Manages account details and transactions."""

    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):

        self.balance += amount
        self.transactions.append(
            f"Deposit: +${amount:.2f} at {datetime.now()}")

        return self.balance

    def withdraw(self, amount):

        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transactions.append(
            f"Withdrawal: -${amount:.2f} at {datetime.now()}")
        return f"Successfully withdrawn ${amount}"

    def get_balance(self):

        return self.balance

    def view_transactions(self):
        return self.transactions


class Customer:
    """Manages customer information and associates it with bank accounts."""

    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, address):

        self.accounts["Account Details"] = {
            "Account Number": account_number, "Name": name, "Address": address}

    def get_account(self):

        return self.accounts.get("Account Details", "You have no account")

    def view_details(self):
        return self.accounts


print("Welcome to DoWell Bank!!!")
print("To get started, please create an account.")

customer = Customer()

customer_name = input("Enter your name: ")
customer_address = input("Enter your address: ")
auto_generated_account_number = "".join(random.choices(string.digits, k=4))

customer.create_account(auto_generated_account_number,
                        customer_name, customer_address)

print("You have successfully created your account!")
print("Please find your account details below:")

account_details = customer.get_account()

for account_detail in account_details.items():
    print(f"{account_detail[0]}: {account_detail[1]}")

bank_account = BankAccount()
while True:
    print("What operation do you want to perform next?")
    print("1. Deposit Money")
    print("2. Check Account Balance")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. View Customer Details")
    print("6. Quit")

    operation_choice = input("Please enter an option (1/2/3/4/5/6): ")

    if operation_choice == "1":
        customer_account_number = input("Please provide your account number: ")
        if customer_account_number == auto_generated_account_number:
            amount_deposited = input("Please enter your deposit amount: ")
            bank_account.deposit(int(amount_deposited))
            print(f"Successfully deposited ${amount_deposited}")
        else:
            print("Account does not exist")
    elif operation_choice == "2":
        customer_account_number = input("Please provide your account number: ")
        if customer_account_number == auto_generated_account_number:
            balance_on_account = bank_account.get_balance()
            print(f"Your account balance is: ${balance_on_account}")
        else:
            print("Account does not exist")
    elif operation_choice == "3":
        customer_account_number = input("Please provide your account number: ")
        if customer_account_number == auto_generated_account_number:
            amount_withdrawal = input("Please enter your withdrawal amount: ")
            balance_on_account = bank_account.withdraw(int(amount_withdrawal))
            print(f"Successfully withdrawn ${amount_withdrawal}")
    elif operation_choice == "4":
        customer_account_number = input("Please provide your account number: ")
        if customer_account_number == auto_generated_account_number:
            transaction_history = bank_account.view_transactions()
            for transaction in transaction_history:
                print(transaction)
    elif operation_choice == "5":
        customer_account_number = input("Please provide your account number: ")
        if customer_account_number == auto_generated_account_number:
            details = customer.view_details().get("Account Details")
            for detail in details.items():
                print(f"{detail[0]}: {detail[1]}")
        else:
            print("Account does not exist")
    elif operation_choice == "6":
        break

    else:
        print("Invalid input")
