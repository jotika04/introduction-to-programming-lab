class Car :                 #create car class
    def __init__(self, car):
        self.car = car
    def get_car(self):
        return  self.car

class Bus :                 #create bus class
    def __init__(self, bus):
        self.bus = bus
    def get_bus(self):
        return self.bus

class Truck :               #create truck class
    def __init__(self, truck):
        self.truck = truck
    def get_truck(self):
        return self.truck

class Tollgate(Car,Bus,Truck):  #make a class for toll gate

    def __init__(self,type):    #make the class a super class
        super().__init__(type)

    def car_fee(self):
        Car.get_car = 6000 #creates fee for car
        return Car.get_car
    def bus_fee(self):
        Bus.get_bus = 8000  #creates fee for bus
        return Bus.get_bus
    def truck_fee(self):
        Truck.get_truck =10000 #creates fee for truck
        return Truck.get_truck

class Tollgate2(Car,Bus,Truck):  #make a second class for another toll gate

    def __init__(self,type):    #make the class a super class
        super().__init__(type)

    def car_fee(self):
        Car.get_car = 18000 #creates fee for car
        return Car.get_car
    def bus_fee(self):
        Bus.get_bus = 20000  #creates fee for bus
        return Bus.get_bus
    def truck_fee(self):
        Truck.get_truck = 25000 #creates fee for truck
        return Truck.get_truck


