

import numpy as np 
import  matplotlib.pyplot as plt
import os 

os.makedirs("plots", exist_ok=True)

np.random.seed(42)

# Generate bpsk signal 

no_of_bits = 20 

bits = np.random.randint(0,2,no_of_bits)

symbols = 2 * bits -1
sample_per_bit = 100 
N = sample_per_bit * no_of_bits # Total sample 

fc = 5 
fs= 100 
t = np.linspace (0,no_of_bits,N,endpoint=False)

# Bpsk modulation 

symbol_stream = np.repeat(symbols,sample_per_bit)
carrier = np.cos (2*np.pi* fc*t)

bpsk_signal = symbol_stream * carrier 

# noise generation 

sigma_noise = 0.5

noise = np.random.normal (0,sigma_noise, N)

##Experiment 01 :pulsed jammer 

fj= 8 # jammer frequency 
A = 1 

pulse = (np.sin(2*np.pi*1*t)>0).astype(float)
pulsed_jammer= A * pulse *np.cos(2*np.pi*fj*t)

received_pulse= bpsk_signal + noise + pulsed_jammer

## Time domain analysis 

fig, ax = plt.subplots(3,1, figsize=(10,10))

ax[0].plot(t, bpsk_signal)
ax[0].set_title("BPSK signal")
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("Amplitude")
ax[0].grid()

ax[1].plot(t, pulsed_jammer)
ax[1].set_title("Pulsed Jammer")
ax[1].set_xlabel("Time (s)")
ax[1].set_ylabel("Amplitude")
ax[1].grid()    

ax[2].plot(t, received_pulse)
ax[2].set_title("Received Signal (BPSK + Noise + Jammer)")
ax[2].set_xlabel("Time (s)")    
ax[2].set_ylabel("Amplitude")
ax[2].grid()    

plt.tight_layout()
plt.savefig("plots/pulsed_jammer_time_domain.png")
plt.close()

## Frequency domain analysis 

bpsk_fft = np.fft.fft(bpsk_signal)
pulsed_jammer_fft = np.fft.fft(pulsed_jammer)
received_signal_fft = np.fft.fft(received_pulse)
freqs = np.fft.fftfreq(N,1/fs)

fig,ax = plt.subplots(3,1,figsize=(10,10))

ax[0].plot(freqs, np.abs(bpsk_fft))
ax[0].set_title("BPSK Signal Spectrum")
ax[0].set_xlabel("Frequency (Hz)")
ax[0].set_ylabel("Magnitude")
ax[0].grid()

ax[1].plot(freqs, np.abs(pulsed_jammer_fft))
ax[1].set_title("Pulsed Jammer Spectrum")
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_ylabel("Magnitude")
ax[1].grid()

ax[2].plot(freqs, np.abs(received_signal_fft))
ax[2].set_title("Received Signal Spectrum")
ax[2].set_xlabel("Frequency (Hz)")
ax[2].set_ylabel("Magnitude")
ax[2].grid()

plt.tight_layout()
plt.savefig("plots/pulsed_jammer_frequency_domain.png")
plt.close()



## Experiment 02 : Stealth reactive jammer
 
trigger = (np.abs(bpsk_signal)>0.9).astype(float)

fake_symbols = np.random.choice([-1,1], size=no_of_bits)

fake_bits = np.repeat(
    fake_symbols,
    sample_per_bit
)

stealth_reactive = (0.3 * trigger * fake_bits*np.cos(2*np.pi*fc*t))


received_stealth = bpsk_signal + noise + stealth_reactive
 
## Time domain behavior 


fig, ax = plt.subplots(3,1, figsize=(10,10))

ax[0].plot(t, bpsk_signal)
ax[0].set_title("BPSK signal")
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("Amplitude")
ax[0].grid()

ax[1].plot(t, stealth_reactive)
ax[1].set_title("Stealth Reactive Jammer")
ax[1].set_xlabel("Time (s)")
ax[1].set_ylabel("Amplitude")
ax[1].grid()    

ax[2].plot(t, received_stealth)
ax[2].set_title("Received Signal (BPSK + Noise + Jammer)")
ax[2].set_xlabel("Time (s)")    
ax[2].set_ylabel("Amplitude")
ax[2].grid()    

plt.tight_layout()
plt.savefig("plots/stealth_jammer_time_domain.png")
plt.close()

## Frequency domain analysis 

stealth_jammer_fft = np.fft.fft(stealth_reactive)
received_signal_fft = np.fft.fft(received_stealth)


fig,ax = plt.subplots(3,1,figsize=(10,10))

ax[0].plot(freqs, np.abs(bpsk_fft))
ax[0].set_title("BPSK Signal Spectrum")
ax[0].set_xlabel("Frequency (Hz)")
ax[0].set_ylabel("Magnitude")
ax[0].grid()

ax[1].plot(freqs, np.abs(stealth_jammer_fft))
ax[1].set_title("Stealth Jammer Spectrum")
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_ylabel("Magnitude")
ax[1].grid()

ax[2].plot(freqs, np.abs(received_signal_fft))
ax[2].set_title("Received Signal Spectrum")
ax[2].set_xlabel("Frequency (Hz)")
ax[2].set_ylabel("Magnitude")
ax[2].grid()

plt.tight_layout()
plt.savefig("plots/stealth_jammer_frequency_domain.png")
plt.close()