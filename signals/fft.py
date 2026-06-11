import numpy as np 
import matplotlib.pyplot as plt 

def compute_fft(signal):
    x=signal.x 
    fs = signal.sampling
    N=len(x)

    fft_vals = np.fft.rfft(x)

    freqs = np.fft.rfftfreq(N,d=1/fs)

    magnitude = np.abs(fft_vals)

    return freqs, magnitude

def dominant_frequency(signal):
    freqs,magnitude= compute_fft(signal)
    idx= np.argmax(magnitude)

    return freqs[idx]

def plot_fft(signal, title=None):
    freqs,magnitude =compute_fft(signal)

    plt.figure(figsize=(10,10))
    plt.plot(freqs,magnitude)

    plt.xlabel("Frequency(Hz)")
    plt.ylabel("Magnitude")

    if title: 
        plt.title(title)

    plt.grid(True)
    plt.show()
    plt.close()


def power_spectrum(signal):
    freqs,magnitude = compute_fft(signal)

    power = magnitude ** 2 

    return freqs, power

def plot_power_spectrum(signal, title = None): 

    freqs, power = power_spectrum(signal)
    plt.figure(figsize=(10,10))
    plt.plot(freqs,power)

    plt.xlabel("Frequency(Hz)")
    plt.ylabel("Power")

    if title: 
        plt.title(title)

    plt.grid()
    plt.show()
    plt.close()