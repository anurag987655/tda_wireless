import numpy as np 
import matplotlib.pyplot as plt 
from scipy import signal 

fs = 1000 
t = np.linspace(0,1,fs)

# create a signal (sine)

f = 5

x = np.sin(2 * np.pi * f * t)

X = np.fft.fft(x)
freq = np.fft.fftfreq(len(x),1/fs)

# looking at positive frequencies only 

half = len(x) // 2

fig, ax = plt.subplots(2,1, figsize=(12,4))

#left for time domain
ax[0].plot(t,x)
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("Amplitude")
ax[0].set_title("Time Domain")
ax[0].grid()

# right for frequency domain 

ax[1].plot(freq[:half],np.abs(X[:half]))
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_ylabel("Magnitude")
ax[1].set_title("Frequency Domain")
ax[1].grid()

plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.savefig("plots/sinewavefft.png")
plt.close()


## Experiment 2 : mixed signal fft (5 Hz + 20 Hz)

f1 = 5 
f2 = 20 

x_mixed = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

X_mixed = np.fft.fft(x_mixed)

fig , ax = plt.subplots(2,1, figsize=(12,4))

#Time domain for mixed signal 

ax[0].plot(t,x_mixed)
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("Amplitude")
ax[0].set_title("Time domain - Mixed signal (5 hz + 20  hz )")
ax[0].grid()

# frequency domain for mixed signal 

ax[1].plot(freq[:half], np.abs(X_mixed[:half]))
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_ylabel("Magnitude")
ax[1].set_title("Frequency Domain - Mixed signal")
ax[1].grid()

plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.savefig("plots/mixedsignalfft.png")
plt.close()

## Experiment 3 : mixed with noise 

x_noise = np. sin (2 * np.pi * f1 * t) + 0.5 *  np.random.normal (size = t.shape)

X_noise = np.fft.fft(x_noise)
fig , ax = plt.subplots(2,1, figsize=(12,4))

# Time domain view of noisy  signal 

ax[0].plot(t,x_noise)
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("Amplitude")
ax[0].set_title("Time domain - Noisy signal (5 Hz + noise)")
ax[0].grid()    

# Frequency domain view of noisy signal 

ax[1].plot(freq[:half], np.abs(X_noise[:half]))
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_ylabel("Magnitude")
ax[1].set_title("Frequency domain - Noisy signal")
ax[1].grid()    

plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.savefig("plots/noisysignalfft.png")
plt.close() 

## Challenge of the day : Create this signal: x(t)=sin(2π⋅5t)+0.7sin(2π⋅20t)+0.4n(t) however show the frequency domain in full range 

f1 = 5 
f2 = 20 
noise = 0.4 * np.random.normal(size = t.shape)

x_challenge = np.sin(2*np.pi * f1 * t) + 0.7 * np.sin(2 * np.pi * f2 * t) + noise

X_challenge = np.fft.fft(x_challenge)

fig, ax = plt.subplots(2,1, figsize=(12,4))

# Time domain view of challenge signal 

ax[0].plot(t,x_challenge)
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("Amplitude")
ax[0].set_title("Time domain - Challenge signal")   
ax[0].grid()

# Frequency domain view of challenge signal

ax[1].plot(freq, np.abs(X_challenge))
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_ylabel("Magnitude")       
ax[1].set_title("Frequency domain - Challenge signal")
ax[1].grid()    

plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.savefig("plots/challengesignalfft.png")
plt.close() 


# Experminent 04 : square wave 

square = signal.square(2 * np.pi * f1 * t)

X_square = np.fft.fft(square)

fig, ax = plt.subplots(2,1, figsize=(12,4))

# Time domain view of square wave 

ax[0].plot(t,square)
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("Amplitude")       
ax[0].set_title("Time domain - Square wave")
ax[0].grid()

# Frequency domain view of square wave 

ax[1].plot(freq[:half], np.abs(X_square[:half]))
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_ylabel("Magnitude")
ax[1].set_title("Frequency domain - Square wave")
ax[1].grid()    

plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.savefig("plots/squarewavefft.png")
plt.close()