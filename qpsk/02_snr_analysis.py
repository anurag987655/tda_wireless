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
    mean_p_list = []
    entropy_list = []

    for _ in range(trials):
        
        noisy = add_awgn_snr(signal, snr)
        noisy = noisy / np.std(noisy)
        embedded = delay_embedding(noisy,tau)
        points = subsample(embedded, 200)

        mp, mean_p, entrp = compute_topological_metrics(points)

        max_p_list.append(mp)
        mean_p_list.append(mean_p)
        entropy_list.append(entrp)

    return {"snr": snr,"max_p_mean": np.mean(max_p_list),"max_p_std": np.std(max_p_list),"mean_p_mean": np.mean(mean_p_list),"mean_p_std": np.std(mean_p_list), "entropy_mean": np.mean(entropy_list),"entropy_std": np.std(entropy_list)}


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


def run_full_experiment(seed):
    np.random.seed(seed)

    results = []

    for snr in SNRs:
        result = run_snr_experiment(snr, signal, tau, TRIALS)
        results.append(result)

    return pd.DataFrame(results)

I, Q, symbols = qpsk(1000)

x = gaussian_pulse_shaping(symbols, 20)

signal = x / np.std(x)

# results = []

# for snr in SNRs: 
#     result = run_snr_experiment(snr, signal, tau, TRIALS)
#     results.append(result)

# df = pd.DataFrame(results)
# print(df) 

# df.to_csv(f"results/snr_experiment_qpsk.csv", index=False)      


# plot_results(df)   

seeds = [0, 1, 42, 100]

all_runs = []

for s in seeds:
    df_run = run_full_experiment(s)
    df_run["seed"] = s
    all_runs.append(df_run)

df_all = pd.concat(all_runs)
df_stats = df_all.drop(columns=["seed"])

df_mean = df_stats.groupby("snr").mean(numeric_only=True)
df_std = df_stats.groupby("snr").std(numeric_only=True)


df_mean = df_mean.sort_index()
df_std = df_std.sort_index()

print("\nMean across seeds:")
print(df_mean)

print("\nStd across seeds:")
print(df_std)

df_mean.to_csv("results/stability_mean.csv")

df_std.to_csv("results/stability_std.csv")

plt.figure()

plt.plot(
    df_mean.index,
    df_mean["entropy_mean"],
    marker="o"
)

plt.fill_between(
    df_mean.index,
    df_mean["entropy_mean"]
      - df_std["entropy_mean"],
    df_mean["entropy_mean"]
      + df_std["entropy_mean"],
    alpha=0.3
)

plt.xlabel("SNR (dB)")
plt.ylabel("Persistence Entropy")
plt.grid(True)

plt.savefig(
    "plots/entropy_stability.png"
)
plt.close()

plt.figure()

plt.plot(
    df_mean.index,
    df_mean["max_p_mean"],
    marker="o"
)

plt.fill_between(
    df_mean.index,
    df_mean["max_p_mean"] - df_std["max_p_mean"],
    df_mean["max_p_mean"] + df_std["max_p_mean"],
    alpha=0.3
)

plt.xlabel("SNR (dB)")
plt.ylabel("Maximum Persistence")
plt.grid(True)

plt.savefig("plots/persistence_stability.png")
plt.close()

plt.figure()

plt.plot(
    df_mean.index,
    df_mean["mean_p_mean"],
    marker="o",
    color="crimson" # Distinct color for Mean Persistence
)

plt.fill_between(
    df_mean.index,
    df_mean["mean_p_mean"] - df_std["mean_p_mean"],
    df_mean["mean_p_mean"] + df_std["mean_p_mean"],
    color="crimson",
    alpha=0.3
)

plt.xlabel("SNR (dB)")
plt.ylabel("Mean Persistence")
plt.title("Mean Persistence Stability across Seeds")
plt.grid(True)

plt.savefig("plots/mean_persistence_stability.png")
plt.close()