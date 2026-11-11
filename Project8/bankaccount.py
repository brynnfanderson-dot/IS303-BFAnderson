import random

class BankAccount:
    
    
    def __init__(self, user_name):
        self.balance = 0.00
        self.name = user_name #in the main file, have user name be an input the program asks for
        self.account_number = random.randint(100, 1000)

    def make_deposit(self):
        dep_amount = float(input("Enter the amount to deposit: $"))
        self.balance = self.balance + dep_amount
    def make_withdrawal(self):
        with_amount = float(input("Enter the amount to withdraw: $"))
        while with_amount > self.balance or with_amount < 0:
            print("You cannot withdraw an amount greater than the balance, or less than 0, please try again")
            with_amount = float(input("Enter the amount to withdraw: $"))
        self.balance = self.balance - with_amount
    def view_acount(self):
        print(f"\nName: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:,.2f}\n")