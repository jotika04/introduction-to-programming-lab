class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_balance(self):
        return self.balance
    def get_name(self):
        return self.name


class ATM(Account):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        # super(Account, self).__init__() #inheritance by relying on super function
        Account.__init__(self, self.name, self.balance) #inheritance by uisng class name

    def deposit(self, amount):
        self.amount = float(amount)
        if self.amount > 0:
            self.balance += self.amount
            return "your balance is {}".format(self.balance)
        else:
            return "you need money to  deposit"

    def withdraw(self, amount):
        self.amount = float(amount)
        if self.amount < self.balance:
            self.balance -= self.amount
            return "your balance is {}, and your have {}".format(self.balance, self.amount)
        elif self.amount > self.balance:
            return "you don't have enough balance"

def main():
    #  declaring the objects
    # akunJotika = Account("Jotika", 0) #Creating an object called akunJotika that based from Account class
    atmBCA = ATM("Jotika", 0)

    # akunJotika.get_name()
    print("Name: {}".format(atmBCA.get_name()))
    print("Balance: ", atmBCA.get_balance())

    while True:
        print("welcome to the ATM")
        print("Name: {}".format(atmBCA.get_name()))
        print("Balance: ", atmBCA.get_balance())
        print("1.deposit\n2.witdraw")
        usrinput=input("what do you wan to do ?\n==>")
        if usrinput == "1":
            mnyinput = int(input("how much do you want to deposit ?\n==>"))
            atmBCA.deposit(mnyinput)
        elif usrinput == "2":
            mnyinput2 = int(input("how much do you want to withdraw ?\n==>"))
            atmBCA.withdraw(mnyinput2)

main()
