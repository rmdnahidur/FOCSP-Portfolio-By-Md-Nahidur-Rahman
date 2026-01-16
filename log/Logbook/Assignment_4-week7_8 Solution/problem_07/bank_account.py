"""
Program Name: Bank Account Class
Description:
This program defines a class 'BankAccount' with methods:
deposit(amount) - to add money
withdraw(amount) - to withdraw money with exception handling
get_balance() - to display current balance
"""

# Define BankAccount class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. Current balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Insufficient balance!")
            elif amount <= 0:
                print("Withdrawal amount must be positive.")
            else:
                self.balance -= amount
                print(f"Withdrew {amount}. Current balance: {self.balance}")
        except ValueError as e:
            print("Error:", e)

    # Method to get current balance
    def get_balance(self):
        print(f"Current balance: {self.balance}")

# Main program
account = BankAccount("Ram Yadav")

# Demonstration
account.deposit(5000)
account.withdraw(2000)
account.withdraw(4000)  # This will trigger insufficient balance
account.get_balance()
