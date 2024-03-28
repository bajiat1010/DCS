import numpy as np
import matplotlib.pyplot as plt
N = 10
n = np.random.randint(2, size=N)
print(n)
t = np.arange(0, N + 0.01, 0.01)
y = np.zeros(len(t))
for i in range(N):
    for j in range(len(t)):
        if t[j] >= i and t[j] <= i + 0.5:
            y[j] = n[i]
        elif t[j] > i + 0.5:
            break
plt.plot(t, y, linewidth=2)
plt.grid(True)
plt.axis([0, N, -1.5, 1.5])
plt.title("Unipolar Return to Zero")
plt.show()



