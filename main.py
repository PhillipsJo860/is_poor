# Joshua Phillips
# 5/6/25
# Three Ways to Modify BankAccount Class Attributes

class BankAccount():
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'${amount} has been added to your balance.')
        elif amount <= 0:
            print('Invalid deposit amount.')
    
    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            print(f'${amount} has been withdrawn.')
        elif amount <= 0:
            print('Invalid withdraw amount.')
    
    def get_balance(self, ):
        return self.balance
    
    def display_info(self):
        print()
        print(f'This account waws created today by, {self.account_holder} with a current balance of ${self.balance}.')
        print()

my_account = BankAccount('Joshua', 148)
print(my_account)
my_account.display_info()
my_account.deposit(198)
my_account.display_info()
my_account.deposit(33)
my_account.display_info()
my_account.deposit(130)
my_account.display_info()
my_account.withdraw(507)
my_account.display_info()