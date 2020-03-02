import numpy as np
import matplotlib.pyplot as plt
import random 
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d

def bladzenieLosowe():
        v=np.array([[1, 0, 0],[0, 1, 0],[0, 0, 1],[-1, 0, 0],[0, -1, 0],[0, 0, -1]])
        r0=np.array([0,0,0])
        ds=1000  
        wsp_x=np.zeros(ds)
        wsp_y=np.zeros(ds) 
        wsp_z=np.zeros(ds)

        wsp_x[0]=r0[0]
        wsp_y[0]=r0[1]
        wsp_z[0]=r0[2]
        for k in range(1,ds):
                los = random.randint(0,5)
                wsp_x[k] = wsp_x[k-1]+v[los][0] 
                wsp_y[k] = wsp_y[k-1]+v[los][1]
                wsp_z[k] = wsp_z[k-1]+v[los][2]
        return wsp_x, wsp_y, wsp_z

x, y, z = bladzenieLosowe()
plt.axes(projection='3d').plot3D(x, y, z)
plt.show()

