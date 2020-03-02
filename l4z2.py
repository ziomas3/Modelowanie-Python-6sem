import random
import numpy as np
import matplotlib.pyplot as plt

v=np.array([[1, 0],[0, 1],[-1, 0],[0,-1]]) # 4 wektory do najbliższych sąsiadów

Lp=300  # współrzędna środka sieci 
L=2*Lp  # rozmiar liniowy sieci
siec=np.zeros((L,L),int)  # siec o  L*L pocżatkowo wyzerowana
#  Składowe sieci mogą przyjmować wartości  0,1 i 2
# Wartości te reprezentują
#   0 węzły dyfuzyjne
#   1 węzły zlepka
#   2 węzły pochlaniające

def init():
    siec[Lp,Lp]=1  #zarodek
    #wezly pochlaniajace
    for i in range(L):
        siec[i,0]=2
        siec[i,L-1]=2
        siec[0,i]=2
        siec[L-1,i]=2
    return np.array([Lp,Lp],int)


def start_cz(R):
    kat=2*np.pi*random.random()
    # losowe położenie początkowe na okręgu o promieniu R
    return np.array([Lp+np.rint(R*np.cos(kat)),Lp+np.rint(R*np.sin(kat))],int)
       

def wzrost(Rm,mmax,xy_z):
    R=1
    licz=1
    rb=init()
    xy_z.append(rb)
    while licz<mmax:     
        if R<Rm:
            R=R+1   
        rb=start_cz(R)
        while siec[rb[0],rb[1]]==0:
            xr=rb+v[random.randint(0,3)] #losowy  krok
            rb=xr
            if siec[xr[0]+1,xr[1]]==1 or siec[xr[0]-1,xr[1]]==1 or siec[xr[0],xr[1]+1]==1 or siec[xr[0],xr[1]-1]==1:
                
                siec[rb[0],rb[1]]=1
                xy_z.append(rb)
                licz+=1
            if siec[xr[0]+1,xr[1]]==2 or siec[xr[0]-1,xr[1]]==2 or siec[xr[0],xr[1]+1]==2 or siec[xr[0],xr[1]-1]==2:
                break
    rys_zlep(mmax,xy_z)         
    

def rys_zlep(kn,xy):
    x, y = zip(*xy)
    plt.scatter(x, y, marker='o')

    plt.show()

xy_agr=[]

mmax=1000
R=150
wzrost(R,mmax,xy_agr)
