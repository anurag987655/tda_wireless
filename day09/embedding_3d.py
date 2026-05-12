import numpy as np 
import matplotlib.pyplot as plt
import os 

os.makedirs("plots",exist_ok=True)
np.random.seed(42)

## Todays goal: 
# 3d embedding of sine wave 
# 3d embedding of noisy sine wave 

N = 1000 

t = np.linspace(0,1,N)

# Generating sine wave 

A = 1
f = 5

sine_wave = A * np.sin(2 * np.pi * f * t)

# Generating square wave

square_wave = np.sign(np.sin(2 * np.pi * f *t))

# Generating noise 

noise = np.random.normal(0,0.2,N)

noisy_wave = noise + sine_wave
noisy_square= noise + square_wave

# Generating 3d delay embedding function 

def delay_embedding(signal,tau=20):
    x=signal[:-2*tau]
    y=signal[tau:-tau]
    z=signal[2*tau:]

    return x,y,z


## Embedding the sine wave and noisy sine wave signal 

x_sine,y_sine,z_sine = delay_embedding(sine_wave)
x_noisy,y_noisy,z_noisy = delay_embedding(noisy_wave)
x_square,y_square,z_square=delay_embedding(square_wave)
x_sqnoisy,ysqnoisy,zsqnoisy= delay_embedding(noisy_square)

## Generating the plot

### Generating sine wave 3d embedding 

fig = plt.figure(figsize=(7,7))

ax1=fig.add_subplot(211)

ax1.plot(t,sine_wave)
ax1.set_title("Sine wave")
ax1.set_xlabel("Time")
ax1.set_ylabel("Amplitude")


ax2 = fig.add_subplot(212,projection='3d')

ax2.scatter(x_sine, y_sine, z_sine, s=5)


ax2.set_title("Delay embedding of sine wave in 3d")
ax2.set_xlabel("x(t)")
ax2.set_ylabel("x(t+tau)")
ax2.set_zlabel("x(t+2tau)")

plt.tight_layout()
plt.savefig("plots/3d_sine_delay_embedding.png")
plt.close()


### Generating noisy sine wave 3d embedding 

fig = plt.figure(figsize=(7,7))

ax1=fig.add_subplot(211)

ax1.plot(t,noisy_wave)
ax1.set_title("Noisy sine wave")
ax1.set_xlabel("Time")
ax2.set_ylabel("Amplitude")

ax2 = fig.add_subplot(212, projection='3d')

ax2.scatter(x_noisy,y_noisy,z_noisy)

ax2.set_title("Delay embedding of noisy sine wave in 3d")
ax2.set_xlabel("x(t)")
ax2.set_ylabel("x(t+tau)")
ax2.set_zlabel("x(t+2tau)")

plt.tight_layout()
plt.savefig("plots/3d_noisy_sine_embedding")
plt.close()

## Generating square wave in 3d embedding 

fig = plt.figure(figsize=(7,7))

ax1=fig.add_subplot(211)

ax1.plot(t,square_wave)
ax1.set_title("Square wave")
ax1.set_xlabel("Time")
ax1.set_ylabel("Amplitude")

ax2=fig.add_subplot(212,projection='3d')

ax2.scatter(x_square,y_square,z_square,s=5)
ax2.set_title("Delay embedding of square wave in 3d")
ax2.set_xlabel("x(t)")
ax2.set_ylabel("x(t+tau)")
ax2.set_zlabel("x(t+2tau)")

plt.tight_layout()
plt.savefig("plots/square_wave_embedding.png")
plt.close()

## Generating noisy square wave in 3d embedding 

fig = plt.figure(figsize=(7,7))

ax1= fig.add_subplot(211)
ax1.plot(t,noisy_square)
ax1.set_title("Noisy square wave")
ax1.set_xlabel("Time")
ax1.set_ylabel("Amplitude")

ax2=fig.add_subplot(212,projection='3d')
ax2.scatter(x_sqnoisy,ysqnoisy,zsqnoisy,s=5)
ax2.set_title("Delay embedding of noisy square wave in 3d")
ax2.set_xlabel("x(t)")
ax2.set_ylabel("x(t+tau)")
ax2.set_ylabel("x(t+2tau)")

plt.tight_layout()
plt.savefig("plots/3d_noisy_square_wave_embedding.png")
plt.close()