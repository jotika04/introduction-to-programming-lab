star=int(input("number star :"))    #user inputs a number
for x in range (0,star):    #set the range for how many stars
    print("*"*(x + 1),end="")     #loop to get the star to make a triangle
    print()

for x in range (0,star):                #it will define the range of the program
    print (" "*((star-x)-1),"*"*(x+1))  #it will create the space needed to make then make the stars after the spaces
print()                                 #then it makes the stars then add another one at the bottom by removing a space

for x in range (0,star):                #defines range of thr program
    print ("*"*(star-x))               #loop that will print stars by the number of input

for x in range (0,star):                #define the number of range in the program
    print (" "*x,"*"*(star-x))          #it makes the space cause it is a reverse triangle and make the stars
print()                                 #to make a blank line to give space between programs

for x in range (0,star):                #define ranges of the program
    print (" "*(star-x),"*"*(x*2-1))    #makes a space first then create a star so that it can make a triangle
print ()                                #makes a blank line to give space between programs

for x in range (0,star):                #give the program a range
    print (" "*(star-x),"*"*(x*2-1))    #makes a triangle first with space and thena  star
for x in range (0,star):                #give the program a range
    print (" "*x,"*"*((star-x)*2-1))    #makes a reverse triangle by changeing some of the code

