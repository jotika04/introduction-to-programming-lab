listofcars = [] #create array
listofbus = []  #create array
listoftruck = [] #create array

class Car :
    def __init__(self, car):
        self.car = car  #declares truck
    def get_car(self):
        return  self.car #return to get car
class Bus :
    def __init__(self, bus):
        self.bus = bus #declares truck
    def get_bus(self):
        return self.bus #return to get bus
class Truck :
    def __init__(self, truck):
        self.truck = truck #declares truck
    def get_truck(self):
        return self.truck #return to get truck
class Vehicle :
    def addcar(self):
        listofcars.append(Car.get_car)  #add the vehicle to the array
    def addbus(self):
        listofcars.append(Bus.get_bus)#add the vehicle to the array
    def addtruck(self):
        listoftruck.append(Truck.get_truck) #add the vehicle to the array

restart = "y"
car_fee = 6000  #define the fee for car
bus_fee = 8000  #define the fee for car
truck_fee = 10000   #define the fee for car

while restart != "n":
    print("1.car\n2.bus\n3.truck")
    usrinput = input("what is your vehicle type : ") #user input their vehicle

    if usrinput == "1":
        print("fee :{}".format(car_fee))    #prints the fee
        menu = input("Is there any other vehicle ? (Y/N) =>").upper() #give user choice to continue to other vehicle
        if menu == "N":
           print("Have a nice day ? i guess.")
           break            #end program
    if usrinput == "2":
        print("fee:{}".format(bus_fee))#prints the fee
        menu = input("Is there any other vehicle ? (Y/N) =>").upper()   #give user choice to continue to other vehicle
        if menu == "N":
           print("Have a nice day ? i guess.")
           break            #end program
    if usrinput == "3":
        print("fee :{}".format(truck_fee))#prints the fee
        menu = input("Is there any other vehicle ? (Y/N) =>").upper() #give user choice to continue to other vehicle
        if menu == "N":
           print("Have a nice day ? i guess.")
           break            #end program
