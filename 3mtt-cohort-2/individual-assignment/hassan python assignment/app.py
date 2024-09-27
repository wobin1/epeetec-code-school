
class BankAccount:
    def __init__(self, account_number, account_type="Checking", balance=0):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance}")
        return self.balance

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.accounts = []

    def add_account(self, account):
        if isinstance(account, BankAccount):
            self.accounts.append(account)
            print(f"Account {account.account_number} added for customer {self.name}.")
        else:
            print("Invalid account.")

    def get_accounts(self):
        if self.accounts:
            print(f"Customer {self.name} has the following accounts:")
            for account in self.accounts:
                print(f"- Account Number: {account.account_number}, Type: {account.account_type}, Balance: ${account.balance}")
        else:
            print(f"Customer {self.name} has no accounts.")


customer1 = Customer("Alice", 101)
customer2 = Customer("Bob", 102)

account1 = BankAccount(1001, "Checking", 500)
account2 = BankAccount(1002, "Savings", 1000)
account3 = BankAccount(1003, "Checking", 300)

customer1.add_account(account1)
customer1.add_account(account2)
customer2.add_account(account3)

account1.deposit(200)
account2.withdraw(150)
account3.deposit(500)

account1.check_balance()
account2.check_balance()
account3.check_balance()

customer1.get_accounts()
customer2.get_accounts()
