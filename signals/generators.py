import numpy as np 
from signal_base import Signal

## Generator for various signal 
# 1)sine wave
# 2)Multitone signal
# 3)Bpsk signal 
# 4)Qpsk signal 
# 5)Bfsk signal

def sine_wave(
        amplitude=1.0,frequency=5.0, phase = 0.0, fs=1000, duration=1.0
        ):
    
    t = np.arange(0,duration,1/fs)
    x = amplitude * np.sin(2*np.pi*frequency*t + phase)
    return Signal(x,t,"Sine Wave")

def multi_sine(frequencies, amplitudes=None, fs = 1000, duration =1.0):
    t = np.arange(0, duration, 1/fs)
    if amplitudes is None: 
        amplitudes = [1.0]*len(frequencies)
    x = np.zeros_like(t)

    for A, f in zip(amplitudes, frequencies): 
        x+=A*np.sin(2*np.pi*f*t)
    
    return Signal(x,t,"Multi Sine")

def white_noise(sigma = 1.0 , fs = 1000 , duration = 1.0):
    t = np.arange(0,duration,1/fs)
    x = np.random.normal(0,sigma,len(t))

    return Signal(x,t,"White Noise")

def bpsk(num_bits =100, samples_per_bit = 50): 
    bits = np.random.randint(0,2,num_bits)
    symbol = 2 * bits -1

    x = np.repeat(symbol , samples_per_bit)

    t  =np.arange(len(x))/samples_per_bit

    return Signal(x,t,"BPSK")

def qpsk(num_symbols=1000, samples_per_symbol=20):

    bits = np.random.randint(0,2,2*num_symbols)

    I = 2*bits[0::2]-1
    Q = 2*bits[1::2]-1

    symbols = (I + 1j*Q)/np.sqrt(2)

    x = np.repeat(symbols,samples_per_symbol)

    t = np.arange(len(x))/samples_per_symbol

    return Signal(x,t,"QPSK")
         

def bfsk(num_bits = 50 , f0 = 5 , f1=20, fs =100, bit_duration = 0.1): 
    bits = np.random.randint(0,2,num_bits)
    waveform = []
    t_bit = np.arange(0,bit_duration,1/fs)
    for bit in bits: 
    
        freq = f1 if bit else f0 

        waveform.extend(np.sin(2*np.pi*freq*t_bit))

    x= np.array(waveform)
    t = np.arange(len(x))/fs
    return Signal(x,t,"BFSK")


def qpsk_symbols(num_symbols=100):
    """Generate normalized QPSK symbols for OFDM subcarriers."""
    bits = np.random.randint(0, 2, size=2 * num_symbols)
    i = 2 * bits[0::2] - 1
    q = 2 * bits[1::2] - 1
    return (i + 1j * q) / np.sqrt(2)


def ofdm(num_ofdm_symbols=10, n_subcarriers=64, cp_length=16, fs=8000, modulation="qpsk", carrier_freq=0.0):
    """Generate a simple OFDM waveform.

    Parameters
    ----------
    num_ofdm_symbols : int
        Number of OFDM symbols to generate.
    n_subcarriers : int
        Number of subcarriers per OFDM symbol.
    cp_length : int
        Length of the cyclic prefix in samples.
    fs : float
        Sampling frequency (Hz) for the time axis.
    modulation : str
        Only 'qpsk' is supported in this helper.
    carrier_freq : float
        Carrier frequency for passband output. If 0.0, the returned signal is complex baseband.
    """
    if modulation.lower() != "qpsk":
        raise ValueError("Only 'qpsk' modulation is implemented for OFDM generation.")
    if n_subcarriers <= 0 or cp_length < 0:
        raise ValueError("n_subcarriers must be positive and cp_length must be non-negative.")

    symbols = qpsk_symbols(num_ofdm_symbols * n_subcarriers)
    freq_grid = symbols.reshape(num_ofdm_symbols, n_subcarriers)
    time_grid = np.fft.ifft(freq_grid, axis=1)

    if cp_length > 0:
        cyclic_prefix = time_grid[:, -cp_length:]
        time_grid = np.concatenate([cyclic_prefix, time_grid], axis=1)

    x = time_grid.ravel()
    t = np.arange(len(x)) / fs

    if carrier_freq != 0.0:
        x = np.real(x * np.exp(2j * np.pi * carrier_freq * t))

    return Signal(x, t, f"OFDM_{n_subcarriers}_{modulation.upper()}")