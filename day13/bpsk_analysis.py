import numpy as np 
import matplotlib.pyplot as plt 
import os 

os.makedirs("plots",exist_ok=True)

#for experiment seeds
np.random.seed(42)

# Defining Delay embedding function: 

def delay_embedding_2d(signal,tau):
    return signal[:-tau],signal[tau:]

def delay_embedding_3d(signal,tau):
    return signal[:-2*tau],signal[tau:-tau],signal[2*tau:]

## Nearest Neighbour function 
def nearest_neighbour(x , y):
    points = np.column_stack((x,y))
    nearest_distance = []

    for i in range(len(points)):
        current_point = points[i]
        distances = []

        for j in range(len(points)):
            if i == j : 
                continue 

            other_points = points[j]
            distance = np.linalg.norm(current_point - other_points)

            distances.append(distance)
        nearest_distance.append(min(distances))

    return np.array(nearest_distance)

#Generating Bpsk signal
 
no_of_bits = 20
sample_per_bit = 100

## Generating bits 

bits = np.random.randint(0,2,no_of_bits)

## Bit mapping: 

symbol = 2 * bits -1

## Total sample 
N = no_of_bits * sample_per_bit

## Generating Carrier wave: 

t = np.linspace(0,no_of_bits,N,endpoint=False)

A = 1
fc = 5
phi = 0 


symbol_stream = np.repeat(symbol, sample_per_bit)

cosine_wave = A*np.cos(2* np.pi * fc * t + phi)


bpsk_signal = symbol_stream * cosine_wave

## Generating Noise: 

noise = np.random.normal(0,0.1,N)

## Generating reactive jammer

signal_detected = np.abs(bpsk_signal)>0.95
attack_now = np.random.rand(len(bpsk_signal))>0.7

trigger = signal_detected & attack_now

reactive_jammer = np.where(trigger, np.random.normal(0,0.5,len(bpsk_signal)),0)

## Bpsk + jammer behavior
jammed_bpsk = reactive_jammer + bpsk_signal

## delay embedding for each signal 

x_bpsk , y_bpsk = delay_embedding_2d(bpsk_signal,5)
x_nbpsk , y_nbpsk = delay_embedding_2d(jammed_bpsk ,5)

# Plotting the bpsk_signal : 

fig,ax = plt.subplots(2,1,figsize=(10,10))

ax[0].plot(t,bpsk_signal)
ax[0].set_title("Bpsk Signal")
ax[0].set_xlabel("Time(t)")
ax[0].set_ylabel("Amplitude")
ax[0].grid()

ax[1].scatter(x_bpsk,y_bpsk,s=10)
ax[1].set_title("Delay embedding of Bpsk signal")
ax[1].set_xlabel("x(t)")
ax[1].set_ylabel("x(t+tau)")
ax[1].grid()

plt.tight_layout()
plt.savefig("plots/bpsk_embedding_tau_5.png")
plt.close()

# plotting the behavior of bpsk_signal with jammer 

fig , ax = plt.subplots(2,1,figsize=(10,10))

ax[0].plot(t,jammed_bpsk)
ax[0].set_title("Bpsk Signal in presence of reactive jammer")
ax[0].set_xlabel("Time(t)")
ax[0].set_ylabel("Amplitude")
ax[0].grid()

ax[1].scatter(x_nbpsk,y_nbpsk,s=10)
ax[1].set_title("Delay embedding of Jammed Bpsk signal")
ax[1].set_xlabel("x(t)")
ax[1].set_ylabel("x(t+tau)")
ax[1].grid()

plt.tight_layout()
plt.savefig("plots/jammed_bpsk_embedding_tau_5.png")
plt.close()


print("Clean spread:", np.std(x_bpsk), np.std(y_bpsk))
print("Jammed spread:", np.std(x_nbpsk), np.std(y_nbpsk))

print("Average mean bpsk: ",np.mean(nearest_neighbour(x_bpsk,y_bpsk)))
print("Average mean of jammed bpsk", np.mean(nearest_neighbour(x_nbpsk,y_nbpsk)))