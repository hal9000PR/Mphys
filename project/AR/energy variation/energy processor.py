import matplotlib.pyplot as plot
import numpy as np
import math as mt
from scipy.optimize import curve_fit
from os import listdir


files = listdir("C:/Users/Charl/Desktop/masterclass/python/AR/energy variation/energy_data")

show_plot = True

def gaussian (x, sigma, A, mean):
    exponent = (-(x - mean) ** 2) / (2 * (sigma **2))
    return A * (2.71 ** exponent)

def linear (x, grad, offset):
    return grad * x + offset

results = np.zeros([2, len(files)])
i = 0

x_range = np.linspace(0, 50, 1000)

for file in files:

    x, y = np.loadtxt(f'C:/Users/Charl/Desktop/masterclass/python/AR/energy variation/energy_data/{file}', unpack = True, skiprows=17, delimiter=",")

    standard_deviation = np.std(x)
    y_max = y.max()

    op, pcm = curve_fit(gaussian, x, y, p0=[standard_deviation, y_max, 0])

    if(show_plot):
        plot.xlabel("angle")
        plot.ylabel("integrated flux")

        plot.scatter(x, y)
        plot.plot(x_range, gaussian(x_range, op[0], op[1], op[2]))

        plot.show()
    
    stripped = file.split("W", 1)[0]
    results[0, i] = stripped
    results[1, i] = op[2]
    i +=1

plot.xlabel("power (W)")
plot.ylabel("mean energy (eV)")
plot.scatter(results[0,:], results[1,:])

mean_grad = (max(results[1,:]) - min(results[1,:])) / (max(results[0,:]) - min(results[0,:]))
op, pcm = curve_fit(linear, results[0,:], results[1,:], p0=[mean_grad, y[0]])
x_range = np.linspace(0, 500, 1000)
plot.plot(x_range, linear(x_range, op[0], op[1]))
print("gradient", op[0])


plot.show()