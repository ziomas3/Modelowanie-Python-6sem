import numpy as np
import matplotlib.pyplot as plt

def spacer(b1, b2, x0):
    t = 0
    x = x0
    while(x != b1 and x != b2):
        x += np.random.choice([-1, 1])
        t += 1
    return t

a = 5
b1 = 0 
b2 = 2*a    
tsr = 0.
n = 10000

for i in range(n):
    tsr += spacer(b1, b2, a)

print("srednia dla " + str(a) + ": " + str(tsr/n))

poczatki = np.arange(b1 + 1, b2, step=1) 
tsrednie = np.zeros((len(poczatki),), dtype=float)

for i in range(len(poczatki)):
    for j in range(n):
        tsrednie[i] +=spacer(b1, b2, poczatki[i])

tsrednie = tsrednie/n
for i in poczatki:
    print(str(i)+" "+str(tsrednie[i-1]))
plt.plot(poczatki, tsrednie)
plt.xlabel("Położenia startu")
plt.ylabel("krok")
plt.show()