class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    # Function to deposit
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. Your new balance is: {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Your new balance:  {self.balance}.")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.account = None

    def create_account(self, account_number, initial_balance=0):
        self.account = BankAccount(account_number, self.name, initial_balance)
        print(f"Account created for {self.name} with account number {account_number}.")

    def deposit(self, amount):
        if self.account:
            self.account.deposit(amount)
        else:
            print("No account found for this customer.")

    def withdraw(self, amount):
        if self.account:
            self.account.withdraw(amount)
        else:
            print("No account found for this customer.")

    def check_balance(self):
        if self.account:
            balance = self.account.get_balance()
            print(f"Current balance for {self.name}: ${balance}.")
        else:
            print("No account found for this customer.")


# Example
if __name__ == "__main__":
    # Create customers
    customer1 = Customer("Alex", "C001")
    customer2 = Customer("Bob", "C002")

    # Create accounts
    customer1.create_account("1234567890", 10000)
    customer2.create_account("0987654321", 5000)

    # Perform transactions
    customer1.deposit(2000)
    customer1.withdraw(1500)
    customer1.check_balance()

    customer2.deposit(3000)
    customer2.withdraw(7000)  # Insufficient funds
    customer2.check_balance()
