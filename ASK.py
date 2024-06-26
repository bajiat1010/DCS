import numpy as np
import matplotlib.pyplot as plt
# Binary information at transmitter
x = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1])
bp = 0.000001
print('Binary Information at transmitter:')  
print(x)
# Digital signal representation
bit = np.array([np.ones(100) if bit_value == 1 else np.zeros(100) for bit_value in x]).flatten()
t1 = np.arange(bp / 100, 100 * len(x) * (bp / 100) + bp / 100, bp / 100)

plt.subplot(211)
plt.plot(t1, bit, linewidth=2.5)
plt.grid(True)
plt.axis([0, bp * len(x), -0.5, 1.5])
plt.ylabel("Amplitude (volt)")
plt.xlabel("Time (sec)")
plt.title("Transmitting Information as Digital Signal")
# Binary ASK Modulation
A1, A2 = 10, 5
br = 1 / bp
f = br * 10
t2 = np.arange(bp / 99, bp + bp / 99, bp / 99)
m = np.concatenate([(A1 * np.cos(2 * np.pi * f * t2)) if bit_value == 1 else (A2 * np.cos(2 * np.pi * f * t2)) for bit_value in x])
t3 = np.arange(bp / 99, bp * len(x), bp / 99)

plt.subplot(212)
plt.plot(t3, m)
plt.grid(True)
plt.axis([0, bp * len(x), -10, 10])
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude (volt)")
plt.title("Waveform for Binary ASK Modulation Corresponding Binary Information")
plt.tight_layout()
plt.show()   


