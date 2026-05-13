import numpy as np 
import matplotlib.pyplot as plt 
import os 

os.makedirs("plots",exist_ok=True)

def delay_embedding(signal, tau = 1):

    x=signal[:-tau]
    y=signal[tau:]

    return x, y 

## Todays objective : 
# Generating chaos signal 

r=3.9
x=0.5

values = []

for _ in range(200):
    x = r *x * (1-x)
    values.append(x)

# plotting the behavior of $$x_{n+1}$$=$$r$$ * $$x_n$$ *(1-$$x_n$$)

plt.figure(figsize=(7,7))
plt.plot(values)
plt.title("Logistic Map Time Series")
plt.xlabel("Iteration")
plt.ylabel("x(n)")

plt.grid()
plt.savefig("plots/chaos_behavaior.png")
plt.close()

# Sensitive dependent experiment:

r=3.9

x1=0.5000
x2=0.5001

v1=[]
v2=[]

for _ in range(100):
    x1=r*x1*(1-x1)
    x2=r*x2*(1-x2)
    v1.append(x1)
    v2.append(x2)

plt.figure(figsize=(10,10))

plt.plot(v1)
plt.plot(v2)
plt.title("Analysis")
plt.xlabel("Iteration")
plt.ylabel("Value")


plt.savefig("plots/sensivity_dependent.png")
plt.close()

## Plotting the difference graph : 

diff = np.abs(np.array(v1)-np.array(v2))

plt.figure(figsize=(10,6))
plt.plot(diff)

plt.yscale("log")
plt.title("Growth of difference")
plt.xlabel("Iteration")
plt.ylabel("Difference |x1-x2|")

plt.grid()
plt.savefig("plots/difference_plt.png")
plt.close()


## Generate noise 

noise = np.random.rand(200)

x_chaos, y_chaos = delay_embedding(values)

x_noise , y_noise = delay_embedding(noise)

fig, ax = plt.subplots(4,1,figsize=(10,16))
plt.subplots_adjust(hspace=0.6)

ax[0].plot(values)
ax[0].set_title("1) Chaotic Signal (Logistic Map, r = 3.9)")
ax[0].set_xlabel("Iteration")
ax[0].set_ylabel("Value")
ax[0].grid(True)

# (2) Chaotic delay embedding
ax[1].scatter(x_chaos, y_chaos, s=10)
ax[1].set_title("2) Delay Embedding of Chaotic Signal (2D)")
ax[1].set_xlabel("x(n)")
ax[1].set_ylabel("x(n+1)")
ax[1].grid(True)

# (3) Random noise
ax[2].plot(noise)
ax[2].set_title("3) Random Noise")
ax[2].set_xlabel("Iteration")
ax[2].set_ylabel("Value")
ax[2].grid(True)

# (4) Noise delay embedding
ax[3].scatter(x_noise, y_noise, s=10)
ax[3].set_title("4) Delay Embedding of Random Noise (2D)")
ax[3].set_xlabel("x(n)")
ax[3].set_ylabel("x(n+1)")
ax[3].grid(True)

plt.tight_layout()
plt.savefig("plots/noisy_vs_chaos.png")