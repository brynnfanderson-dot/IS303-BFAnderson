from bankaccount import BankAccount

#create bank account
user_name = input("Welcome to the Bank! Please enter your name: ")

#generate bank account starting info
account_info = BankAccount(user_name)

#Display opening menu
menu_choice = int(input("Please choose an option: \n1. Make a deposit \n2. Make a withdrawal \n3. View account information \n4. Quit \n:"))

while menu_choice != 4:
    if menu_choice == 1:
        account_info.make_deposit()
    elif menu_choice == 2:
        account_info.make_withdrawal()
    elif menu_choice == 3:
        account_info.view_acount()
    else:
        print("Invalid option, please try again")
    
    #Display opening menu
    menu_choice = int(input("Please choose an option: \n1. Make a deposit \n2. Make a withdrawal \n3. View account information \n4. Quit \n:"))


