import math
import random
def zrob(n):
        sum=0.0
        for i in range(n):
                x=random.uniform(-1,1)
                y=random.uniform(-1,1)
                z=random.uniform(-1,1)
                r=math.sqrt(x**2+y**2+z**2)
                if(r<1.0):
                        sum+=1
        print("objetosc kuli= ",2**3*sum/n, 4.0/3.0*math.pi)
n=100
zrob(n)
n=10**4
zrob(n)
n=10**6
zrob(n)