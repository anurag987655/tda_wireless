import numpy as np 
import matplotlib.pyplot as plt
from scipy import signal 

## pure signal setup

t = np.linspace(0,1,1000) 

## pure sine wave generation : 

A = 1
f = 5 
phi = 0 

x1 = A * np.sin(2*np.pi * f * t + phi)

plt.figure()
plt.plot(t,x1)
plt.title("pure sine wave generation")
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig("plots/sine_wave.png")
plt.close()


## higher frequency sine wave 

f = 20 
x2 = A * np.sin(2*np.pi * f * t + phi)

plt.figure()
plt.plot(t, x2)
plt.title("higher frequency sine wave")
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig("plots/higher_freq_sine_wave.png")
plt.close() 

## higher amplitude sine wave 

A = 3
f = 5
x3= A * np.sin(2* np.pi * f * t + phi)

plt.figure()
plt.plot(t,x3)
plt.title("higher amplitude sine wave")
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig("plots/higher_amp_sine_wave.png")
plt.close()

## Noisy signal 

A = 1
f = 5
noise = 0.5 * np.random.normal(size=t.shape)

x = A *np.sin(2*np.pi * f * t + phi)
x4 = x + noise 

plt.figure()
plt.plot(t,x4)
plt.title("noisy signal")
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig("plots/noisy_signal.png")
plt.close()

## phase shift

phi  = np.pi/4
x5 = A * np.sin(2*np.pi * f * t + phi)

plt.figure()
plt.plot(t,x5)
plt.title("phase shift")
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig("plots/phase_shift.png")
plt.close()

square_wave = signal.square(2* np.pi * f * t)
plt.figure()
plt.plot(t, square_wave)
plt.title("square wave")
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig("plots/square_wave.png")
plt.close()