import matplotlib.pyplot as plot
import numpy as np
import math as mt
from scipy.optimize import curve_fit
from os import listdir

show_plot = False

directory = "C:/Users/Charl/Desktop/masterclass/python/AR/energy variation/etch_data"

#C:/Users/Charl/Desktop/masterclass/python/AR2+/power_etch
# C:/Users/Charl/Desktop/masterclass/python/AR/energy variation/etch_data

files = listdir(directory)

results = np.zeros([3, len(files)])
i = 0

for file in files:

    x, y = np.loadtxt(f'{directory}/{file}', unpack = True, skiprows=17, delimiter=",")

    y_centre = y[0]
    max_etching_radius = 0
    min_etching_flux = 1e31

    for j in range(0, len(y)):
        if(y[j] < min_etching_flux):
            min_etching_flux = y[j]
        
        if((y[j] < (y_centre * 1.1)) and (y[j] > (y_centre * 0.9))):
            max_etching_radius = x[j]
            continue
        break

    if(show_plot):
        plot.xlabel("angle")
        plot.ylabel("integrated flux")

        plot.scatter(x, y)
        plot.show()
    
    stripped = file.split("W", 1)[0]
    print(stripped, max_etching_radius)
    results[0, i] = stripped
    results[1, i] = max_etching_radius
    results[2, i] = min_etching_flux
    i += 1

plot.xlabel("Power (W)")
plot.ylabel("Max Etching Radius (cm)")

plot.scatter(results[0,:], results[1,:])
plot.show()


plot.xlabel("Power (W)")
plot.ylabel("Min Etching Flux (cm)")
plot.scatter(results[0, :], results[2, :])
plot.show()