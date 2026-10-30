import matplotlib.pyplot as plot
import numpy as np
import math as mt
from scipy.optimize import curve_fit
from os import listdir


files = listdir("C:/Users/Charl/Desktop/masterclass/python/AR/pressure_var/electron temp")

results = np.zeros([2, len(files)])
i = 0

for file in files:
    
    x, y, z = np.loadtxt(f'C:/Users/Charl/Desktop/masterclass/python/AR/pressure_var/electron temp/{file}', unpack = True, skiprows=17, delimiter=",")
    results[0, i] = file.split("mT", 1)[0]
    results[1, i] = max(z)
    i += 1

plot.ylabel("electron Temperature (ev)")
plot.xlabel("pressure (mT)")

plot.scatter(results[0,:], results[1,:])
plot.show()