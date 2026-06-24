import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

from optimal_tau import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


os.makedirs("results", exist_ok=True)
os.makedirs("plots", exist_ok=True)

TRIALS = int(os.environ.get("QPSK_TRIALS", "10"))
TAU = int(os.environ.get("QPSK_TAU", "15"))
MAX_POINTS = int(os.environ.get("QPSK_MAX_POINTS", "200"))
SYMBOLS = int(os.environ.get("QPSK_SYMBOLS", "1000"))
SAMPLES_PER_SYMBOL = int(os.environ.get("QPSK_SAMPLES_PER_SYMBOL", "20"))
SNRs = [30, 25, 20, 15, 10, 5, 0, -5]
SEEDS = [0, 1, 42, 100]
NORMALIZATION_MODES = ["shape_normalized", "physical_scale"]


def make_clean_signal(seed, symbols=SYMBOLS):
    np.random.seed(seed)
    _, _, qpsk_symbols = qpsk(symbols)
    shaped = gaussian_pulse_shaping(qpsk_symbols, SAMPLES_PER_SYMBOL)
    return shaped / np.std(shaped)


def metric_record(seed, trial, snr, signal, normalization_mode, tau=TAU):
    noisy = add_awgn_snr(signal, snr)

    if normalization_mode == "shape_normalized":
        noisy = noisy / np.std(noisy)
    elif normalization_mode != "physical_scale":
        raise ValueError(f"Unknown normalization mode: {normalization_mode}")

    embedded = delay_embedding(noisy, tau)
    points = subsample(embedded, MAX_POINTS)
    max_p, mean_p, entropy, normalized_entropy, h1_bar_count = compute_topological_metrics(points)

    return {
        "seed": seed,
        "trial": trial,
        "snr": snr,
        "normalization_mode": normalization_mode,
        "tau": tau,
        "symbols": SYMBOLS,
        "max_points": MAX_POINTS,
        "max_persistence": max_p,
        "mean_persistence": mean_p,
        "persistence_entropy": entropy,
        "normalized_entropy": normalized_entropy,
        "h1_bar_count": h1_bar_count,
    }


def run_trial_level_experiment():
    records = []

    for seed in SEEDS:
        clean_signal = make_clean_signal(seed)

        for normalization_mode in NORMALIZATION_MODES:
            for snr in SNRs:
                for trial in range(TRIALS):
                    records.append(
                        metric_record(
                            seed=seed,
                            trial=trial,
                            snr=snr,
                            signal=clean_signal,
                            normalization_mode=normalization_mode,
                        )
                    )

    return pd.DataFrame(records)


def summarize_trials(df):
    metric_cols = [
        "max_persistence",
        "mean_persistence",
        "persistence_entropy",
        "normalized_entropy",
        "h1_bar_count",
    ]

    summary = (
        df.groupby(["normalization_mode", "snr"])[metric_cols]
        .agg(["mean", "std", "count"])
        .reset_index()
    )
    summary.columns = [
        metric if stat == "" else f"{metric}_{stat}"
        for metric, stat in summary.columns.to_flat_index()
    ]
    if "index" in summary.columns:
        summary = summary.drop(columns=["index"])

    for metric in metric_cols:
        summary[f"{metric}_sem"] = (
            summary[f"{metric}_std"] / np.sqrt(summary[f"{metric}_count"])
        )

    return summary.sort_values(["normalization_mode", "snr"])


def write_legacy_tables(summary):
    normalized = summary[summary["normalization_mode"] == "shape_normalized"]
    normalized = normalized.set_index("snr").sort_index()

    mean_cols = {
        "max_persistence_mean": "max_p_mean",
        "max_persistence_std": "max_p_std",
        "mean_persistence_mean": "mean_p_mean",
        "mean_persistence_std": "mean_p_std",
        "persistence_entropy_mean": "entropy_mean",
        "persistence_entropy_std": "entropy_std",
        "normalized_entropy_mean": "normalized_entropy_mean",
        "normalized_entropy_std": "normalized_entropy_std",
        "h1_bar_count_mean": "h1_bar_count_mean",
        "h1_bar_count_std": "h1_bar_count_std",
    }

    legacy = normalized[list(mean_cols.keys())].rename(columns=mean_cols)
    legacy.to_csv("results/stability_summary_shape_normalized.csv")


def plot_metric(summary, metric, ylabel, filename):
    plt.figure()

    for normalization_mode, group in summary.groupby("normalization_mode"):
        group = group.sort_values("snr")
        label = normalization_mode.replace("_", " ")
        mean = group[f"{metric}_mean"]
        sem = group[f"{metric}_sem"]

        plt.plot(group["snr"], mean, marker="o", label=label)
        plt.fill_between(group["snr"], mean - sem, mean + sem, alpha=0.2)

    plt.xlabel("SNR (dB)")
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    plt.savefig(filename)
    plt.close()


def plot_all(summary):
    plot_metric(
        summary,
        "max_persistence",
        "Maximum H1 Persistence",
        "plots/persistence_stability.png",
    )
    plot_metric(
        summary,
        "mean_persistence",
        "Mean H1 Persistence",
        "plots/mean_persistence_stability.png",
    )
    plot_metric(
        summary,
        "persistence_entropy",
        "Persistence Entropy",
        "plots/entropy_stability.png",
    )
    plot_metric(
        summary,
        "normalized_entropy",
        "Normalized Persistence Entropy",
        "plots/normalized_entropy_stability.png",
    )
    plot_metric(
        summary,
        "h1_bar_count",
        "H1 Bar Count",
        "plots/h1_bar_count_stability.png",
    )


if __name__ == "__main__":
    df_trials = run_trial_level_experiment()
    df_summary = summarize_trials(df_trials)

    df_trials.to_csv("results/snr_experiment_qpsk_trials.csv", index=False)
    df_summary.to_csv("results/snr_experiment_qpsk_summary.csv", index=False)
    write_legacy_tables(df_summary)
    plot_all(df_summary)

    print("\nTrial-level summary:")
    print(df_summary)
