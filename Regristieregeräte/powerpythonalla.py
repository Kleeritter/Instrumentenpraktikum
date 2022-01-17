import numpy as np
from math import modf

zeit = np.loadtxt("daten2.txt", skiprows=1, usecols=(4,15,26,),dtype="str")
feuchte =np.loadtxt("daten2.txt", skiprows=1, usecols=(1,))
temp=np.loadtxt("daten2.txt", skiprows=1, usecols=2,)
druck=np.loadtxt("daten2.txt", skiprows=1, usecols=3,)
zeiter=np.array([])
n=np.arange(0, len(zeit), 1)
for i in zeit:
    zeiter=np.append(zeiter,int(i[:2]))
print(zeiter)
nfeuchte=np.array_split(feuchte,60)
feuchtesums=np.array([])
tempsum=np.array([])
drucksum=np.array([])
zeitsum=np.array([])
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
koks=list(chunks(feuchte,60))
timeso=list(chunks(zeiter,60))
tempo=list(chunks(temp,60))
drucko=list(chunks(druck,60))
print(timeso[len(timeso)-6])
print(koks[len(koks)-1])
for x in range(0,len(koks)):
    feuchtesums=np.append(feuchtesums, np.mean(koks[x]))
    tempsum=np.append(tempsum, np.mean(tempo[x]))
    drucksum=np.append(drucksum, np.mean(drucko[x]))
    zeitsum=np.append(zeitsum, np.mean(timeso[x]))
np.savetxt("feuchten.txt",feuchtesums,fmt='%.2f')
np.savetxt("temps.txt",tempsum,fmt='%.2f')
np.savetxt("drücke.txt",drucksum,fmt='%.2f')
np.savetxt("zeiten.txt",zeitsum ,fmt='%d')