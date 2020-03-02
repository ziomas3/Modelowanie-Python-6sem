import numpy as np
import matplotlib.pyplot as plt
import random 

def Randomwalk():
        v=np.array([[1, 0],[0, 1],[-1, 0],[0,-1]])   #sasiedzi
  
        wsp_x=0
        wsp_y=0 
        b=[0,0,0,0]
        kon=[] #all uderzenia w 1 sciane
        kontynuuj=1
        k=1
        while(kontynuuj):
                los = random.randint(0,3)
                wsp_x= wsp_x+v[los][0] 
                wsp_y= wsp_y+v[los][1]
                if(wsp_x==20):
                        b[0]=b[0]+1
                        kon.append(wsp_y)
                        kontynuuj=0
                if(wsp_y==20):
                        b[1]=b[1]+1
                        kontynuuj=0
                if(wsp_x==-20):
                        b[2]=b[2]+1
                        kontynuuj=0
                if(wsp_y==-20):
                        b[3]=b[3]+1
                        kontynuuj=0
                k=k+1
        return kon, b

kon, b = Randomwalk()
print (kon)

N = 100000
powrot = 0 

d=[0,0,0,0]
koncowe=[]
for i in range(N): 
        kon, b = Randomwalk()
        for i in range(4):
                koncowe.append(kon)
                d[i]+=b[i]

print(d)
alls=np.arange(-19,20)
print(alls)
wyplute=[]
for i in alls:
        wyplute.append(koncowe.count(i))
plt.plot(alls, wyplute)
plt.show()
