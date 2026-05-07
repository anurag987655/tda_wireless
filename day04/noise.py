import matplotlib.pyplot as plt
import numpy as np 
import os 


os.makedirs('plots', exist_ok=True)


## Experiment 1 : Analysis of white noise 

N = 1000 

noise = np.random.normal(
    loc=0,      # mean
    scale=1,    # std
    size=N
)

fig , ax = plt.subplots(3,1,figsize=(10,4))

# Noise in time domain 

ax[0].plot(noise)
ax[0].set_title("AWGN in time domain")
ax[0].set_xlabel("Sample Index")
ax[0].set_ylabel("Amplitude")
ax[0].grid()


## Histogram plot 

ax[1].hist(noise, bins= 30)
ax[1].set_title("Histogram of AWGN")
ax[1].set_xlabel("Amplitude") 
ax[1].set_ylabel("count")
ax[1].grid()    

## fft plot 

noise_fft = np.fft.fft(noise)
magnitude = np.abs(noise_fft)
freq = np.fft.fftfreq(N)

ax[2].plot(freq , magnitude)

ax[2].set_title("FFT of AWGN")
ax[2].set_xlabel("Frequency")
ax[2].set_ylabel("Magnitude")
ax[2].grid()

plt.tight_layout()
plt.savefig("plots/awgn_analysis.png")


# Experiment 2 : Autocorrelation analysis of white noise

autocorr = np.correlate(noise, noise , mode = 'full')
lags  = np.arange (-N+1 , N)

plt.figure(figsize = (10,4))

plt.plot(lags, autocorr)
plt.title("Autocorrelation of AWGN")
plt.xlabel("lags")
plt.ylabel("Correlation")
plt.grid()

plt.tight_layout()
plt.savefig("plots/awgn_autocorrelation.png")

# Experiment 3 :BPSK + noise Analysis : 

bits = np.random.randint(0,2,20)

symbol = 2 * bits -1 


## generating carrier waveform 

samples_per_symbol = 100 
fc = 5 

symbol_wave = np.repeat(symbol, samples_per_symbol)

t= np.linspace(0, len(symbol), len(symbol_wave))

carrier = np.cos(2 * np.pi * fc * t)

bpsk_signal = symbol_wave * carrier


sigma = 0.5
noise = np.random.normal(0,sigma, len(bpsk_signal))
bpsk_signal = symbol_wave * carrier

noise = np.random.normal(0, sigma, len(bpsk_signal))


## additive noise 

received = bpsk_signal + noise 



## Time and frequency domain analysis of bpsk + noise

received = bpsk_signal + noise

fig ,ax = plt.subplots(2,2, figsize=(10,4))

# original bpsk signal 

ax[0,0].plot(t, bpsk_signal)
ax[0,0].set_title("Original BPSK (Time Domain)")
ax[0,0].set_xlabel("Sample Index")
ax[0,0].set_ylabel("Amplitude")
ax[0,0].grid()

#Noisy bpsk signal

ax[0,1].plot(t, received)
ax[0,1].set_title("Noisy BPSK (Time Domain)")
ax[0,1].set_xlabel("Sample Index")
ax[0,1].set_ylabel("Amplitude")
ax[0,1].grid()  

# Frequency domain analysis 

symbol_fft = np.fft.fftshift(np.fft.fft(bpsk_signal))
received_fft = np.fft.fftshift(np.fft.fft(received))
freq = np.fft.fftshift(np.fft.fftfreq(len(bpsk_signal)))

# Original spectrum 

ax[1,0].plot(freq, np.abs(symbol_fft))
ax[1,0].set_title("Original BPSK FFT")
ax[1,0].set_xlabel("Frequency")
ax[1,0].set_ylabel("Magnitude")
ax[1,0].grid()

# Noisy spectrum 

ax[1,1].plot(freq, np.abs(received_fft))
ax[1,1].set_title("Noisy BPSK (Frequency Domain)")
ax[1,1].set_xlabel("Frequency")
ax[1,1].set_ylabel("Magnitude")
ax[1,1].grid()

plt.tight_layout()
plt.savefig("plots/bpsk_noise_analysis.png")
plt.close()


# Experiment 4: BER vs SNR

N = 10000
bits = np.random.randint(0,2,N)

symbol = 2* bits - 1

snr_db_range = np.arange(0,11,2)
ber_values = []

for snr_db in snr_db_range:
    snr_linear = 10 ** (snr_db / 10 ) ## converting the db scale into normal scale
    sigma = np.sqrt(1/(2*snr_linear)) ## noise power is 1/2 of signal power for BPSK 
    noise = np.random.normal(0, sigma ,N )

    received = symbol + noise
    detected = (received > 0).astype(int)
    no_of_errors = np.sum(detected != bits)

    ber = no_of_errors / N
    ber_values.append(ber)

plt.figure(figsize=(10,4))
plt.semilogy(snr_db_range, ber_values, marker='o')

plt.title("BER vs SNR for BPSK")
plt.xlabel("SNR (dB)")
plt.ylabel("BER")
plt.grid()

plt.savefig("plots/ber_vs_snr.png")
plt.close()