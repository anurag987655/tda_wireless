# Today's Objective:
Today I looked at the bpsk signal its behavior in embedded space and also analyzed how it is spread in this space and average mean with nearest neighbour then i did same for the jammed bpsk signal to see how they would deviate

# Observation: 

Clean Bpsk : 
- Delay embedding formed repeated structured phase point and for tau=5 it formed a circular.
[Delay embedding of bpsk for tau=5](plots/bpsk_embedding_tau_5.png)
- Point cloud spread:
  - x = 0.707
  - y = 0.707
- Mean nearest-neighbor distance ≈ 0

Jammed Bpsk : 
- Point cloud became wider and fuzzier.
[Delay embeddinf of jammed bpsk for tau = 5](plots/jammed_bpsk_embedding_tau_5.png)
- Point cloud spread:
  - x = 0.722
  - y = 0.723
- Mean nearest-neighbor distance ≈ 0.006
