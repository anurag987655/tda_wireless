import numpy as np 
import matplotlib.pyplot as plt 
import gudhi 
import os 


os.makedirs("plots",exist_ok=True)
np.random.seed(42)


# 2 dimensional delay embedding of a signal: 
def delay_embedding(signal,tau=5): 
    return np.column_stack([signal[:-tau],signal[tau:]])

# Draw a persistence diagram for a given signal: 
def draw_persistence(points,title):
    rips=gudhi.RipsComplex(points=points)
    simplex_tree = rips.create_simplex_tree(max_dimension=2)
    print(title)

    persistence = simplex_tree.persistence()

    h1_persistences = []

    # for dim, interval in persistence: 
    #     if dim == 1: 
    #         birth, death = interval 
    #         h1_persistences.append((birth, death, death - birth))

    # h1_persistences.sort(key=lambda x: x[2],reverse = True)
    # print("Number of H1 features:",len(h1_persistences))

    # print("Top 5 H1 persistences:")

    # for i,(birth,death,pers) in enumerate(h1_persistences[:5],start=1):
    #     print(f"{i}: birth={birth:.4f}, death = {death:.4f}, persistence={pers:.4f}")

    for dim, interval in persistence: 
        if dim == 1: 
            birth, death = interval 
            h1_persistences.append(death-birth)

    max_persistence = max(h1_persistences)
    print("Max Persistence",max_persistence)

    gudhi.plot_persistence_diagram(persistence)
    plt.title(title)
    plt.savefig(f"plots/{title}_persistence_diagram.png")
    plt.close()

    return max_persistence

# Drawing the plot maximum persistence vs noise strength for the given signal: 

def plot_persistence_vs_noise(max_persistences, title, noise_strengths=[0.1,0.3,0.5,1.0]):
    plt.figure(figsize=(10,10))
    plt.plot(noise_strengths,max_persistences, marker='o')
    plt.title(f"Maximum Persistence vs Noise Strength for {title}")
    plt.xlabel("Noise Strength")
    plt.ylabel("Maximum Persistence")
    plt.grid(True)
    plt.savefig(f"plots/{title}_persistence_vs_noise.png")
    plt.close()

# Saving the delay embedding of a given signal with the title: 

def save_embedding(points,title,noise): 
    plt.figure(figsize=(10,10))
    plt.scatter(points[:,0],points[:,1])
    plt.title(f"Delay embedding of {title} with noise={noise}")
    plt.axis('equal')
    plt.grid(True)
    plt.savefig(f"plots/Delay_embedding_{title}_noise_{noise}.png")
    plt.close()

    draw_persistence(points, f"Persistence of {title} with noise= {noise}")


# def show_signal_time_domain(signal,t,title):
#     plt.figure(figsize=(10,10))
#     plt.plot(t,signal)
#     plt.title(title)
#     plt.xlabel("Time")
#     plt.ylabel("Amplitude")
#     plt.grid(True)
#     plt.show()
#     plt.close()
# Generate a simple sine wave  

A = 1 
f = 5 
phi = 0 

t_sine = np.linspace(0,1,200)

sine_wave = A * np.sin(2 * np.pi * f * t_sine + phi)

# Generating Bpsk signal 

no_of_bits = 5 
bits = np.random.randint(0,2,no_of_bits)

symbol = 2 * bits - 1 

sample_per_bits = 100 
fc = 5 

N = no_of_bits * sample_per_bits

t_bpsk = np.linspace(0,no_of_bits,N,endpoint=False)

carrier = np.cos(2 * np.pi * fc * t_bpsk)

symbol_stream = np.repeat(symbol, sample_per_bits)

bpsk_signal = symbol_stream * carrier

## Showing the time domain signal 

# show_signal_time_domain(sine_wave,t_sine,"Sine Wave")
# show_signal_time_domain(bpsk_signal,t_bpsk,"BPSK Signal")


# Adding noise to the sine wave: 
## Generating a random normal noise 

sine_max_persistences=[]
bpsk_max_persistences=[]

noise_strength = [0.1,0.3,0.5,1.0]

for noise in noise_strength: 
    noisy_sine = sine_wave + np.random.normal(0,noise,size=sine_wave.shape)
    embedded_noisy_sine = delay_embedding(noisy_sine,tau=10)
    # save_embedding(embedded_noisy_sine, "Noisy Sine Wave", noise)   
    mp_sine = draw_persistence(embedded_noisy_sine,f"Sine noise ={noise}")
    sine_max_persistences.append(mp_sine)


    noisy_bpsk = bpsk_signal + np.random.normal(0,noise,size=bpsk_signal.shape)
    embedded_noisy_bpsk = delay_embedding(noisy_bpsk, tau=5)
    # save_embedding(embedded_noisy_bpsk, "Noisy BPSK Signal", noise)   
    mp_bpsk = draw_persistence(embedded_noisy_bpsk ,f"BPSK noise={noise}")
    bpsk_max_persistences.append(mp_bpsk)

plt.plot(noise_strength, sine_max_persistences, marker='o', label='Sine')
plt.plot(noise_strength, bpsk_max_persistences, marker='o', label='BPSK')

plt.xlabel("Noise Strength")
plt.ylabel("Max Persistence")
plt.title("Topology Stability vs Noise")
plt.grid(True)
plt.legend()
plt.savefig("plots/comparison.png")
plt.close()