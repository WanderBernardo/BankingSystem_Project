# Banking System: Deposit, Withdrawal and Extract
For the first version of the system we must implement only 3 operations: deposit, withdrawal and statement.

**Deposit operation**

It must be possible to deposit positive amounts into my bank account. v1 of the project only works with 1 user, so we don't need to worry about identifying the branch and bank account number. All deposits must be stored in a variable and displayed in the statement operation.

**Withdrawal operation**

The system must allow you to make 3 daily withdrawals with a maximum limit of R$500.00 per withdrawal. If the user does not have a balance in their account, the system must display a message stating that it will not be possible to withdraw the money due to lack of balance. All withdrawals must be stored in a variable and displayed in the statement operation.

**Operação de extrato**

This operation must list all deposits and withdrawals made to the account. At the end of the list, the current account balance should be displayed. If the statement is blank, display the message: No transactions were carried out.
The values ​​must be displayed using the format R$ xxx.xx, example:
1500.45 = R$ 1500.45
