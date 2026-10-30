import matplotlib.pyplot as plot
import numpy as np

# serial
x = np.loadtxt("output.txt")
y = np.loadtxt("paraout.txt")
vtimes = [0.098236,0.042456,0.042476,0.036447,0.043273,0.031053,0.038283,0.021983,0.025149,0.031763,0.035865,0.074570]
stimes = [0.000106,
0.000109,
0.000263,
0.000577,
0.001733,
0.005386,
0.011769,
0.025462,
0.062879,
0.129420,
0.259714,
0.640793]
j = 1
N = [1E3, 2E3, 5E3, 1E4, 2E4, 5E4, 1E5, 2E5, 5E5, 1E6, 2E6, 5E6]
times = []
values = []
ptimes =[]
pvalues = []

for i in x:
    if(j % 2 == 0):
        times.append(i)
    else:
        values.append(i)
    j += 1
j = 1

for i in y:
    if(j % 2 == 0):
        ptimes.append(i)
    else:
        pvalues.append(i)
    j += 1
j = 0
speedup = []
for i in stimes:
    speedup.append(i / vtimes[j])
    j +=1
print(speedup)

plot.ylabel("omp wtime elapsed")
plot.xlabel("size of N")
plot.scatter(N, stimes)
plot.scatter(N, ptimes)
plot.show()


plot.ylabel("parallel speedup")
plot.xlabel("size of N")
plot.scatter(N, speedup)
plot.show()


speedups = [1, 1.81, 2.87, 3.46, 5.51, 8.59]
cores = [1, 2, 3, 4, 8, 20]
plot.ylabel("parallel speedup")
plot.xlabel("number of cores")
plot.scatter(cores, speedups)
plot.plot(cores, cores, color = 'orange')
plot.show()