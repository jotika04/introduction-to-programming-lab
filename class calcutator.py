class calculator :                              #class calculator
    def __init__(self,num1,num2):               #initialize the numbers
        self.nm1 = num1                         #give the intialized numbers a varible
        self.nm2 = num2                         #give the initialized number a variable
    def add(self):                              #function to add the numbers
        return self.nm1 + self.nm2
    def sub(self):                              #function to subtract the numbers
        return self.nm1 - self.nm2
    def multi(self):                            #function to multiply the two numbers
        return self.nm1 * self.nm2
    def div(self):                              #function to divei the two numbers
        return self.nm2 /self.nm2

fnum = int(input("enter first number :"))       #inputs the first number
list_opt = ["+", "-", "*" ,"/"]                 #list the kind of operator used
print(list_opt)                                 #prints the list to tell what u can use
opt = input("what math symbol to use :")        #inputs what kind of operator you want
snum =int(input("enter the second number :"))   #inpuits the second number

list_opt = ["+", "-", "*" ,"/"]                 #list the kind of operator used

if opt == list_opt[0]:                          #checks the input operator and compare the first element on list
    cl =calculator(fnum,snum)                   #creates the cal variable to call the calculator class
    print(cl.add())                             #prints the result
elif opt == list_opt[1]:                        #checks the input operator and compares the second element the list
    cl = calculator(fnum,snum)                  #created the variable cal to call the calculatr class
    print(cl.sub())                             #prints the result
elif opt == list_opt[2]:                        #checks the input operator and compares the third element
    cl = calculator(fnum,snum)                  #created the variable cal to call the calculatr class
    print(cl.multi())                           #prints the result
elif opt == list_opt[3]:                        #check the input operator and compares the last element
    cl = calculator(fnum,snum)                  #created the variable cal to call the calculatr class
    print(cl.div())                             #prints the result

