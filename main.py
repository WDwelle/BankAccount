class Bank_Account:
    all_accounts = []
    def __init__(self, bank_name, int_rate,):
        self.name = bank_name
        self.int_rate = int_rate
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print("Balnce $", self.balance)

    def yeild_interest(self):
        if self.balance >= 0:
            self.balance += self.int_rate*self.balance
            print(self.balance)
            return self
        else:
            print("Declined")




Will = Bank_Account("Dojo Bank", .05)
Gianna = Bank_Account("AnyBank", .1)
Dad = Bank_Account("Money Planet", .35)

Dad.deposit(1000).deposit(500).deposit(3500).withdraw(1500).yeild_interest()

Will.deposit(1200).deposit(600).withdraw(20).withdraw(20).withdraw(78).withdraw(15).yeild_interest().display_account_info()



