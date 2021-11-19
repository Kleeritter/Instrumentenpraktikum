import numpy as np
import math 

temp= np.arange(253.15, 313.15 ,1)
ras = 8.314462618
kappa =1.402
menge =0.02896
schall= np.array([])
for i in np.arange(253.15, 313.15 ,1):
    sc= math.sqrt(kappa*((ras*i)/menge))
    schall=np.append(schall, sc)

v = np.arange(0.1, 15.0 ,0.1)
fehlerv= 0.05
fehlerd=
fehlerc=
fehlert= np.array([])