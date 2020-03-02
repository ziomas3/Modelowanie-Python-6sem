import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
import random
def persisted_rw(nk,x0,p):
    a = np.zeros(nk)
    x=x0
    a[0]=x
    krok=random.choice([-1, 1])
    
    for i in range(1,nk):
        if random.random()>p:
            krok=-krok
        x=x+krok
        a[i]=x
    return a
    
n1=100 
t = np.arange(n1)
ns=10000  
x0=0 

p=0.2
r1 = np.zeros(n1) 
for i in range(ns):
    xt=persisted_rw(n1,x0,p)
    for l in range(n1):
        r1[l]=r1[l]+(xt[l]-x0)**2 
for i in range(n1):
    r1[i]=r1[i]/ns      
plt.plot(t,r1,label='p=0.8')


p=0.8
r2 = np.zeros(n1) 
for i in range(ns):
    xt=persisted_rw(n1,x0,p)
    for l in range(n1):
        r2[l]=r2[l]+(xt[l]-x0)**2 
for i in range(n1):
    r2[i]=r2[i]/ns  
plt.plot(t,r2,label='p=0.8')

plt.ylabel('<r^2>')
plt.xlabel('t')
tytul = "skorelowane błądzenia losowe"
plt.title(tytul)
plt.show()
#definicja msd/ ośk