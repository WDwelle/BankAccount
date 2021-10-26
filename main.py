class Bank_Account:
    bank_name = "Dojo Bank"
    all_accounts = []
    def __init__(self, balance, int_rate,):
        self.int_rate = int_rate
        self.balance = balance
        Bank_Account.all_accounts.append(self)

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


Business = Bank_Account(500, .05)
Saver = Bank_Account(200, .1)
Investment = Bank_Account(1500, .35)

#Investment.deposit(1000).deposit(500).deposit(3500).withdraw(1500).yeild_interest()

#Business.deposit(1200).deposit(600).withdraw(20).withdraw(20).withdraw(78).withdraw(15).yeild_interest().display_account_info()


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = Bank_Account(0,.02)
    # adding the deposit method
    def make_deposit(self):
        self.account.deposit(100)
        print(self.account.balance)
        return self

    def make_withdrawl(self):
        self.account.withdraw(20)
        print(self.account.balance)
        return self

    def display_user_balance(self):
        print(self.name , "$",self.account_balance)
        return self

    def transfer(self, amount, other_user):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(self.account_balance)
        print(other_user.account_balance)
        return self

Will = User("Will Dwelle", "ww@coolguy.com")
Gianna = User("Gianna Dwelle", "GW@selfcare.org")
Dad = User("Denzil Dwelle", "dd@blah.com")


Dad.make_deposit()