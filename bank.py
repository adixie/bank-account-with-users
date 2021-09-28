class BankAccount:

        def __init__(self, account_balance = 0, interest_rate = 0.05): 
                self.account_balance = account_balance
                self.interest_rate = interest_rate

        def deposit(self, amount, accountType):
                self.account_balance += amount
                return self

        def withdraw(self, amount):
                self.account_balance -= amount
                return self
        
        def display_account_info(self):
                print(self.account_balance)

        def yield_interest(self):
                interest_yield = 0
                interest_yield += self.account_balance * self.interest_rate + self.account_balance
                print(interest_yield)