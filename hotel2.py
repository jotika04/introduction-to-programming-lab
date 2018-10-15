class Single :                  #class for the single bedroom
    def __init__(self,sroom):
        self.room1 = sroom
    def get_single(self):
        return self.room1

class Double :                  #class for double bedroom
    def __init__(self, droom):
        self.room2 = droom
    def get_double(self):
        return self.room2

class Hotel(Single,Double):
    def __init__(self,type):
        super().__init__(type)      #declares super class
    def get_feesingle(self):
        Single.get_single = 15000   #gives amount of money
        return Single.get_single
    def get_feedouble(self):
        Double.get_double = 30000   #gives amount of money
        return Double.get_double


def hotel_operator():
    singlelist = 0
    doublelist = 0
    price1 =[] #empty list
    price2 = [] #empty list
    while True:
        print("1.check in\n2.check out\n3.quit")
        usrinput = input("check in or check out ?\n ==>".lower()) #give user inpupts and make it to lower case alphabets
        htl = Hotel(usrinput)   #give variable to hotel class

        if usrinput == "1": #loop
            y = input("do you want single or double beds?\n==> ")
            if y == "single": # loop to add 1 to the integer
                if singlelist >0:   #check if its occupied
                    print("its is occupied")
                else:
                    singlelist += 1 #add1 to room
                    print("you are checked in")
                    #x1 = int(input("how many nights"))
                    #print(x1,"nights")
            elif y == "double":
                if doublelist > 0 : #checks if its occupied
                    print("it is occupied")
                else:
                    doublelist += 1 #add 1 to the room
                    print("you are checked in")
                    #x2 = int(input("how many nights")) #checks how many night they stay
                    #print(x2,"nights")
        elif usrinput == "2":
            roominput = input("what is your room type?\n==>") #ask user what type is their room
            if roominput == "single":
                x1 =int(input("how many nights"))
                a = htl.get_feesingle() * x1 #gets prize for single
                price1.append(a)
                print(a)
            elif roominput == "double":
                x2=int(input("how many nights"))
                b = htl.get_feedouble() * x2 #gets the prize for double
                price2.append(b)
                print(b)
        elif usrinput == "3":
             totalinput =input("was the hotel full ? (Y/N)".lower())

             if totalinput == "y": #checks if the hotel is full to calculate the total if its full
                print(price1,price2)
                a = price1.pop(0)
                b = price2.pop(0)
                total = a+b  #calculate the total
                print(total)
                print("----------------------------------------------------")
                print("thank you for coming ! and thank you for the quiz !")
                break
             elif totalinput == "n": #if its not full which is filled
                which = input("which one is empty ?(enter room type)\n==>")
                if which == "single": #if single filled run program
                    totalsingle = price1.pop()
                    print(totalsingle)
                    print("----------------------------------------------------")
                    print("thank you for coming ! and thank you for the quiz !")
                    break
                elif which == "double": #if double filled run program
                    totaldouble = price2.pop()
                    print(totaldouble)
                    print("----------------------------------------------------")
                    print("thank you for coming ! and thank you for the quiz !")
                    break


hotel_operator()





