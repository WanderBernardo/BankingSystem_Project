# Banking System - Version 02

For the second version of the system we must implement operations: deposit, withdrawal and statement in Functions and include two new functions: Account Registration and User Registration.

**General Objective** 
- Separate the functions existing of withdrawal, deposit and statement in function;
- Create new functions: User Registration and Account Registration.

**Withdrawal:**

The function need to receive the arguments only for name (keyword only).
 - Sugestion of the arguments: balance, value, statement, limit, number_withdrawal, llimit_withdrawal.
 - Sugestion of return: balance and statement.

**Deposit:**

The function need to receive the arguments only for position (positional only).
- Sugestion of arguments: balance, value, statement.
- Sugestion of return: balance and statement.

**Statement:**

The statement function need to receive the arguments for position and name (positional only and keyword only).
- Position Arguments: balance.
- Named Arguments: statement.

**User Registration:**

Program need to storage the user in a list, a user is compound for: Name, Birthday date, CPF and Address.
- Address: is string in format: public place - number - neighborhood - city/acronym of state.
- CPF: only number
- it cannot registration two user with same number CPF.

**User Registration:**

Program need to storage accounts in a list, a account is compound for: bank agency number, account number and user.
- Account number: sequential, inicial: 0001.
- User can has of one account, but a account belongs the only a user.

