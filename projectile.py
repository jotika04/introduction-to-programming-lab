import numpy as np
import matplotlib.pylab as plot
import math as m

vo = int(input("velocity ==>"))
a = float(input("angle ==>"))
g = 9.81

theta = np.radians(a)
t_max =2*(vo*m.sin(theta)/g)
t = np.linspace(0, t_max, num=1000) #set the time as continuous parameter\
x1 =[]
y1= []
for k in t:
    x =((vo*k)*np.cos(theta))
    y = ((vo*k)*np.sin(theta)-((0.5*g)*(k**2)))
    x1.append(x)
    y1.append(y)
p =[i for i, j in enumerate(y1) if j< 0] #dont'fall through the floor
for i in sorted(p, reverse = True):
    del x1[i]
    del y1[i]
plot.plot(x1, y1)
plot.title("projectile lol !!", fontsize = 25, color= "black")
plot.ylabel("y-coordiantes", fontsize =20, color="blue")
plot.xlabel("x-coordinates", fontsize =20, color="yellow")
plot.show()
