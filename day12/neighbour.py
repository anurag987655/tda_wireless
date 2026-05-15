# Todays objectives: 
# Generation of sine wave, noise signal, choas signal 
# a plot of delay embedding 
# nearest neighbour analysis with euclidean distance 


import numpy as np 
import matplotlib.pyplot as plt 
import os 

os.makedirs("plots",exist_ok=True)

def delay_embedding(signal,tau):
    x = signal[:-tau]
    y = signal[tau:]

    return x,y

## Function to find nearest neighbour: 

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

N = 200

t = np.linspace(0,1,200)

# Define sine wave : 

A = 1 
f = 5
phi = 0 

sine_wave = A * np.sin(2 * np.pi * f * t + phi)

# Define choas signal

x = 0.05
r = 3.9
choas=[]

for i in range(300):
    x = x*r*(1-x)
    choas.append(x)

choas = choas[100:] #Removing transient behavior

# Define noise signal:

noise = np.random.normal(0,0.02,N)


## Delay embedding for each signal 

x_sine,y_sine = delay_embedding(sine_wave,10)
x_noise,y_noise = delay_embedding(noise,1)
x_chaos,y_chaos = delay_embedding(choas,1)

## nearest neighbour distance 

dist_sine = nearest_neighbour(x_sine,y_sine)
dist_noise = nearest_neighbour(x_noise,y_noise)
dist_choas = nearest_neighbour(x_chaos,y_chaos)

## Visualization

# sine wave 

fig,ax = plt.subplots(3,1,figsize=(10,10))

ax[0].plot(t,sine_wave)
ax[0].set_title("Sine Wave")
ax[0].set_xlabel("Time")
ax[0].set_ylabel("Amplitude")
ax[0].grid()

ax[1].scatter(x_sine,y_sine,s=10)
ax[1].set_title("Delay embedding of sine wave")
ax[1].set_xlabel("x(t)")
ax[1].set_ylabel("x(t+tau), tau=20")
ax[1].grid()

ax[2].hist(dist_sine,bins=30)
ax[2].set_title("Nearest neighbour distances")
ax[2].set_xlabel("Distance")
ax[2].set_ylabel("Count")
ax[2].grid()

plt.tight_layout()
plt.savefig("plots/sine_wave_nearest_neighbour_in_embedding_space.png")
plt.close()

#choas wave 

fig,ax = plt.subplots(3,1,figsize=(10,10))

ax[0].plot(choas)
ax[0].set_title("Choas_signal")
ax[0].set_xlabel("Iteration")
ax[0].set_ylabel("Value")
ax[0].grid()

ax[1].scatter(x_chaos,y_chaos,s=10)
ax[1].set_title("Delay embedding of choas signal")
ax[1].set_xlabel("x(t)")
ax[1].set_ylabel("x(t+tau), tau=1")
ax[1].grid()

ax[2].hist(dist_choas,bins=30)
ax[2].set_title("Nearest neighbour distances")
ax[2].set_xlabel("Distance")
ax[2].set_ylabel("Count")
ax[2].grid()

plt.tight_layout()
plt.savefig("plots/choas_signal_nearest_neighbour_in_embedding_space.png")
plt.close()

# Noise wave


fig,ax = plt.subplots(3,1,figsize=(10,10))

ax[0].plot(noise)
ax[0].set_title("Noise Wave")
ax[0].set_xlabel("Time")
ax[0].set_ylabel("Value")
ax[0].grid()

ax[1].scatter(x_noise,y_noise,s=10)
ax[1].set_title("Delay embedding of noisy wave")
ax[1].set_xlabel("x(t)")
ax[1].set_ylabel("x(t+tau), tau=1")
ax[1].grid()

ax[2].hist(dist_noise,bins=30)
ax[2].set_title("Nearest neighbour distances")
ax[2].set_xlabel("Distance")
ax[2].set_ylabel("Count")
ax[2].grid()

plt.tight_layout()
plt.savefig("plots/Noise_signal_nearest_distance_in_embedding_space")
plt.close()

print("Sine:", np.mean(dist_sine), np.std(dist_sine))
print("Noise:", np.mean(dist_noise), np.std(dist_noise))
print("Chaos:", np.mean(dist_choas), np.std(dist_choas))