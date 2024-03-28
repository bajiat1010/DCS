import numpy as np
import matplotlib.pyplot as plt
N = 10
n = np.random.randint(2, size=N)
print(n)
nn = np.where(n == 1, 1, -1) #Converts the binary values to polar values.
t = np.arange(0, N + 0.01, 0.01) #Creates a time array t from 0 to N with a step size of 0.01
y = np.zeros(len(t)) #Initializes an array y filled with zeros with the same length as t.
for i in range(N):
    y[i * 100:(i + 1) * 100] = nn[i]
    
plt.plot(t, y, linewidth=2)
plt.grid(True)
plt.axis([0, N, -1.5, 1.5])
plt.title("Polar Non Return to Zero")
plt.show()