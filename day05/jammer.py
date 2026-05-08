
import numpy as np 
import matplotlib.pyplot as plt 
import os 

np.random.seed(42)
os.makedirs("plots",exist_ok=True)

#Generate Bpsk signal 


no_of_bits = 20 

bits = np.random.randint(0,2,no_of_bits)

# Bit mapping 

symbols = 2 * bits -1 
samples_per_bit = 100 
N= no_of_bits * samples_per_bit

#carrier signal 

fc= 5
fs = 100 
t = np.linspace(0,no_of_bits,N, endpoint=False)

#Bpsk modulation 
symbol_stream = np.repeat(symbols, samples_per_bit)
carrier = np.cos(2*np.pi*fc*t)
bpsk_signal = symbol_stream * carrier

#Generate AWGN noise 

sigma_noise = 0.5 
noise = np.random.normal(0,sigma_noise, N)


# Experiment 1 : Barrage jammer

sigma_jammer = 1.5 
jammer_noise = np.random.normal(0, sigma_jammer, N)


received_signal = bpsk_signal + noise + jammer_noise

fig, ax = plt.subplots(3,1, figsize=(10,10))
ax[0].plot(t, bpsk_signal)
ax[0].set_title("BPSK signal")
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("Amplitude")
ax[0].grid()

ax[1].plot(t, jammer_noise)
ax[1].set_title("Jammer Noise")
ax[1].set_xlabel("Time (s)")
ax[1].set_ylabel("Amplitude")
ax[1].grid()    

ax[2].plot(t, received_signal)
ax[2].set_title("Received Signal (BPSK + Noise + Jammer)")
ax[2].set_xlabel("Time (s)")    
ax[2].set_ylabel("Amplitude")
ax[2].grid()    

plt.tight_layout()
plt.savefig("plots/bpsk_barrage_jammer_time_domain.png")
plt.close()

## frequency domain analysis of barrage jammer 

fft_bpsk = np.fft.fft(bpsk_signal)
fft_jammer = np.fft.fft(jammer_noise)
fft_received = np.fft.fft(received_signal)
freqs= np.fft.fftfreq(N, 1/fs)

fig , ax = plt.subplots(3,1, figsize=(10,10))

ax[0].plot(freqs, np.abs(fft_bpsk))
ax[0].set_title("BPSK Signal Spectrum")
ax[0].set_xlabel("Frequency (Hz)")
ax[0].set_ylabel("Magnitude")
ax[0].grid()

ax[1].plot(freqs, np.abs(fft_jammer))
ax[1].set_title("Jammer Noise Spectrum")
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_ylabel("Magnitude")
ax[1].grid()

ax[2].plot(freqs, np.abs(fft_received))
ax[2].set_title("Received Signal Spectrum")
ax[2].set_xlabel("Frequency (Hz)")
ax[2].set_ylabel("Magnitude")
ax[2].grid()

plt.tight_layout()
plt.savefig("plots/bpsk_barrage_jammer_frequency_domain.png")
plt.close()


# Experiment 2 : Tone jammer 

fj = 8 # jammer frequency 

jammer_signal = 0.5 * np.cos (2* np.pi * fj * t)
received_toner_signal = bpsk_signal + noise + jammer_signal

# Time domain analysis of tone jammer 

fig, ax = plt.subplots(3,1, figsize=(10,10))
ax[0].plot(t,bpsk_signal)
ax[0].set_title("BPSK signal")
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("Amplitude")
ax[0].grid()

ax[1].plot(t, jammer_signal)
ax[1].set_title("Tone Jammer Signal")
ax[1].set_xlabel("Time (s)")
ax[1].set_ylabel("Amplitude")
ax[1].grid()

ax[2].plot(t, received_toner_signal)
ax[2].set_title("Received Signal (BPSK + Noise + Tone Jammer)")
ax[2].set_xlabel("Time (s)")
ax[2].set_ylabel("Amplitude")
ax[2].grid()

plt.tight_layout()
plt.savefig("plots/bpsk_tone_jammer_time_domain.png")
plt.close()

# Frequency domain analysis of tone jammer

fft_tone_jammer = np.fft.fft(jammer_signal)
fft_received_tone = np.fft.fft(received_toner_signal)

fig, ax = plt.subplots(3,1, figsize=(10,10))

ax[0].plot(freqs, np.abs(fft_bpsk))
ax[0].set_title("BPSK Signal Spectrum")
ax[0].set_xlabel("Frequency (Hz)")
ax[0].set_ylabel("Magnitude")
ax[0].grid()

ax[1].plot(freqs, np.abs(fft_tone_jammer))
ax[1].set_title("Tone Jammer Spectrum")
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_ylabel("Magnitude")
ax[1].grid()

ax[2].plot(freqs, np.abs(fft_received_tone))
ax[2].set_title("Received Signal Spectrum")
ax[2].set_xlabel("Frequency (Hz)")
ax[2].set_ylabel("Magnitude")
ax[2].grid()

plt.tight_layout()
plt.savefig("plots/bpsk_tone_jammer_frequency_domain.png")
plt.close()


# Experiment 3 : Reactive jammer : core  basis of hypothesis

reactive_jammer = np.where(np.abs(bpsk_signal)>0.95,2*np.random.normal(0,1,len(bpsk_signal)),0)

received_reactive_signal = bpsk_signal + noise + reactive_jammer 

## Time domain plot of reactive jammer along with signal and noise

fig , ax = plt.subplots(3,1, figsize = (10,10))

ax[0].plot(t, bpsk_signal)
ax[0].set_title("BPSK signal")
ax[0].set_xlabel("Time(s)")
ax[0].set_ylabel("Amplitude")
ax[0].grid()

ax[1].plot(t,reactive_jammer)
ax[1].set_title("Reactive jammer signal")
ax[1].set_xlabel("Time(s)")
ax[1].set_ylabel("Amplitude")
ax[1].grid()

ax[2].plot(t,received_reactive_signal)
ax[2].set_title("Received signal(BPSK + Noise + Reactive jammer)")
ax[2].set_xlabel("Time(s)")
ax[2].set_ylabel("Amplitude")
ax[2].grid()

plt.tight_layout()
plt.savefig("plots/bpsk_reactive_jammer_time_domain.png")
plt.close()

## Frequency domain plot of reactive jammer along with signal and noise

fft_reactive_jammer= np.fft.fft(reactive_jammer)
fft_received_reactive = np.fft.fft(received_reactive_signal)

fig, ax = plt.subplots(3,1,figsize = (10,10))

ax[0].plot(freqs, np.abs(fft_bpsk))
ax[0].set_title("BPSK Signal Spectrum")
ax[0].set_xlabel("Frequency (Hz)")
ax[0].set_ylabel("Magnitude")
ax[0].grid()

ax[1].plot(freqs, np.abs(fft_reactive_jammer))
ax[1].set_title("Reactive Jammer Spectrum")
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_ylabel("Magnitude")
ax[1].grid()

ax[2].plot(freqs, np.abs(fft_received_reactive))
ax[2].set_title("Received Signal Spectrum")
ax[2].set_xlabel("Frequency (Hz)")
ax[2].set_ylabel("Magnitude")
ax[2].grid()

plt.tight_layout()
plt.savefig("plots/bpsk_reactive_jammer_frequency_domain.png")
plt.close()