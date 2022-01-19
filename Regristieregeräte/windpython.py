import numpy as np


richtung=np.loadtxt("spaß.txt", skiprows=1)
ris=np.array([45,90,135,180,225,270,315,360])
alla=np.array([])


for j in ris:
    print(ris[np.where(ris== j)[0]-1])
    alla=np.append(alla, sum((x<=j and x>ris[np.where(ris== j)[0]-1] )for x in richtung))
print(alla)

