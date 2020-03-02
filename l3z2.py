import numpy as np
import matplotlib.pyplot as plt 


def bladzenie(wymiar):
    siec = np.zeros((wymiar, wymiar), int)
    v=np.array([[1, 0],[0, 1],[-1, 0],[0,-1]]) 
    retx = [int(np.floor(wymiar/2))] 
    rety = [int(np.floor(wymiar/2))]
    siec[retx[0], rety[0]] = 1
    dlugosc = 0
    kontynuuj = True
    kierunek = 0

    while(kontynuuj):
        mozliwosci = [] 
        for i in range(4):
            if(retx[-1] + v[i][0] < wymiar and retx[-1] + v[i][0] >= 0 and rety[-1] + v[i][1] < wymiar and rety[-1] + v[i][1] >= 0 and siec[retx[-1] + v[i][0]][rety[-1] + v[i][1]] < 1): #
                
                mozliwosci.append(i)
        
        if not mozliwosci:
            kontynuuj = False
        else:
            dlugosc += 1
            kierunek = np.random.choice(mozliwosci) 
            retx.append(retx[-1] + v[kierunek][0])
            rety.append(rety[-1] + v[kierunek][1])
            siec[retx[-1]][rety[-1]] = 1
    return retx, rety, dlugosc
mx = 0
my =  0
mlen = 0

for i in range(10000):
    x, y, len = bladzenie(1000)
    if(len > mlen):
        mx = x
        my = y
        mlen = len

print(mlen)
plt.plot(mx, my)
plt.show()