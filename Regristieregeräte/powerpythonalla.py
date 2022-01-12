from typing import Counter
import numpy as np
from math import modf

zeit = np.loadtxt("daten.txt", skiprows=1, usecols=(0,),dtype="str")
feuchte =np.loadtxt("daten.txt", skiprows=1, usecols=(1,))
temp=np.loadtxt("daten.txt", skiprows=1, usecols=2,)
druck=np.loadtxt("daten.txt", skiprows=1, usecols=3,)
k=np.array([])
n=np.array([])
counter=0
for t in zeit:
    k= counter 
    n=np.append(n,k)
    counter+=1

sub=np.array([])
subf=np.array([])
fs=np.array([])
print(n)

for t in n:
    if  (t/60) !=1:
        sub=np.append(sub,t)
        subf=np.append(subf,feuchte[t])
    else:
        fs=np.append(fs, np.mean(subf))
        sub=np.array([])
        subf=np.array([])

print(fs)