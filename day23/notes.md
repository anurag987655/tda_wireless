# Day 23: Topological Data Analysis of Signal Delay Embeddings

Today I observed the delay embedding and persistence diagram of three signals: a Sine Wave, Square wave and finally a BPSK diagram. 
---

## 1. Mathematical Background

### Delay Coordinate Embedding
For a discrete-time signal $x(t)$, a delay embedding with delay parameter $\tau$ maps the 1D signal into a sequence of 2D points:
$$(x(t),x(t - \tau))$$

According to **Takens' Embedding Theorem**, if the delay and dimension are chosen correctly, the reconstructed phase space is topologically equivalent to the original state space.

### Persistence  Homology: 
using the points cloud obtained from embedding, we  construct the **Vietoris-Rips complex** by expanding radius around each point. In the process we track topological features: 
**$H_0$** : connected components
**$H_1$** : one dimensional loops/holes 

## Diagram for different tau in embedding space for a clean sine wave, a square wave and finally bpsk signal

#### Sine Wave
| tau = 5 | tau = 10 | tau = 15 | tau = 20 | tau = 25 |
|:---:|:---:|:---:|:---:|:---:|
| <img src="plots/Delay_embedding_Sine Wave_5.png" width="150"> | <img src="plots/Delay_embedding_Sine Wave_10.png" width="150"> | <img src="plots/Delay_embedding_Sine Wave_15.png" width="150"> | <img src="plots/Delay_embedding_Sine Wave_20.png" width="150"> | <img src="plots/Delay_embedding_Sine Wave_25.png" width="150"> |
| <img src="plots/Persistence of Sine Wave tau=5_persistence_diagram.png" width="150"> | <img src="plots/Persistence of Sine Wave tau=10_persistence_diagram.png" width="150"> | <img src="plots/Persistence of Sine Wave tau=15_persistence_diagram.png" width="150"> | <img src="plots/Persistence of Sine Wave tau=20_persistence_diagram.png" width="150"> | <img src="plots/Persistence of Sine Wave tau=25_persistence_diagram.png" width="150"> |

#### Square Wave
| tau = 5 | tau = 10 | tau = 15 | tau = 20 | tau = 25 |
|:---:|:---:|:---:|:---:|:---:|
| <img src="plots/Delay_embedding_Square Wave_5.png" width="150"> | <img src="plots/Delay_embedding_Square Wave_10.png" width="150"> | <img src="plots/Delay_embedding_Square Wave_15.png" width="150"> | <img src="plots/Delay_embedding_Square Wave_20.png" width="150"> | <img src="plots/Delay_embedding_Square Wave_25.png" width="150"> |
| <img src="plots/Persistence of Square Wave tau=5_persistence_diagram.png" width="150"> | <img src="plots/Persistence of Square Wave tau=10_persistence_diagram.png" width="150"> | <img src="plots/Persistence of Square Wave tau=15_persistence_diagram.png" width="150"> | <img src="plots/Persistence of Square Wave tau=20_persistence_diagram.png" width="150"> | <img src="plots/Persistence of Square Wave tau=25_persistence_diagram.png" width="150"> |

#### BPSK Signal
| tau = 5 | tau = 10 | tau = 15 | tau = 20 | tau = 25 |
|:---:|:---:|:---:|:---:|:---:|
| <img src="plots/Delay_embedding_BPSK Signal_5.png" width="150"> | <img src="plots/Delay_embedding_BPSK Signal_10.png" width="150"> | <img src="plots/Delay_embedding_BPSK Signal_15.png" width="150"> | <img src="plots/Delay_embedding_BPSK Signal_20.png" width="150"> | <img src="plots/Delay_embedding_BPSK Signal_25.png" width="150"> |
| <img src="plots/Persistence of BPSK Signal tau=5_persistence_diagram.png" width="150"> | <img src="plots/Persistence of BPSK Signal tau=10_persistence_diagram.png" width="150"> | <img src="plots/Persistence of BPSK Signal tau=15_persistence_diagram.png" width="150"> | <img src="plots/Persistence of BPSK Signal tau=20_persistence_diagram.png" width="150"> | <img src="plots/Persistence of BPSK Signal tau=25_persistence_diagram.png" width="150"> |

## Quantitative Analysis: 

#### Sine Wave
| τ | Number of H₁ Features | Strongest Persistence |
|---|----------------------|----------------------|
| 5  | 1   | 1.0055 |
| 10 | 1   | 1.6725 |
| 15 | 3   | 0.9947 |
| 20 | 95  | 0.0053 |
| 25 | 4   | 1.0267 |
#### Square Wave
| τ | Number of H₁ Features | Strongest Persistence |
|---|----------------------|----------------------|
| 5  | 1 | 0.2361 |
| 10 | 1 | 0.2361 |
| 15 | 1 | 0.2361 |
| 20 | 0 | 0.0000 |
| 25 | 1 | 0.2361 |
#### BPSK Signal
| τ | Number of H₁ Features | Strongest Persistence |
|---|----------------------|----------------------|
| 5  | 19 | 1.4691 |
| 10 | 54 | ~0.0000 |
| 15 | 20 | 1.4691 |
| 20 | 34 | ~0.0000 |
| 25 | 8  | 1.4691 |