import typing_extensions
from optimal_tau import * 
import pandas as pd 
import numpy as np 
# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt 
import os 

os.makedirs("results", exist_ok=True)
os.makedirs("plots", exist_ok=True)

np.random.seed(42) 

TRIALS = 10
tau = 2
SNRs = [30, 25, 20, 15, 10, 5, 0, -5]


def run_snr_experiment(snr, signal, tau=2, trials=10):
    """
        Args:
        snr: SNR level
        signal: clean signal
        tau: delay embedding parameter
        trials: number of trials

        Returns:
            Dict of mean & std for max persistence and entropy
    """
    max_p_list = []
    entropy_list = []

    for _ in range(trials):
        
        noisy = add_awgn_snr(signal, snr)
        embedded = delay_embedding(noisy,tau)
        points = subsample(embedded, 200)

        mp, entrp = compute_topological_metrics(points)

        max_p_list.append(mp)
        entropy_list.append(entrp)

    return {"snr": snr,"max_p_mean": np.mean(max_p_list),"max_p_std": np.std(max_p_list),"entropy_mean": np.mean(entropy_list),"entropy_std": np.std(entropy_list)}


def plot_results(df):
    df = df.sort_values("snr")

    plt.figure()

    plt.plot(df["snr"], df["max_p_mean"], marker='o', label="Max Persistence")
    plt.plot(df["snr"], df["entropy_mean"], marker='s', label="Entropy")

    plt.xlabel("SNR (dB)")
    plt.ylabel("Feature Value")
    plt.title("Topology vs SNR")
    plt.grid(True)
    plt.legend()

    plt.savefig("plots/features_vs_snr.png")
    plt.close()

I, Q, symbols = qpsk(1000)

x = gaussian_pulse_shaping(symbols, 20)

signal = x / np.std(x)

results = []

for snr in SNRs: 
    result = run_snr_experiment(snr, signal, tau, TRIALS)
    results.append(result)

df = pd.DataFrame(results)
print(df) 

df.to_csv(f"results/snr_experiment_qpsk.csv", index=False)      


plot_results(df)   
