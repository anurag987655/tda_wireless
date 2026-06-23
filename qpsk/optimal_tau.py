import numpy as np 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os  
import  gudhi 

np.random.seed(42)

def add_awgn_snr(signal, snr_db):
    signal_power = np.mean(np.abs(signal)**2)
    snr_linear=10**(snr_db/10)

    noise_power = signal_power/snr_linear
    
    sigma = np.sqrt(noise_power/2)

    noise = sigma * (np.random.randn(len(signal)) + 1j * np.random.randn(len(signal)))

    return signal + noise


def qpsk(no_of_symbols = 1000): 
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


def delay_embedding(signal, tau):
    # Returns 4D point cloud if complex, 2D if real
    if np.iscomplexobj(signal):
        return np.column_stack([
            signal[:-tau].real,
            signal[:-tau].imag,
            signal[tau:].real,
            signal[tau:].imag
        ])
    return np.column_stack([signal[:-tau], signal[tau:]])

def plot_embedding(points, tau, title): 
    if points.shape[1] == 4:
        fig, axes = plt.subplots(1, 2, figsize=(15, 7))
        
        # In-phase delay embedding
        axes[0].scatter(points[:, 0], points[:, 2], s=6, alpha=0.4, color='dodgerblue')
        axes[0].set_title("In-Phase (I) Delay Embedding")
        axes[0].set_xlabel("I(n)")
        axes[0].set_ylabel(f"I(n+{tau})")
        axes[0].grid(True)
        axes[0].axis('equal')
        
        # Quadrature delay embedding
        axes[1].scatter(points[:, 1], points[:, 3], s=6, alpha=0.4, color='darkorange')
        axes[1].set_title("Quadrature (Q) Delay Embedding")
        axes[1].set_xlabel("Q(n)")
        axes[1].set_ylabel(f"Q(n+{tau})")
        axes[1].grid(True)
        axes[1].axis('equal')
        
        fig.suptitle(f"Delay embedding of {title} for tau ={tau}", fontsize=14)
        plt.tight_layout()
        plt.savefig(f"plots/{title} delay embedding with tau ={tau}.png")
        plt.close()
    else:
        plt.figure(figsize=(10, 10))
        plt.scatter(points[:, 0], points[:, 1], s=15)
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

    # Step 1: Upsample (support complex dtype)
    upsampled = np.zeros(len(symbols) * samples_per_symbol, dtype=complex)
    upsampled[::samples_per_symbol] = symbols

    # Step 2: Gaussian kernel
    t = np.arange(-4*sigma, 4*sigma+1)
    g = np.exp(-(t**2) / (2*sigma**2))
    g = g / np.sum(g)

    # Step 3: Convolution (this creates smooth waveform)
    shaped = np.convolve(upsampled, g, mode="same")

    return shaped


## Defining the function max_persistence which returns the maximum h1 persistence

def max_persistence(points, max_dim = 1): 
    """
    compute maximum H1 persistence from a given cloud points.
    """
    rips = gudhi.RipsComplex(points=points)
    st = rips.create_simplex_tree(max_dimension= 2)

    st.compute_persistence()

    diag = st.persistence()
    lifetimes = []

    for dim, (birth,death) in diag: 
        if dim == 1 and death != float('inf'):
            lifetimes.append(death - birth)
        
    if len(lifetimes) == 0: 
        return 0 
    
    return np.max(lifetimes)

def subsample(points,max_points=1000):
    if len(points) > max_points:
        idx = np.random.choice(len(points), max_points, replace=False)
        return points[idx]
        
    return points   

def tau_vs_persistence(signal,tau_vals):
    results = []

    for tau in tau_vals:
        embedded = delay_embedding(signal,tau)

        embedded = subsample(embedded)

        mp = max_persistence(embedded)
        results.append(mp)

        print(f"tau={tau}, max persistence={mp:.4f}")
    return np.array(results)


def draw_tau_vs_persistence(max_pers, tau_vals,s):
    plt.figure(figsize=(10,10))
    plt.plot(tau_vals, max_pers, marker='o')
    plt.xlabel("tau")
    plt.ylabel("Max H1 Persistence")
    plt.title(f"Tau vs Persistence ({s} symbols)")
    plt.grid()
    plt.savefig(f"plots/tau_vs_persistence_{s}.png")
    plt.close()

def compute_topological_metrics(points): 
    rips = gudhi.RipsComplex(points=points)
    st = rips.create_simplex_tree(max_dimension=2)
    st.compute_persistence()
    diag = st.persistence()
    
    lifetimes = []
    for dim, (birth, death) in diag: 
        if dim == 1 and death != float('inf'):
            lifetimes.append(death - birth)
        
    if len(lifetimes) == 0: 
        return 0.0, 0.0, 0.0
    
    lifetimes = np.array(lifetimes)
    max_p = np.max(lifetimes)
    mean_p = np.mean(lifetimes) # computing mean persistence 
    total_p = np.sum(lifetimes)
    
    # Persistence Entropy
    probs = lifetimes / total_p
    entropy = -np.sum(probs * np.log(probs + 1e-12))
    
    return max_p, mean_p, entropy



if __name__ == '__main__':
    ## choosing the best tau 
    symbols_choice = [50, 100, 200, 500, 1000]
    tau = range(1,21)
    for s in symbols_choice:
        I, Q, symbol = qpsk(s)
        x = gaussian_pulse_shaping(symbol, samples_per_symbol=20)
        signal = x / np.std(x)
        results=[]
        for tau_val in tau:
            embedded = delay_embedding(signal, tau_val)
            embedded = subsample(embedded,max_points =200)
            max_p, _ = compute_topological_metrics(embedded)
            results.append(max_p)
        
        draw_tau_vs_persistence(results, tau, s)


