import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

date_time = ["2021-11-24", "2021-11-25", "2021-11-26","2021-11-27","2021-11-28","2021-11-29","2021-11-30","2021-12-01"]
date_time = pd.to_datetime(date_time)

miny=  np.loadtxt("min.txt" , usecols=(0,)) 
maxy=  np.loadtxt("min.txt" , usecols=(1,)) 

minmessy= -10.5


maxmessy= 12.5


plt.plot_date(date_time,miny,label="Min T")
plt.plot_date(date_time,maxy,label="Max T")
#plt.plot_date(date_time,minmessy,label="gemessene Minimumtemperatur")
#plt.plot_date(date_time,maxmessy,label="gemessene Maximumtemperatur")
plt.hlines(minmessy,min(date_time), max(date_time),label="gemessene Min T")
plt.hlines(maxmessy,min(date_time), max(date_time),label="gemessene Max T" ,colors="red")
#plt.axis([10**-9,10**-4,0.98,1.05])
plt.xlabel("Tag")
plt.ylabel( "Temperatur in °C")
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.savefig("Tempo.png",dpi=1200)
plt.show()