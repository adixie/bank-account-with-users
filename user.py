from bank import BankAccount

class User:
    def __init__(self, name, email_address,):
        self.name = name
        self.email = email_address
        self.account = BankAccount()

    def makeDeposit(self, amount):
        self.account.account_balance += amount
        return self

    def makeWithdrawal(self, amount):
        self.account.account_balance -= amount
        return self

    def displayUserBalance(self):
        print(self.name)
        print(self.account.account_balance)

    def transferMoney(self, transfer, amount):
        self.account.account_balance -= amount
        transfer.account.account_balance += amount
        self.displayUserBalance()
        transfer.displayUserBalance()

Sarah = User("Sarah", "sarah@email.com")

Mike = User("Mike", "mike@email.com")

Sarah.makeDeposit(100)
Sarah.makeWithdrawal(20)
Sarah.displayUserBalance()

Sarah.transferMoney(Mike, 20)