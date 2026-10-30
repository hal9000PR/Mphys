import matplotlib.pyplot as plot
import numpy as np
import math as mt
from scipy.optimize import curve_fit
from os import listdir

files = listdir("C:/Users/Charl/Desktop/masterclass/python/AR/energy variation/angle_data")

show_plot = False

def linear (x, grad, offset):
    return grad * x + offset

def mirror_decay (x, decay_rate, amplitude, offset):
    exponent = -abs(decay_rate * x + offset)
    return amplitude * (mt.e ** exponent)

results = np.zeros([2, len(files)])
i = 0

for file in files:

    x, y = np.loadtxt(f'C:/Users/Charl/Desktop/masterclass/python/AR/energy variation/angle_data/{file}', unpack = True, skiprows=17, delimiter=",")

    standard_deviation = np.std(x)
    y_max = y.max()
    x_range = np.linspace(-30, 30, 1000)

    op, pcm = curve_fit(mirror_decay, x, y, p0=[standard_deviation, y_max, 0])

    if(show_plot):
        plot.xlabel("angle")
        plot.ylabel("integrated flux")

        plot.scatter(x, y)
        plot.plot(x_range, mirror_decay(x_range, op[0], op[1], op[2]))

        plot.show()
    
    stripped = file.split("W", 1)[0]
    results[0, i] = stripped
    results[1, i] = abs(op[0])
    i +=1

    print(op[0])

plot.xlabel("power (W)")
plot.ylabel("decay coefficient")

plot.scatter(results[0,:], results[1,:])

mean_grad = (max(results[1,:]) - min(results[1,:])) / (max(results[0,:]) - min(results[0,:]))
op, pcm = curve_fit(linear, results[0,:], results[1,:], p0=[mean_grad, y[0]])
x_range = np.linspace(0, 500, 1000)
plot.plot(x_range, linear(x_range, op[0], op[1]))
print("gradient", op[0])

plot.show()