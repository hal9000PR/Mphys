import matplotlib.pyplot as plot
import numpy as np
import math as mt
from scipy.optimize import curve_fit
from os import listdir

show_plot = True

def line(x, y):
    a = []
    for i in range(0, len(x)):
        a.append(y)
    return a

files = listdir("C:/Users/Charl/Desktop/masterclass/python/AR/energy variation/ring")

results = np.zeros([4, len(files)])
i = 0

for file in files:

    x, y = np.loadtxt(f'C:/Users/Charl/Desktop/masterclass/python/AR/energy variation/ring/{file}', unpack = True, skiprows=17, delimiter=",")

    y_centre = y[0]
    max_etching_radius = 0
    y_max = y_centre * 1.05
    y_min = y_centre * 0.95
    for j in range(0, len(y)):
        if((y[j] < y_max) and (y[j] > y_min)):
            max_etching_radius = x[j]
            continue
        break

    if(show_plot):
        plot.title("6mm ring")
        plot.xlabel("radius (cm)")
        plot.ylabel("integrated flux")

        plot.scatter(x, y)
        plot.ylim(0, 2e16)
        x_range = np.linspace(0, max(x), 100)
        plot.plot(x_range, line(x_range, y_max))
        plot.plot(x_range, line(x_range, y_min))
        plot.show()
    


    stripped = file.split("mm", 1)[0]
    print(stripped, max_etching_radius)# / float(stripped))
    results[0, i] = stripped
    results[1, i] = max_etching_radius# / float(stripped)
    i += 1

plot.xlabel("ring radius (mm)")
plot.ylabel("Max Etching radius")

plot.scatter(results[0,:], results[1,:])
plot.show()
