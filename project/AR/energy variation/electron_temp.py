import matplotlib.pyplot as plot
import numpy as np
import math as mt
from scipy.optimize import curve_fit
from os import listdir


files = listdir("C:/Users/Charl/Desktop/masterclass/python/AR/energy variation/electron_data")

results = np.zeros([2, len(files)])
i = 0

for file in files:
    
    x, y, z = np.loadtxt(f'C:/Users/Charl/Desktop/masterclass/python/AR/energy variation/electron_data/{file}', unpack = True, skiprows=17, delimiter=",")
    results[0, i] = file.split("W", 1)[0]
    results[1, i] = max(z)
    i += 1

plot.ylabel("electron Temperature (ev)")
plot.xlabel("power (W)")

plot.scatter(results[0,:], results[1,:])
plot.show()