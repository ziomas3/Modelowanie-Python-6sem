import numpy as np 
import random
import matplotlib.pyplot as plt 

v=np.array([[1, 0],[0, 1],[-1, 0],[0,-1]])   #wektory do najbliższych sąsiadów

#siec o rozmiarach LxL
L=10
Lm1=L-1
siec=np.zeros((L,L),int)

for i in range(1,L):
    siec[0,i]=1 # węzły odbijające w kierunku x
    siec[i,0]=2 # węzły odbijające w kierunku y
    siec[Lm1,i]=3 # węzły pochłaniające
    siec[i,Lm1]=3 # węzły pochłaniające    
def xy_adsorb():
    r=np.array([1,1])  # początek spaceru
    i=0
    while siec[r[0],r[1]]<3:
        if siec[r[0],r[1]]<1:
            r=r+v[random.randint(0,3)] #losowy kierunek kroku
        elif siec[r[0],r[1]]<2:
            r[0]=r[0]+1
        else:
            r[1]=r[1]+1
        i+=1
    return i,r

        
def rys_ads_traj():
    xtr=[]
    ytr=[]
    r=np.array([1,1])  # początek spaceru
    xtr.append(r[0])
    ytr.append(r[1])
    i=0
    while siec[r[0],r[1]]<3:
        if siec[r[0],r[1]]<1:
            r=r+v[random.randint(0,3)] #losowy kierunek kroku
        elif siec[r[0],r[1]]<2:
            r[0]=r[0]+1
        else:
            r[1]=r[1]+1
        xtr.append(r[0])
        ytr.append(r[1])
        i+=1
    return xtr, ytr     
        
    
    
xtr, ytr=rys_ads_traj()
fig, ax = plt.subplots()
ax.set_xticks(np.arange(0,L,1))
ax.set_yticks(np.arange(0,L,1))
ax.set_xlim(0,Lm1)
ax.set_ylim(0,Lm1)

tyt="trasa do adsorpcji"
ax.set_title(tyt)
ax.grid()
ax.plot(xtr, ytr)
ax.axhline(Lm1,0,Lm1,linewidth=5,color='r')
ax.axvline(Lm1,0,Lm1,linewidth=5,color='r')
plt.show()