star=int(input("number star :"))    #user inputs a number
for x in range (0,star):    #set the range for how many stars
    print("*"*(x + 1),end="")     #loop to get the star to make a triangle
    print()

for x in range (0,star):                #it will define the range of the program
    print (" "*((star-x)-1),"*"*(x+1))  #it will create the space needed to make then make the stars after the spaces
print()                                 #then it makes the stars then add another one at the bottom by removing a space

for x in range (0,star):
    print ("*"*(star-x))       #
print ()

for x in range (0,star):
    print (" "*x,"*"*(star-x))
print()

for x in range (0,star):
    print (" "*(star-x),"*"*(x*2-1))
print ()

for x in range (0,star):
    print (" "*(star-x),"*"*(x*2-1))
for x in range (0,star):
    print (" "*x,"*"*((star-x)*2-1))