restart = "Y"
def toll_operator():
    carlist = 0 #total car
    buslist = 0 #total bus
    trucklist = 0 #total truck
    carlist2 = 0  #total car 2
    buslist2 =0     #total bus 2
    trucklist2 = 0 #total bus 2
    while restart != "N" :  #create the loop
        print("locations:\nmeruya\npondok aren")
        location =input("your location :".lower()) #user input location he/she is in and make a lower case word
        if location == "meruya":
            print("1.car\n2.bus\n3.truck")
            usrinput = input("what is your vehicle type ? ==>") #user input
            gate = Tollgate(usrinput)   #create variable of the class
            gate2 =Tollgate2(usrinput)  #variable for the second class
            if usrinput == "1":
                print("fee ==>",gate.car_fee()) #print the fee
                carlist += 1    #adds the number of car
                print ("there is ",carlist,"car")
                menu = input("Is there any other vehicle ? (Y/N) =>").upper() #use input and upper to make it a capital letter
                if menu == "N":
                    print("toll meruya")
                    print("CAR  BUS  TRUCK")
                    print("{}     {}     {}".format(carlist,buslist,trucklist)) #prints the total of each vehicle
                    revenue = (gate.car_fee()*carlist + gate.bus_fee()*buslist + gate.truck_fee()*trucklist) #adds all total value of the vehicles
                    print("total revenue ==>",revenue)  #prints the total revenue

                    print("toll pondok aren")
                    print("CAR  BUS  TRUCK")
                    print("{}     {}     {}".format(carlist2,buslist2,trucklist2)) #prints the total of each vehicle
                    revenue2 = (gate2.car_fee() *carlist2 + gate2.bus_fee()*carlist2 + gate2.truck_fee()*trucklist2) #adds the total value from pondok aren
                    print("total revenue ==> Rp.{}".format(revenue2))
                    grandtotal = (revenue + revenue2)
                    print("grand total revenue Rp.{}".format(grandtotal)) #the grand total of all revenues
                    print("Have a nice day ? i guess.")
                    break   #end program

            elif usrinput == "2":
                print("fee ==>",gate.bus_fee()) #prints the fee
                buslist += 1
                print ("there is",buslist,"buses")
                menu = input("Is there any other vehicle ? (Y/N) =>").upper()#use input and upper to make it a capital letter
                if menu == "N":
                    print("toll meruya")
                    print("CAR  BUS  TRUCK")
                    print("{}     {}     {}".format(carlist,buslist,trucklist))     #prints the total of each vehicle
                    revenue = (gate.car_fee()*carlist + gate.bus_fee()*buslist + gate.truck_fee()*trucklist) #adds all total value of the vehicles
                    print("total revenue ==>",revenue)  #prints the total revenue

                    print("toll pondok aren")
                    print("CAR  BUS  TRUCK")
                    print("{}     {}     {}".format(carlist2,buslist2,trucklist2)) #prints the total of each vehicle
                    revenue2 = (gate2.car_fee() *carlist2 +gate.bus_fee()*carlist2+gate.truck_fee()*trucklist2)#adds the total value from pondok aren
                    print("total revenue ==> Rp.{}".format(revenue2)) #prints the second revenue
                    grandtotal = (revenue + revenue2)
                    print("grand total revenue Rp.{}".format(grandtotal)) #the grand total of all revenues
                    print("Have a nice day ? i guess.")
                    break   #end program

            elif usrinput == "3":
                print ("fee ==>",gate.truck_fee())  #prints the fee
                trucklist += 1
                print("there is ",trucklist,"trucks")
                menu = input("Is there any other vehicle ? (Y/N) =>").upper()#use input and upper to make it a capital letter
                if menu == "N":
                    print("CAR  BUS  TRUCK")
                    print("{}     {}     {}".format(carlist,buslist,trucklist)) #prints the total of each vehicle
                    revenue = (gate.car_fee()*carlist + gate.bus_fee()*buslist + gate.truck_fee()*trucklist) #adds all total value of the vehicles
                    print("total revenue ==>Rp.",revenue) #prints the total revenue

                    print("toll pondok aren")
                    print("CAR  BUS  TRUCK")
                    print("{}     {}     {}".format(carlist2,buslist2,trucklist2)) #prints the total of each vehicle
                    revenue2 = (gate2.car_fee() *carlist2 +gate2.bus_fee()*carlist2+gate.truck_fee()*trucklist2)#adds the total value from pondok aren
                    print("total revenue ==> Rp.{}".format(revenue2)) #prints the second revenue
                    grandtotal = (revenue + revenue2)
                    print("grand total revenue Rp.{}".format(grandtotal)) #the grand total of all revenues
                    print("Have a nice day ? i guess.")
                    break   #end program

        elif location == "pondok aren":
            print("1.car\n2.bus\n3.truck")
            usrinput = input("what is your vehicle type ? ==>") #user input
            gate = Tollgate(usrinput)   #create variable of the class
            gate2 =Tollgate2(usrinput)
            if usrinput == "1":
                print("fee ==>",gate2.car_fee()) #print the fee
                carlist2 += 1    #addds the number of car
                print ("there is ",carlist2,"car")
                menu = input("Is there any other vehicle ? (Y/N) =>").upper() #use input and upper to make it a capital letter
                if menu == "N":
                    print("toll meruya")
                    print("CAR  BUS  TRUCK")
                    print("{}     {}     {}".format(carlist,buslist,trucklist)) #prints the total of each vehicle
                    revenue = (gate.car_fee()*carlist + gate.bus_fee()*buslist + gate.truck_fee()*trucklist) #adds all total value of the vehicles
                    print("total revenue ==>",revenue)  #prints the total revenue

                    print("toll pondok aren")
                    print("CAR  BUS  TRUCK")
                    print("{}     {}     {}".format(carlist2,buslist2,trucklist2)) #prints the total of each vehicle
                    revenue2 = (gate2.car_fee() *carlist2 +gate2.bus_fee()*carlist2+gate2.truck_fee()*trucklist2)#adds the total value from pondok aren
                    print("total revenue ==> Rp.{}".format(revenue2)) #prints the second revenue
                    grandtotal = (revenue + revenue2)
                    print("grand total revenue Rp.{}".format(grandtotal)) #the grand total of all revenues
                    print("Have a nice day ? i guess.")
                    break   #end program

            elif usrinput == "2":
                print("fee ==>",gate2.bus_fee()) #prints the fee
                buslist2 += 1
                print ("there is",buslist2,"buses")
                menu = input("Is there any other vehicle ? (Y/N) =>").upper()#use input and upper to make it a capital letter
                if menu == "N":
                    print("toll meruya")
                    print("CAR  BUS  TRUCK")
                    print("{}     {}     {}".format(carlist,buslist,trucklist))     #prints the total of each vehicle
                    revenue = (gate.car_fee()*carlist + gate.bus_fee()*buslist + gate.truck_fee()*trucklist) #adds all total value of the vehicles
                    print("total revenue ==>",revenue)  #prints the total revenue

                    print("toll pondok aren")
                    print("CAR  BUS  TRUCK")
                    print("{}     {}     {}".format(carlist2,buslist2,trucklist2)) #prints the total of each vehicle
                    revenue2 = (gate2.car_fee() *carlist2 +gate2.bus_fee()*carlist2+gate2.truck_fee()*trucklist2)#adds the total value from pondok aren
                    print("total revenue ==> Rp.{}".format(revenue2)) #prints the second revenue
                    grandtotal = (revenue + revenue2)
                    print("grand total revenue Rp.{}".format(grandtotal)) #the grand total of all revenues
                    print("Have a nice day ? i guess.")
                    break   #end program

            elif usrinput == "3":
                print ("fee ==>",gate2.truck_fee())  #prints the fee
                trucklist2 += 1
                print("there is ",trucklist2,"trucks")
                menu = input("Is there any other vehicle ? (Y/N) =>").upper()#use input and upper to make it a capital letter
                if menu == "N":
                    print("CAR  BUS  TRUCK")
                    print("{}     {}     {}".format(carlist,buslist,trucklist)) #prints the total of each vehicle
                    revenue = (gate.car_fee()*carlist + gate.bus_fee()*buslist + gate.truck_fee()*trucklist) #adds all total value of the vehicles
                    print("total revenue ==>Rp.",revenue) #prints the total revenue

                    print("toll pondok aren")
                    print("CAR  BUS  TRUCK")
                    print("{}     {}     {}".format(carlist2,buslist2,trucklist2)) #prints the total of each vehicle
                    revenue2 = ((gate2.car_fee() * carlist2) + (gate2.bus_fee()*carlist2) + (gate2.truck_fee()*trucklist2))#adds the total value from pondok aren
                    print("total revenue ==> Rp.{}".format(revenue2))
                    grandtotal = (revenue + revenue2)
                    print("grand total revenue Rp.{}".format(grandtotal)) #the grand total of all revenues
                    print("Have a nice day ? i guess.")
                    break   #end program
toll_operator() #run the toll program
