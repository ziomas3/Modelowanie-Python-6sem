import math
import random
def zrob(n):
        sum=0.0
        for i in range(n):
                x1=random.uniform(-1,1)
                x2=random.uniform(-1,1)
                x3=random.uniform(-1,1)
                x4=random.uniform(-1,1)
                x5=random.uniform(-1,1)
                x6=random.uniform(-1,1)
                x7=random.uniform(-1,1)
                x8=random.uniform(-1,1)
                x9=random.uniform(-1,1)
                x10=random.uniform(-1,1)
                x11=random.uniform(-1,1)
                x12=random.uniform(-1,1)
                x13=random.uniform(-1,1)
                x14=random.uniform(-1,1)
                x15=random.uniform(-1,1)
                r=math.sqrt(x1**2+x2**2+x3**2+x4**2+x5**2+x6**2+x7**2+x8**2+x9**2+x10**2+x11**2+x12**2+x13**2+x14**2+x15**2)
                if(r<1.0):
                        sum+=1
        print("objetosc kuli= ",2**15*sum/n, 256*math.pi**7/2027025)
n=100
zrob(n)
n=10**4
zrob(n)
n=10**6
zrob(n)
n=10**8
zrob(n)