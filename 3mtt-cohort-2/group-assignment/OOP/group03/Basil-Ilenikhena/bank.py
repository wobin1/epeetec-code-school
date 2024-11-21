class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = initial_balance
        self.__transaction_history = []

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = value

    @property
    def account_number(self):
        return self.__account_number

    # Function to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"Deposited {amount}")
            print(f"Deposited {amount}. New balance: {self.__balance}.")
        else:
            raise ValueError("Deposit amount must be positive.")

    # Function to withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        self.__transaction_history.append(f"Withdrew {amount}")
        print(f"Withdrew {amount}. New balance: {self.__balance}.")

    # Function to get the balance
    def get_balance(self):
        return self.__balance

    # Function to view transaction history
    def view_transaction_history(self):
        if not self.__transaction_history:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for transaction in self.__transaction_history:
                print(f"- {transaction}")


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.account = None

    # Function to create a new account
    def create_account(self, account_number, initial_balance=0):
        if self.account is not None:
            raise Exception(f"{self.name} already has an account.")
        self.account = BankAccount(account_number, self.name, initial_balance)
        print(f"Account created for {self.name} with account number {account_number}.")

    # Function to deposit into the account
    def deposit(self, amount):
        if self.account:
            self.account.deposit(amount)
        else:
            raise Exception("No account found for this customer.")

    # Function to withdraw from the account
    def withdraw(self, amount):
        if self.account:
            self.account.withdraw(amount)
        else:
            raise Exception("No account found for this customer.")

    # Function to check the account balance
    def check_balance(self):
        if self.account:
            balance = self.account.get_balance()
            print(f"Current balance for {self.name}: ${balance}.")
        else:
            raise Exception("No account found for this customer.")

    # Function to view transaction history
    def view_transaction_history(self):
        if self.account:
            self.account.view_transaction_history()
        else:
            raise Exception("No account found for this customer.")


# Example usage
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
    customer1.view_transaction_history()

    customer2.deposit(3000)
    try:
        customer2.withdraw(7000)  # Insufficient funds
    except Exception as e:
        print(f"Error: {e}")
    customer2.check_balance()
    customer2.view_transaction_history()
