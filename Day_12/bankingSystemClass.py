class Bank:
    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"Amount Deposited: {amount}\nBalance: {self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print(f"Withdraw amount: {amount}\nRemaining Balance: {self.balance}")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

acc = Bank(1000)
acc.check_balance()
acc.deposit(9191)
acc.withdraw(12000)