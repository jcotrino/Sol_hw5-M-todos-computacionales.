import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("Canal_ionico.txt")
data1 = np.loadtxt("Canal_ionico1.txt")

x = data[:,0]
y = data[:,1]

x1 = data1[:,0]
y1 = data1[:,1]

plt.figure()
plt.scatter(x, y)


plt.figure()
plt.scatter(x1, y1)
plt.show()

n_iterations = 100

for i in range(n_iterations):
	xmin = np.amax()	
	x = 
	dx =  
