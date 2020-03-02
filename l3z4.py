import numpy as np 
import random
import matplotlib.pyplot as plt 

v=np.array([[1, 0],[0, 1],[-1, 0],[0,-1]])

def kroplaDeszczu(ds):
    for h in range(100,1000,100):
        r0=np.array([0,h]) 
        wsp_x=[]
        wsp_y=[] 

        wsp_x.append(r0[0])
        wsp_y.append(r0[1])
        for k in range(1,ds):
            r0=r0+v[np.random.choice(4, p=[0.15,0.1,0.15,0.6])] 
            wsp_x.append(r0[0])
            wsp_y.append(r0[1])
        return wsp_x, wsp_y

wsp_x, wsp_y = kroplaDeszczu(101)
plt.plot(wsp_x, wsp_y)
plt.show()

def czas_pas(x0,xa):
    x=x0 
    i=0
    while (-xa<x and x<xa):
        x=x+random.choice([-1, 1])
        i=i+1
    return i
xa=5  
x0=0
ns=20
t1p=[]
for _ in range (ns):
    t1p.append(czas_pas(x0,xa))
print(t1p)

xa=5  
x0=0
tav=0
ns=100
for _ in range (ns):
    tav=tav+czas_pas(x0,xa)
tav=tav/ns
print (tav)
