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

def qpsk(num_symbols=100, samples_per_symbol=100):
    I = np.random.choice([-1,1],num_symbols)
    Q = np.random.choice([-1,1],num_symbols)

    symbols = I + 1j * Q 

    x = np.repeat(np.real(symbols),samples_per_symbol)

    t = np.arange(len(x))

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