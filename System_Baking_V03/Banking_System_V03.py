import textwrap

class Client:
    def __init__(self, cpf, name, birthdate, address):
        self.cpf = cpf
        self.name = name
        self.birthdate = birthdate
        self.address = address

class NaturalPerson(Client):
    pass

class Account:
    def __init__(self, agency, account_number, user):
        self.agency = agency
        self.account_number = account_number
        self.user = user
        self.balance = 0

class CheckingAccount(Account):
    def __init__(self, agency, account_number, user):
        super().__init__(agency, account_number, user)
        self.LIMIT = 3
        self.number_withdrawal = 0
        self.limit_withdrawal = 500.00

    def deposit(self, value_deposit):
        if value_deposit > 0:
            self.balance += value_deposit
            print("Deposit made successfully")
        else:
            print("Invalid value.")
        return self.balance

    def withdrawal(self, value_withdrawal):
        if value_withdrawal <= 0:
            print("Value Invalid!")

        elif self.number_withdrawal >= self.LIMIT or value_withdrawal > self.limit_withdrawal:
            print("Limit of withdrawal daily reached or Value of the withdrawal is bigger than 500.00.")

        elif value_withdrawal > self.balance:
            print(f"Value of the withdrawal is bigger than balance. Your balance is {self.balance}")

        else:
            self.number_withdrawal += 1
            self.balance -= value_withdrawal
            print("Withdrawal made successfully!")

        return self.balance, self.number_withdrawal

class Statement:
    def __init__(self, balance):
        self.balance = balance

    def display(self):
        print(f"Balance of the account is R${self.balance}")
        return self.balance

class BankSystem:
    def __init__(self):
        self.accounts = []
        self.users = []
        self.AGENCY = "0001"
        self.account_number = 0

    def menu(self):
        menuscreen = '''
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

    def user_registration(self):
        cpf = input("Type your CPF (only numbers): ")
        if self.filter_users(cpf):
            print("User already taken.")
            return

        name = input("Type your name: ")
        birthdate = input("Type your birthdate: ")
        address = input("Type your address (address - number - neighborhood - city/states): ")

        user = NaturalPerson(cpf, name, birthdate, address)
        self.users.append(user)
        print("Successfully Registered!")

    def filter_users(self, cpf):
        for user in self.users:
            if user.cpf == cpf:
                return True
        return False

    def account_registration(self):
        cpf = input("Type your CPF (only numbers): ")
        user = self.filter_users(cpf)
        if user:
            self.account_number += 1
            account = CheckingAccount(self.AGENCY, self.account_number, cpf)
            self.accounts.append(account)
            print("Successfully Account Registered!")
        else:
            print("User not registered")

    def list_account(self):
        for account in self.accounts:
            lin = f'''
            Agency: {account.agency}
            Account: {account.account_number}
            User: {account.user}
            Balance: {account.balance}
            '''
            print("=" * 100)
            print(textwrap.dedent(lin))

    def list_user(self):
        for user in self.users:
            lin = f'''
            CPF: {user.cpf}
            Name: {user.name}
            Birthdate: {user.birthdate}
            Address: {user.address}
            '''
            print("=" * 100)
            print(textwrap.dedent(lin))

    def main(self):
        while True:
            self.menu()
            select_option = int(input("What's the operation you would like to carry out: "))

            if select_option == 1:  # Deposit
                account_number = int(input("Enter your account number: "))
                account = self.accounts[account_number - 1]
                value_deposit = float(input("What value would you like to deposit: "))
                account.deposit(value_deposit)

            elif select_option == 2:  # Withdrawal
                account_number = int(input("Enter your account number: "))
                account = self.accounts[account_number - 1]
                value_withdrawal = float(input("What value would you like to withdraw: "))
                account.withdrawal(value_withdrawal)

            elif select_option == 3:  # Bank Statement
                account_number = int(input("Enter your account number: "))
                account = self.accounts[account_number - 1]
                statement = Statement(account.balance)
                statement.display()

            elif select_option == 4:  # Account Registration
                self.account_registration()

            elif select_option == 5:  # User Registration
                self.user_registration()

            elif select_option == 6:  # List Account
                self.list_account()

            elif select_option == 7:  # List User
                self.list_user()

            else:
                if select_option == 0:  # Exit
                    print("Thank you!")
                    break

if __name__ == "__main__":
    bank_system = BankSystem()
    bank_system.main()
