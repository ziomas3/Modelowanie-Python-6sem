import random
import math

def f1(x):
    return 1/math.sqrt(2*math.pi)*math.exp((-x*x)/2)
a=-2
b=2
d=b-a
n=100000
calka=0
for _ in range(n):
    x=random.uniform(a, b)
    calka=calka+d*f1(x)
calka=calka/n
print('I_MC=',calka)
