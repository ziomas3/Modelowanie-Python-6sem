import random
import numpy as np
import matplotlib.pyplot as plt
L=10
Lm1=L-1
siec=np.zeros((L,L),int)
p=0.65
#losowa obsada sieci
zielone=[] #lista współrzędnych obsadzonych węzłów

for k in range (0,L):
    for i in range(0,L):
        if random.random()<p:
            siec[k,i]=-1
            zielone.append([k,i])
            #licz=licz+1
print(len(zielone))
#zamiana listy na tablicę
ziel_grf=np.asarray(zielone)
# Wypalanie - rozprzestrzenianie czerwonego koloru
czerwone=[] # początkowo zielone z pierwszej kolumny
czarne=[]   # czerwone zamieniają się w czarne

for i in range(0,L):
    if siec[0,i]==-1:
        czerwone.append([0,i]) #dodajemy do czerw
        zielone.remove([0,i])  #usuwamy z zielonych
        siec[0,i]=1            #zmiana statusu wezła

#czarne.append(czerwone[0]) 

def krok_propag(sc,ziel,czerw,czar):
    tymcz=[]
    for wz in czerw:
        czar.append([wz[0],wz[1]]) 
        #sprawdzenie czy sąsiedzi są zieloni
        #musimy uważać aby nie przekroczyć zakresu sieci
        if wz[0]>0 and sc[wz[0]-1,wz[1]]==-1: #(-1,0)
            tymcz.append([wz[0]-1,wz[1]])
            ziel.remove([wz[0]-1,wz[1]])
            sc[wz[0]-1,wz[1]]=1
        if wz[0]<Lm1 and sc[wz[0]+1,wz[1]]==-1: #(1,0)
            tymcz.append([wz[0]+1,wz[1]])
            ziel.remove([wz[0]+1,wz[1]])
            sc[wz[0]+1,wz[1]]=1
        if wz[1]>0 and sc[wz[0],wz[1]-1]==-1: #(0,-1)
            tymcz.append([wz[0],wz[1]-1])
            ziel.remove([wz[0],wz[1]-1])
            sc[wz[0],wz[1]-1]=1
        if wz[1]<Lm1 and sc[wz[0],wz[1]+1]==-1: #(0,1)
            tymcz.append([wz[0],wz[1]+1])
            ziel.remove([wz[0],wz[1]+1])
            sc[wz[0],wz[1]+1]=1 
    return tymcz
        
def obraz_wyp(ziel,czerw,czar,krok) :
    z_grf=np.asarray(ziel)
    e_grf=np.asarray(czerw)
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(0,L,1))
    ax.set_yticks(np.arange(0,L,1))
    tyt="krok="+str(krok)
    ax.set_title(tyt)
    ax.grid()
    gz=ax.scatter(z_grf[:,0],z_grf[:,1],s=60,c='g')
    ge=ax.scatter(e_grf[:,0],e_grf[:,1],s=60,c='r')
    if len(czar)>1:
        a_grf=np.asarray(czar)
        ga=ax.scatter(a_grf[:,0],a_grf[:,1],s=30,c='k')
    
    plt.show()    
     #ewolucja rozprzestrzeniania koloru czerwonego
t=0
while len(czerwone)>0:
    obraz_wyp(zielone,czerwone,czarne,t) 
    czerwone=krok_propag(siec,zielone,czerwone,czarne) 
    t=t+1