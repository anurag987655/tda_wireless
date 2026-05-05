import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs('plots', exist_ok=True)

# -------------------------
# BPSK MODULATION
# -------------------------

# Input bits
bits = np.array([1, 0, 1, 1, 0])

# Bit mapping:
# 1 -> +1
# 0 -> -1
symbols = 2 * bits - 1

# Parameters
samples_per_bit = 100
fc = 5   # carrier frequency

# Total samples
N = len(bits) * samples_per_bit

# Global time axis
t = np.linspace(0, len(bits), N, endpoint=False)

# Repeat each symbol over one bit duration
symbol_stream = np.repeat(symbols, samples_per_bit)

# Continuous carrier
carrier = np.cos(2 * np.pi * fc * t)

# BPSK signal
bpsk_signal = symbol_stream * carrier

# -------------------------
# PLOTTING
# -------------------------

fig, ax = plt.subplots(4, 1, figsize=(10, 10))

# 1. Input bits
t_bits = np.arange(len(bits) + 1)
bits_plot = np.append(bits, bits[-1])

ax[0].step(t_bits, bits_plot, where='post')
ax[0].set_title("Input bits")
ax[0].set_xlim(0, len(bits))
ax[0].set_ylim(-0.5, 1.5)
ax[0].grid()

# 2. Carrier signal
ax[1].plot(t, carrier)
ax[1].set_title("Carrier signal")
ax[1].set_xlim(0, len(bits))
ax[1].grid()

# 3. BPSK signal
ax[2].plot(t, bpsk_signal)
ax[2].set_title("BPSK Signal")
ax[2].set_xlim(0, len(bits))
ax[2].grid()

# 4. Constellation diagram
I = symbols
Q = np.zeros(len(symbols))

# Ideal points
ax[3].scatter([-1, 1], [0, 0],
              s=150,
              color='lightgray',
              zorder=1)

# Actual transmitted symbols
ax[3].scatter(I, Q,
              s=100,
              color='blue',
              zorder=2)

# Labels
shown = set()

for i, bit in enumerate(bits):

    if bit not in shown:
        ax[3].text(
            I[i],
            Q[i] + 0.08,
            str(bit),
            fontsize=12
        )
        shown.add(bit)

ax[3].axhline(0, color='black', linewidth=0.8)
ax[3].axvline(0, color='black', linewidth=0.8)

ax[3].set_title("BPSK Constellation")
ax[3].set_xlim(-1.5, 1.5)
ax[3].set_ylim(-1.5, 1.5)

ax[3].set_xlabel("In-phase (I)")
ax[3].set_ylabel("Quadrature (Q)")

ax[3].grid()

plt.tight_layout()

plt.savefig("plots/bpsk_modulation_fixed.png")
plt.close()