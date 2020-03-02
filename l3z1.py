import numpy as np
import matplotlib.pyplot as plt
import random 

def Randomwalk():
        v=np.array([[1, 0],[0, 1],[-1, 0],[0,-1]])   #sasiedzi
        r0=np.array([0,0])  
        ds=101 #kroki
        wsp_x=np.zeros(ds)
        wsp_y=np.zeros(ds) 

        wsp_x[0]=r0[0]
        wsp_y[0]=r0[1]
        for k in range(1,ds):
                los = random.randint(0,3)
                wsp_x[k]= wsp_x[k-1]+v[los][0] 
                wsp_y[k]= wsp_y[k-1]+v[los][1]
        return wsp_x, wsp_y

x, y = Randomwalk()
plt.plot(x, y)



N = 10000
powrot = 0 

for i in range(N): 
        bx, by = Randomwalk()
        if(bx[-1] == 0 and by[-1] == 0):
                powrot += 1

print(powrot)
plt.show()