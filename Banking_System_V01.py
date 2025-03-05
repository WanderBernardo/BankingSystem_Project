menuscreen = f'''
################### Welcome the Menu Options ##################

Select between number 1 until number 3 or 0 to exit.

[1] Deposit

[2] Withdrawal

[3] Bank Statement

[0] Exit

###################################################
'''
# Withdrawal #Saque
# Statement #Extrato

invalid_operation = f'''

invalided value. Select between number 1 until number 3 or 0 to exit."

'''

value_deposit = 0.00
balance = 0.00
BALANCE_DAILY = 3
Limit_withdrawal_daily = 0
MAXIMUM_WITHDRAWAL = 500.00
value_withdrawal = 0.00

while True:
        print(menuscreen)
        select_option = float(input ("What's the operation would you like carry out: "))

        if (select_option == 1): # Deposit
                value_deposit = float(input ("What value would you like of deposit:"))
                if (value_deposit <=0):
                        print("invalided value.")
                else:
                        print("Deposit made successfully")
                        balance += value_deposit

                        confirm = bool(input("Would you like execute other operation (Yes or Not):"))
                        if (confirm == False):
                                break
                
        elif (select_option == 2): # Withdrawal
                value_withdrawal = float(input("What value would you like of withdrawal:"))
                if (value_withdrawal <= 0):
                        print("Value Invalid!")

                elif (Limit_withdrawal_daily >= BALANCE_DAILY) or (value_withdrawal > MAXIMUM_WITHDRAWAL):
                        print("Limit of withdrawal daily reaching or Value of the withdrawal is begger that 500.00.")

                elif (value_withdrawal > balance):
                        print(f"Value of the withdrawal is bigger that balance. Your balance is {balance}")
                
                else:
                        Limit_withdrawal_daily +=1
                        balance -= value_withdrawal
                        print("Withdrawal made successfully!")

                        confirm = bool(input("Would you like execute other operation (Yes or Not):"))
                        if (confirm == False):
                                break

        elif (select_option == 3): # Bank Statement
                print (f"balance of the account is {balance}")

                confirm = bool(input("Would you like execute other operation (Yes or Not):"))
                if (confirm == False):
                        break
        elif (select_option == 0): # Exit
                print("Thank you. ")
                break
else:
  print (invalid_operation)
  print(menuscreen)
        

