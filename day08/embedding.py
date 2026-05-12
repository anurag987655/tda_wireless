import numpy as np 
import matplotlib.pyplot as plt 
import os 

os.makedirs("plots",exist_ok=True)
np.random.seed(42)

## Todays objective : 
# plotting sine wave embedding 
# plotting noisy sine wave embedding 

N = 1000 
t= np.linspace(0,1,N)

# Generating sine wave 

A=1 
f=5
sine_wave = A*np.sin (2*np.pi*f*t)

# Generating noise 

noise = np.random.normal (0,0.2,N)

# Noisy signal 

noisy_signal = noise + sine_wave

## square wave 
square_wave = np.sign(np.sin(2*np.pi*f*t))


# Creating delay embedding function 

def delay_embedding(signal, tau=10): 
    x1= signal[:-tau]
    x2=signal[tau:]

    return x1,x2  # returns the pair lists (x(t),x(t+tau))


x_sine,y_sine=delay_embedding(sine_wave)
x_noisy,y_noisy= delay_embedding(noisy_signal)
x_square,y_square=delay_embedding(square_wave)


# Experiment 01 : plot sine wave embedding 

plt.figure(figsize=(6,6))

plt.scatter(x_sine,y_sine,s=0.5)
plt.title("Delay embedding of sine wave")
plt.xlabel("x(t)")
plt.ylabel("x(t+tau)")

plt.grid()
plt.savefig("plots/sine_embedding.png")
plt.close()

# Experiment 02 : plot noisy sine wave embedding 

plt.figure (figsize=(6,6))

plt.scatter(x_noisy,y_noisy,s=0.5)
plt.title("Delay embedding of noisy sine wave")

plt.xlabel("x(t)")
plt.ylabel("x(t+tau)")

plt.grid()
plt.savefig("plots/noisy_sine_embedding.png")
plt.close()

# seeing more 

plt.figure(figsize=(6,6))

plt.scatter(x_square,y_square,s=10)
plt.title("Delay embedding of square wave")

plt.xlabel("x(t)")
plt.ylabel("x(t+tau)")

plt.grid()
plt.savefig("plots/square_delay_embedding_2d.png")
plt.close()