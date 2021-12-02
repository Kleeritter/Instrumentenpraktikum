import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

date_time = ["2021-11-24", "2021-11-25", "2021-11-26","2021-11-27","2021-11-28","2021-11-29","2021-11-30","2021-12-01"]
date_time = pd.to_datetime(date_time)

miny=  np.loadtxt("min.txt" , usecols=(1,)) 

plt.plot_date(date_time,miny,label="Minimumtemperattur")
#plt.axis([10**-9,10**-4,0.98,1.05])
plt.xlabel("Tag")
plt.ylabel( "Temperatur in °C")

plt.title("Vergleich verschiedener Köhlerkurven")
plt.legend()
plt.savefig("Tempo.png",dpi=1200)