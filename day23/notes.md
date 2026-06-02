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