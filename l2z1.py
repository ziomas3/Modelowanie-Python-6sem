import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
import random
def wykres_spaceru(nk):
    a = np.zeros(nk)
    x=0 
    a[0]=x
    for i in range(1,nk):
        x=x+random.choice([-1, 1])
        a[i]=x
    t = np.arange(nk)
    plt.rcParams["figure.figsize"] = (10,5)
    plt.plot(t,a)
    plt.ylabel('x')
    plt.xlabel('numer kroku')
    

wykres_spaceru(100)
wykres_spaceru(100)


def koniec_spaceru(nk,ns):  
    ks=np.zeros(ns)
    for i in range(ns):
        x=0
        for k in range(1,nk):
            x=x+random.choice([-1, 1])
        ks[i]=x
    return ks
   

xs = koniec_spaceru(101,10000)
plt.show()
nh, xh,pa = plt.hist(xs,85,histtype='stepfilled')
plt.xlabel('x_k')
plt.ylabel('czestosc')
plt.title('Histogram błądzenia losowego')
plt.show()