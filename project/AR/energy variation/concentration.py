import matplotlib.pyplot as plot
import numpy as np
import math as mt
from scipy.optimize import curve_fit
from os import listdir
matrix = np.zeros([59,59])

files = listdir("C:/Users/Charl/Desktop/masterclass/python/AR/energy variation/concentration_data")

results = np.zeros([2, len(files)])

j = 0
for file in files:
    i = -9 # skip first 8 rows
    f = open(f'C:/Users/Charl/Desktop/masterclass/python/AR/energy variation/concentration_data/{file}')
    for line in f:
        i += 1
        if(i < 0):
            continue

        line_ = line[:-3]
        x = line_.split(",")
        matrix[i, :] = x

    results[1,j] = matrix.max()
    results[0,j] = file.split("W", 1)[0]
    j +=1

plot.xlabel("power (W)")
plot.ylabel("Maximum Plasma Concentration (cm^-3)")

plot.scatter(results[0,:], results[1,:])
plot.show()