import textwrap

def menu():
        menuscreen = f'''
        ################### Welcome the Menu Options ##################

        Select between number 1 until number 3 or 0 to exit.

        [1] Deposit

        [2] Withdrawal

        [3] Bank Statement

        [4] Account Registration

        [5] User Registration

        [6] List Account

        [7] List User

        [0] Exit

        ###################################################
        '''
        
        print(menuscreen)
        
def deposit(balance, value_deposit, /):
        if (value_deposit > 0):
                balance += value_deposit
                print("Deposit made successfully")
        else:
                print("invalided value.")

        return balance

def withdrawal(* , balance, value_withdrawal, LIMIT, number_withdrawal, limit_withdrawal):
        if (value_withdrawal <= 0):
                print("Value Invalid!")

        elif (number_withdrawal >= LIMIT) or (value_withdrawal > limit_withdrawal):
                print("Limit of withdrawal daily reaching or Value of the withdrawal is begger that 500.00.")

        elif (value_withdrawal > balance):
                print(f"Value of the withdrawal is bigger that balance. Your balance is {balance}")
                
        else:
                number_withdrawal +=1
                balance -= value_withdrawal
                print("Withdrawal made successfully!")

        return balance, number_withdrawal

def statement(balance):
        print(f"Balance of the account is R${balance}")
        return balance
      
def user_registration(users):
        
        cpf = str(input("Type your CPF (only numbers): "))

        if(filter_users(cpf, users)):
                print("User already taken.")
                return
        
        name = str(input("Type your name: "))
        birthdate = str(input("Type your birthdate: "))
        address = str(input("Type your address (address - number - neiborhood - city/states): "))

        users.append({"cpf": cpf, "name": name, "birthdate": birthdate, "address": address})

        print("Successfully Resgistration!")
        
        return users, cpf

def filter_users(cpf, users):
        
        for user in users:
                if (user["cpf"] == cpf):
                        return True
        else:
                return False

def account_registration(AGENCY, account_number, users):
        cpf = str(input("Type your CPF (only numbers): "))
        user = filter_users(cpf, users)
        if user:
                print("Successfully Account Registration!")
                
                return {"AGENCY": AGENCY, "account_number": account_number, "user": users}
        
        print("User not registered")
            
def list_account(accounts):
        for account in accounts:
                lin = f'''
                        Agency: {account['AGENCY']}
                        Account: {account['account_number']}
                        User: {account['user']}
                '''
                print("="*100)
                print(textwrap.dedent(lin))

def list_user(users):
        for user in users:
                lin = f'''
                        CPF: {user['cpf']}
                        Name: {user['name']}
                        Birthdate: {user['birthdate']}
                        Address: {user['address']}
                '''
                print("="*100)
                print(textwrap.dedent(lin))        

def main():
        balance = 0
        LIMIT = 3
        number_withdrawal = 0
        limit_withdrawal = 500.00
        account_number = 0
        users = []
        accounts = []
        AGENCY = "0001"

        while True:

                menu()

                select_option = int(input ("What's the operation would you like carry out: "))

                if (select_option == 1): # Deposit
                        value_deposit = float(input ("What value would you like of deposit: "))
                        
                        balance = deposit(balance, value_deposit)
                
                elif(select_option == 2): # Withdrawal
                        value_withdrawal = float(input("What value would you like of withdrawal: "))

                        balance, number_withdrawal = withdrawal(
                                balance = balance,
                                value_withdrawal = value_withdrawal,
                                LIMIT = LIMIT,
                                number_withdrawal = number_withdrawal,
                                limit_withdrawal = limit_withdrawal
                        )

                elif(select_option == 3): # Bank Statement
                        balance = statement(balance)
                
                elif(select_option == 4): # Account Registration
                        account_number = len(accounts) + 1
                        account = account_registration(AGENCY, account_number, users)
                        if account:
                                accounts.append(account)
                                
                elif(select_option == 5): # User Registration
                        user_registration(users)

                elif(select_option == 6): # List Account
                        list_account(accounts)

                elif(select_option == 7): # List User
                        list_user(users)

                else:
                        if (select_option == 0): # Exit
                                print("Thank you!")
                                break
        

main()