import matplotlib.pyplot as plot
import numpy as np
import math as mt
from scipy.optimize import curve_fit
from os import listdir

def decay (x, decay_rate, amplitude, offset):
    exponent = -(decay_rate * x + offset)
    return amplitude * (mt.e ** exponent)

def reciprical (x, decay_rate, offset_x, offset_y):
    return (decay_rate/(x + offset_x)) + offset_y

show_plot = False

files = listdir("C:/Users/Charl/Desktop/masterclass/python/AR/pressure_var/etch_data")

results = np.zeros([3, len(files)])
i = 0

for file in files:

    x, y = np.loadtxt(f'C:/Users/Charl/Desktop/masterclass/python/AR/pressure_var/etch_data/{file}', unpack = True, skiprows=17, delimiter=",")

    y_centre = y[0]
    max_etching_radius = 0
    min_etching_flux = 1e31
    for j in range(0, len(y)):
        if(y[j] < min_etching_flux):
            min_etching_flux = y[j]

        if((y[j] < (y_centre * 1.1)) and (y[j] > (y_centre * 0.9))):
            continue
        max_etching_radius = x[j]
        break

    if(show_plot):
        plot.xlabel("angle")
        plot.ylabel("integrated flux")

        plot.scatter(x, y)
        plot.show()
    
    stripped = file.split("mT", 1)[0]
    print(stripped, max_etching_radius)
    results[0, i] = stripped
    results[1, i] = max_etching_radius
    results[2, i] = min_etching_flux
    i += 1

plot.xlabel("Pressure(mT)")
plot.ylabel("Max Etching Radius (cm)")

x_range = np.linspace(0, 500, 1000)
op, pcm = curve_fit(reciprical, results[0, :], results[1, :], p0=[1, 0, min(results[1, :])])
plot.plot(x_range, reciprical(x_range, op[0], op[1], op[2]))

plot.scatter(results[0,:], results[1,:])
plot.show()


plot.xlabel("Pressure(mT)")
plot.ylabel("Min Etching Flux (cm)")
plot.scatter(results[0, :], results[2, :])
plot.show()