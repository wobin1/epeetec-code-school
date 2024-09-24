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




# Interactive CLI flow
def main():
    print("Welcome to the Banking System CLI!")


    customers = {}


    while True:
        print("\nChoose an option:")
        print("1. Create a new customer")
        print("2. Create an account for a customer")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. Check balance")
        print("6. View transaction history")
        print("7. Exit")


        choice = input("Enter your choice (1-7): ")


        if choice == "1":
            # Create a new customer
            name = input("Enter customer name: ")
            customer_id = input("Enter customer ID: ")
            if customer_id not in customers:
                customers[customer_id] = Customer(name, customer_id)
                print(f"Customer {name} created successfully.")
            else:
                print("Customer ID already exists.")


        elif choice == "2":
            # Create an account for a customer
            customer_id = input("Enter customer ID: ")
            if customer_id in customers:
                account_number = input("Enter account number: ")
                initial_balance = float(input("Enter initial balance: "))
                customers[customer_id].create_account(account_number, initial_balance)
            else:
                print("Customer not found. Please create the customer first.")


        elif choice == "3":
            # Deposit money
            customer_id = input("Enter customer ID: ")
            if customer_id in customers:
                amount = float(input("Enter deposit amount: "))
                customers[customer_id].deposit(amount)
            else:
                print("Customer not found.")


        elif choice == "4":
            # Withdraw money
            customer_id = input("Enter customer ID: ")
            if customer_id in customers:
                amount = float(input("Enter withdrawal amount: "))
                try:
                    customers[customer_id].withdraw(amount)
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Customer not found.")


        elif choice == "5":
            # Check balance
            customer_id = input("Enter customer ID: ")
            if customer_id in customers:
                customers[customer_id].check_balance()
            else:
                print("Customer not found.")


        elif choice == "6":
            # View transaction history
            customer_id = input("Enter customer ID: ")
            if customer_id in customers:
                customers[customer_id].view_transaction_history()
            else:
                print("Customer not found.")


        elif choice == "7":
            # Exit the program
            print("Exiting the Banking System CLI. Goodbye!")
            break


        else:
            print("Invalid choice, please select a valid option (1-7).")




if __name__ == "__main__":
    main()