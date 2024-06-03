"""
Ensure to complete the expected code in hpolyFintech.py before proceeding to this file
"""
from hpolyFintech import *


option = ['R', 'W', 'D', 'C', 'B', "EXIT"]


def align_center(message):
    print(message.center(100))

def align_tab(message):
    info = message.split("\n")
    for information in info:
        print(f"\t{information}")

def register_data():
    data_gen = {}
    align_center("Please Provide the following data correctly")
    data_gen["username"] = input("\tPls Enter username$ ")
    data_gen["pin"] = pin_validation()
    data_gen["amount"] = amount_validation()
    data_gen["age"] = age_validation()
    user_registration(**data_gen)

def withdrawal_check():
    info = accountData()
    for data in info:
        withdrawal_check = withdrawals(data['account_Number'], data['pin'])
        align_tab(withdrawal_check)
        break

def deposit_check():
    info = accountData()
    for data in info:
        username = data['username']
        pin = data['pin']
        account_number = check_balance(username,pin)
        align_tab(account_number)
        break


def pin_validation():
    while True:
        try:
            pin = int(input("\tEnter user pin$ "))
            if len(str(pin)) == 4:
                return pin
            else:
                align_tab("Pin must be 4 digits")
        except ValueError:
            align_tab("Pin must be an integer data type")


def amount_validation():
    while True:
        try:
            amount = int(input("\tEnter initial deposit$ "))
            if amount >= 1000:
                return amount
            else:
                align_tab("Initial deposit must be up to 1000 and above")
        except ValueError:
            align_tab("Initial deposit must be an integer data type")


def age_validation():
    while True:
        try:
            age = int(input("\tEnter age$ "))
            if age > 0:
                return age
            else:
                align_tab("Age must be a positive integer")
        except ValueError:
            align_tab("Age must be an integer data type")


while True:
    print("*" * 100)
    align_center("Welcome to HpolyFintech Service")
    print()
    align_center("Enter either [R to register, W to withdraw, D to deposit, C to check balance, B for balance]")
    align_center("Enter exit to close Application")

    choice = input("\t$ ")

    if choice.lower() == "r":
        register_data()
    elif choice.lower() == "w":
        withdrawal_check()
    elif choice.lower() == "d":
        deposit_check()


        # Study the code above, depending on how you implemented the rest of your features like deposit, withdrawal, etc
        # in hpolyFintech.py, implement other choices to execute the needed functions
        # Ensure to use align_tab to print all text returned from your called functions if the text is aligned to
        # the left, or use align_center if the text is aligned to the center or use print function only
        # where it is crucial and necessary if any

    elif choice.lower() == "exit":
        print()
        align_center("GOOD BYE")
        print("*" * 100)
        break
