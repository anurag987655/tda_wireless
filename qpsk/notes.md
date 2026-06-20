# QPSK Delay Embedding Notes

This note summarizes what can be concluded from the plots in [plots](plots) for the pulse-shaped QPSK experiment in [qpsk.py](qpsk.py).

## 1. Experiment Setup

The experiment generates random QPSK symbols, applies a Gaussian pulse-shaping filter, normalizes the complex signal, and then forms delay embeddings. Since the signal is complex, the embedding is internally 4D:

- `I(n)`
- `Q(n)`
- `I(n + tau)`
- `Q(n + tau)`

For visualization, each saved delay plot shows two 2D projections:

- left: in-phase delay embedding, `I(n)` vs `I(n + tau)`
- right: quadrature delay embedding, `Q(n)` vs `Q(n + tau)`

The plots are generated for clean pulse-shaped QPSK and for AWGN-corrupted signals at 30 dB, 20 dB, 10 dB, 5 dB, and 0 dB.

## 2. Main Visual Conclusion

The delay embedding captures the memory introduced by pulse shaping. The clean QPSK signal does not fill the plane randomly. Instead, the points form a structured, symmetric pattern with many samples concentrated near the origin and repeated branches away from the origin.

This happens because the Gaussian pulse shaping spreads each QPSK symbol over nearby samples. Nearby samples are therefore correlated, and the delay embedding exposes that correlation.

The clean reference plots are:

- [pulse shaped qpsk.png](plots/pulse%20shaped%20qpsk.png)
- [clean tau = 5](plots/pulse%20shaped%20qpsk%20delay%20embedding%20with%20tau%20%3D5.png)
- [clean tau = 10](plots/pulse%20shaped%20qpsk%20delay%20embedding%20with%20tau%20%3D10.png)
- [clean tau = 15](plots/pulse%20shaped%20qpsk%20delay%20embedding%20with%20tau%20%3D15.png)
- [clean tau = 20](plots/pulse%20shaped%20qpsk%20delay%20embedding%20with%20tau%20%3D20.png)

## 3. Effect of Tau

The value of `tau` controls how far apart the compared samples are.

- `tau = 5`: samples are close in time, so the embedding is compact and strongly tied to local pulse-shape correlation.
- `tau = 10`: the structure opens up and the branches become easier to see.
- `tau = 15`: the separated branch structure is strong and visually clear.
- `tau = 20`: the embedding spreads farther and shows longer-delay relationships between samples.

Visually, larger `tau` values make the geometry more spread out. However, the persistence plots show that "more spread" is not always the same as "stronger topology."

## 4. Effect of Noise

The AWGN plots show a gradual loss of structure as SNR decreases.

### 30 dB

At 30 dB, the noisy embedding remains very close to the clean case. The branch locations and symmetry are still visible, with only small local scatter around each clean point cluster.

Example:

- [30 dB, tau = 20](plots/Pulse_shaped_QPSK_AWGN_30DB%20delay%20embedding%20with%20tau%20%3D20.png)

### 20 dB

At 20 dB, the same structure is still visible, but the clusters are thicker. The signal geometry is still recoverable by eye.

### 10 dB

At 10 dB, noise becomes a major part of the embedding. A central noisy cloud appears, but the outer branch structure is still partly visible.

Example:

- [10 dB, tau = 20](plots/Pulse_shaped_QPSK_AWGN_10DB%20delay%20embedding%20with%20tau%20%3D20.png)

### 5 dB

At 5 dB, the embedding is strongly blurred. The original QPSK/pulse-shape structure is weak and only partially recognizable.

### 0 dB

At 0 dB, noise dominates. The points mostly form a broad random cloud, and the clean QPSK structure is largely lost.

Example:

- [0 dB, tau = 20](plots/Pulse_shaped_QPSK_AWGN_0DB%20delay%20embedding%20with%20tau%20%3D20.png)

## 5. Topological Persistence Result

The persistence plots compare maximum H1 persistence across tau values for 50, 100, and 200 symbols:

- [tau vs persistence, 50 symbols](plots/tau_vs_persistence_50.png)
- [tau vs persistence, 100 symbols](plots/tau_vs_persistence_100.png)
- [tau vs persistence, 200 symbols](plots/tau_vs_persistence_200.png)

The same pattern appears across all three symbol counts:

- `tau = 2` gives the largest maximum H1 persistence.
- `tau = 5` gives a moderate value.
- `tau = 15` and `tau = 25` give secondary peaks.
- `tau = 10`, `tau = 20`, and `tau = 30` give very low persistence.

This means the topology is sensitive to delay choice. The visually wider embeddings at larger tau do not automatically produce stronger H1 persistence. For this dataset, the most persistent loop-like feature appears at very small delay, with repeated secondary structure around `tau = 15` and `tau = 25`.

## 6. Strengths

- Delay embedding clearly exposes temporal structure created by pulse shaping.
- I and Q behave consistently, which supports the interpretation that the observed geometry comes from the QPSK waveform rather than a one-channel artifact.
- High-SNR cases preserve the clean geometry well, so the method is useful for visualizing signal structure under mild noise.
- The persistence plots are repeatable across 50, 100, and 200 symbols, suggesting the tau-dependent topological trend is not just a single-sample accident.
- The method gives both visual evidence and a quantitative topological summary through maximum H1 persistence.

## 7. Weaknesses

- The structure becomes unreliable at low SNR. Around 5 dB and especially 0 dB, the delay embedding is dominated by noise.
- The conclusion depends strongly on `tau`; choosing a visually spread embedding does not guarantee high persistence.
- The current pulse shaping uses a simple Gaussian filter, not a full communication-standard pulse such as root-raised cosine filtering.
- The plotted AWGN embeddings are subsampled to 200 points, so the visual density can change depending on the random subsample.
- Maximum H1 persistence alone is a limited metric. It reports the strongest loop-like feature but does not describe all geometry, cluster separation, or classification usefulness.
- The plots show projections of the complex 4D embedding into separate I and Q panels. Some structure may exist in the full 4D cloud that is not visible in either 2D projection.

## 8. Final Conclusion

The plots support this conclusion: delay embedding is effective for revealing the pulse-shape memory and structured geometry of QPSK at high SNR, but it is sensitive to delay selection and loses reliability as AWGN becomes strong.

For this experiment, the best topological signal according to maximum H1 persistence occurs at `tau = 2`, while `tau = 15` and `tau = 25` show secondary peaks. For visual inspection, `tau = 15` or `tau = 20` makes the branch structure easy to see, but for quantitative topology the persistence plots should guide the tau choice.
