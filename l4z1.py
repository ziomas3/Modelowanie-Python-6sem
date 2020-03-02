import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm  
def podziel(list, n):
    # dzieli liste na podlisty po n elementow
    for i in range(0, len(list), n):
        
        yield list[i:i+n] # zwraca podliste elementow od i do i+n (yield zwraca to kilka razy, az i osiagnie len(list), wiec otrzymamy kilka podlist listy n)
        # przyklad: dla [1,2,3,4,5,6,7,8,9]
        # yield dla n = 3 zwroci: [1,2,3] , [4,5,6] , [7,8,9]
def rys_zlep():
#4 wektory do najbliższych sąsiadów
    v=np.array([[1, 0],[0, 1],[-1, 0],[0,-1]])
    Lp=50 
    L=2*Lp
    siec=np.zeros((L,L),int)

    zlep_x=[]
    zlep_y=[]
#zarodek
    r=np.array([0,0])
    lista=[[Lp,Lp]]
    
    while 1:
        r=random.choice(lista)
        if (r[0]==0)or(r[0]==L-1):
            break
        if (r[1]==0)or(r[1]==L-1):
            break    
        siec[r[0],r[1]]=1
        zlep_x.append(r[0])
        zlep_y.append(r[1])
        for i in range(4):
            rs=r+v[i]
            if(siec[rs[0],rs[1]]==0):
                lista.append([rs[0],rs[1]])
        lista.remove([r[0],r[1]])
        
       
    
    lk=10 # liczba kolorow
    zlep_x=list(podziel(zlep_x, int(len(zlep_x)/lk))) # uruchamiam dzielenie listy zawierajacej x
    zlep_y=list(podziel(zlep_y, int(len(zlep_y)/lk))) # uruchamiam dzielenie listy zawierajacej y
    for i in range(0, lk): # petla wyrysowujaca poszczegolne etapy tworzenia zlepka
        plt.scatter(zlep_x[i], zlep_y[i], marker='s')

    plt.show()
rys_zlep()