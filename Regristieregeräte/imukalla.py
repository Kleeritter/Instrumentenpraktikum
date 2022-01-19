import numpy as np
from math import modf

temp = dict()
druck=dict()
feuchte= dict()
tempsum=np.array([])
drucksum=np.array([])
zeitsum=np.array([])
feuchtesum=np.array([])
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

for i in range(5,104,11):
    temp[i] =np.loadtxt("alarm.txt",  usecols=(i))
    tempo=list(chunks(temp[i],60))
    for x in range(0,len(tempo)):
        tempsum=np.append(tempsum, np.mean(tempo[x]))
np.savetxt("tempsi.txt",tempsum,fmt='%.2f')
for i in range(9,106,11):
    druck[i] =np.loadtxt("alarm.txt",  usecols=(i))
    drucko=list(chunks(druck[i],60))
    for x in range(0,len(drucko)):
        drucksum=np.append(drucksum, np.mean(drucko[x]))
np.savetxt("drucki.txt",drucksum,fmt='%.2f')
print(temp)

for i in range(6,105,11):
    feuchte[i] =np.loadtxt("alarm.txt",  usecols=(i))
    feuchto=list(chunks(feuchte[i],60))
    for x in range(0,len(feuchto)):
        feuchtesum=np.append(feuchtesum, np.mean(feuchto[x]))
np.savetxt("feuchti.txt",feuchtesum,fmt='%.2f')


