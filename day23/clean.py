import numpy as np 
import matplotlib.pyplot as plt 
import gudhi 
import os 

os.makedirs("plots",exist_ok=True)
np.random.seed(42)

def delay_embedding_2d(signal,tau=5):
    return np.column_stack([signal[:-tau],signal[tau:]])

# Draw a persistence diagram for a given signal : 

def draw_persistence(points,title):
    rips = gudhi.RipsComplex(points=points)
    simplex_tree= rips.create_simplex_tree(max_dimension=2)

    print(title)


    persistence = simplex_tree.persistence()
    for dim, interval in persistence: 
        if dim == 1: 
            print(interval)

    gudhi.plot_persistence_diagram(persistence)
    plt.title(title)
    plt.savefig(f"plots/{title}_persistence_diagram.png")
    plt.close()

def save_embedding(points,title,tau):
    plt.figure(figsize=(10,10))
    plt.scatter(points[:,0],points[:,1])
    plt.axis('equal')
    plt.grid(True)

    plt.title(f"Delay embedding with tau={tau}")
    plt.savefig(f"plots/Delay_embedding_{title}_{tau}.png")
    plt.close()

    draw_persistence(points, f"Persistence of {title} tau={tau}")

# Generate a simple sine wave 

A = 1 
f = 5 
phi = 0 

t = np.linspace(0,1,200)

sine_wave = A * np.sin(2 * np.pi * f * t  + phi)


# Generating the square wave
square_wave = np.sign(np.sin(2*np.pi*f*t + phi))

embedded_sine = delay_embedding_2d(sine_wave)
embedded_square = delay_embedding_2d(square_wave)

## Bpsk signal generation : 

no_of_bits = 5 
bits = np.random.randint(0,2,no_of_bits)

symbols = 2 * bits - 1 

samples_per_bit = 100 
fc = 5 

N = no_of_bits * samples_per_bit
t = np.linspace(0,no_of_bits,N,endpoint=False)

symbol_stream = np.repeat(symbols, samples_per_bit)

carrier = np.cos(2* np.pi * fc * t)

bpsk_signal = symbol_stream * carrier

values = [5,10,15,20,25]

for tau in values:
    embedded_sine = delay_embedding_2d(sine_wave,tau=tau)
    embedded_square = delay_embedding_2d(square_wave,tau=tau)
    embedded_bpsk = delay_embedding_2d(bpsk_signal,tau=tau)

    save_embedding(embedded_sine, "Sine Wave", tau)
    save_embedding(embedded_square, "Square Wave", tau)
    save_embedding(embedded_bpsk, "BPSK Signal", tau)


