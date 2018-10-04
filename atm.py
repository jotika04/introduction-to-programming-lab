#An ATM program
class account:
    def __init__(self, name, balance):  #intialize name and balance
        self.name = name                #declare that "name" is in the class account
        self.balance = balance          #declares that "balance" is in the class account

    def get_name(self):                 #creates a function to get and show the name
        return self.name

    def get_money(self):                #creates a function to get and show the money
        return self.money

    def balance(self):                  #creates a function to show your balance
        return self.balance

    def deposit(self,amount,money):     #create a function to deposit the money
        self.amount = float(amount)     #declare amount and money to be in the class
        self.money = float(money)
        if self.amount > 0:             #the amount you want to depost must be more than 0
            if self.money > self.amount:   #if you have more money than the amount it will run the code
                self.balance += self.amount #add amount to balance
                self.money -= self.balance  #subtract amount from money
                return print("your balance is : {} cash : {}".format(self.balance, self.money))
            else:# it will show your balance and cash atm
                return print("get some money")#it will print this if you dont have enough money

    def withdraw(self,amount):          #create a function to withdraw
        self.amount = float(amount)     #declare amount to be in this class
        if self.balance >=self.amount:  #if the balance is more than amount run the code
            self.balance -= self.amount #subtract balance by the amount
            self.money += self.amount   #add amount to money
            return print("balance : {} cash : {}".format(self.balance, self.money))
            #shows balance and cash you have now
    def debit(self,amount):             #create a function to use debit
        self.amount = float(amount)     #declare amount to be in the class
        if self.balance >= self.amount: #if balance is more than amount
                self.money += 0         #it wont add your money
                return print("balance : {} cash : {}".format(self.balance, self.money))
        else:     #shows balance and cash at the moment
                return print("you don't enough balance")
                    #if balance is less than amount print that
usrinput = input("enter full name here :")  #input name
a =account(usrinput,0)  #sets your account balance to 0
cash =input("enter how much cash you have :")   #inputs how much cash u have
print("u have","Rp.",cash)  #print your cash

while True : #if condition true
    print("welcome to the TT bank ATM\nThis list is what can you do :\n1.Deposit\n2.Withdraw\n3.Debit\n4.Check Account Balance\n5.quit")
    options = input("what do you want to do :") #user inputs what to do

    if options == "1":  #if user input 1 it will run deposit
        amount =float(input("enter your amount :")) #enter amount
        print(a.deposit(amount,cash))

    elif options =="2": #if user input 2 run withdraw
        amount =float(input("enter your amount :")) #input amount
        print(a.withdraw(amount))

    elif options =="3": #if user input 3 run debit
       amount =float(input("enter your amount :"))#input amount
       print(a.debit(amount))

    elif options =="5":                         #exits the program
        print("thank you for using the ATM")
        break

