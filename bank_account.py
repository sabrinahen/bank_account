class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
            print(self.balance)
            
        else:
            self.balance -= amount
            print(self.balance)
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            print(self.balance)
        else:
            print(self.balance)
        return self

sabrina = BankAccount(0.01, 10000)
brian = BankAccount(0.02, 800)

sabrina.deposit(100).deposit(100).deposit(100).withdraw(350).yield_interest().display_account_info()
brian.deposit(500).deposit(300).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()
