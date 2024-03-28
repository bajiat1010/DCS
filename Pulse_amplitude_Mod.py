import numpy as np
import matplotlib.pyplot as plt
# Parameters
fc, fm, fs, t, duty = 20, 2, 1000, 1, 20
# Time axis
n = np.arange(0, t, 1/fs)
# Square wave generation
s = np.where(np.floor(2 * fc * n) % 2 == 0, 1, 0)
# Sine wave generation
m = np.sin(2 * np.pi * fm * n)
# PAM waveform generation
period_samp = len(n) / fc
on_samp = int(np.ceil(period_samp * duty / 100))
ind = np.arange(0, len(n), int(period_samp))
pam = np.zeros(len(n))
for i in ind:
    pam[i:i+on_samp] = m[i]
# Plotting
plt.figure(figsize=(8, 6))
plt.subplot(3, 1, 1)
plt.plot(n, s)
plt.title('Square Wave')
plt.ylim(-0.2, 1.2)

plt.subplot(3, 1, 2)
plt.plot(n, m)
plt.title('Sine Wave')
plt.ylim(-1.2, 1.2)

plt.subplot(3, 1, 3)
plt.plot(n, pam)
plt.title('PAM Waveform')
plt.ylim(-1.2, 1.2)

plt.tight_layout()
plt.show()