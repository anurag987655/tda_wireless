import numpy as np 
import matplotlib.pyplot as plt 
import os  

os.makedirs("plots",exist_ok=True)
np.random.seed(42)

def add_awgn_snr(signal, snr_db):
    signal_power = np.mean(np.abs(signal)**2)
    snr_linear=10**(snr_db/10)

    noise_power = signal_power/snr_linear
    
    sigma = np.sqrt(noise_power/2)

    noise = sigma * (np.random.randn(len(signal)) + 1j * np.random.randn(len(signal)))

    return signal + noise


def qpsk(no_of_symbols = 1000, sample_per_symbol = 20): 
    bits = np.random.randint(0,2,2*no_of_symbols)

    I = 2*bits[0::2] -1
    Q = 2*bits[1::2] -1

    symbol = I + 1j * Q

    return I, Q , symbol


def plot_constellation(I,Q): 
    plt.figure(figsize=(10,10))
    plt.scatter(I,Q,s=15)
    plt.xlabel("In-Phase(I)")
    plt.ylabel("Quadrature(Q)")
    plt.grid(True)
    plt.axis("equal")
    plt.show()
    plt.close()

def plot_I(I, samples=100):
    plt.figure(figsize=(10,4))

    plt.plot(I[:samples])

    plt.title("I Component")
    plt.xlabel("Symbol Index")
    plt.ylabel("Amplitude")

    plt.grid(True)
    plt.show()
    plt.close()

def plot_Q(Q, samples=100):
    plt.figure(figsize=(10,4))

    plt.plot(Q[:samples])

    plt.title("Q Component")
    plt.xlabel("Symbol Index")
    plt.ylabel("Amplitude")

    plt.grid(True)
    plt.show()
    plt.close()


def delay_embedding(signal,tau):
    return np.column_stack([signal[:-tau],signal[tau:]])

def plot_embedding(points,tau,title): 
    plt.figure(figsize=(10,10))
    plt.scatter(points[:,0],points[:,1])
    plt.title(f"Delay embedding of {title} for tau ={tau}")
    plt.xlabel("x(n)")
    plt.ylabel(f"x(n+{tau})")

    plt.grid(True)
    plt.savefig(f"plots/{title} delay embedding with tau ={tau}.png")
    plt.close()


def gaussian_pulse_shaping(symbols, samples_per_symbol=20, sigma=2):
    """
    Simple pulse shaping using Gaussian convolution.
    Not strict telecom standard, but perfect for experiments.
    """

    # Step 1: Upsample (this is NOT repeat, it's sparse insertion)
    upsampled = np.zeros(len(symbols) * samples_per_symbol)
    upsampled[::samples_per_symbol] = symbols

    # Step 2: Gaussian kernel
    t = np.arange(-4*sigma, 4*sigma+1)
    g = np.exp(-(t**2) / (2*sigma**2))
    g = g / np.sum(g)

    # Step 3: Convolution (this creates smooth waveform)
    shaped = np.convolve(upsampled, g, mode="same")

    return shaped

I, Q, symbols = qpsk(1000)
# plot_I(I)
# plot_Q(Q)
# plot_constellation(I,Q)


x = gaussian_pulse_shaping(symbols.real, samples_per_symbol=20)

signal = np.real(x)
plt.plot(x[:300])
plt.title("Pulse Shaped QPSK (I component)")
plt.grid()
plt.savefig("plots/pulse shaped qpsk.png")

tau = [5,10,15,20]

for t in tau:
   embedded =  delay_embedding(signal,t) 
   plot_embedding(embedded,t,"pulse shaped qpsk")

SNR = [30,20,10,5,0]

for s in SNR: 
    r = add_awgn_snr(signal,s)

    # plt.figure(figsize=(10,4))
    # plt.plot(r[:300])
    # plt.title(f"SNR = {s} dB")
    # plt.grid(True)

    # plt.show()
    # plt.close()

    for tau in [5,10,15,20]:
        embedded = delay_embedding(r,tau)

        plot_embedding(embedded,tau,f"Pulse_shaped_QPSK_AWGN_{s}DB")