# Todays objective 
# compare differnet orbit for different value of r in  both space.
# value of r = 2.5(stable orbit) 3.5(periodic orbit) 3.9(chaos orbit)


import matplotlib.pyplot as plt 
import numpy as np 
import os 

os.makedirs("plots",exist_ok=True)

def delay_embedding(signal, tau = 1):

    x=signal[:-tau]
    y=signal[tau:]

    return x, y 


# initialize the value 

r1 = 2.5
r2 = 3.5
r3 = 3.9

# initial value 
x1 = 0.5
x2 = 0.5
x3 = 0.5 

v1 = []
v2 = []
v3 = []

for i in range(200):
    x1= x1 *r1 * (1-x1)
    x2= x2 *r2 * (1-x2)
    x3= x3 *r3 * (1-x3)
    v1.append(x1)
    v2.append(x2)
    v3.append(x3)

# Generating delay embedding points 
xa , ya =delay_embedding(v1)
xb , yb = delay_embedding(v2)
xc , yc = delay_embedding(v3)


# Plotting the r1 = 2.5 i.e. stable orbit 

fig,ax = plt.subplots(2,1,figsize=(10,10))

ax[0].plot(v1)
ax[0].set_title("Stable orbit for (r=2.5)")
ax[0].set_xlabel("Iteration")
ax[0].set_ylabel("Value")
ax[0].grid()

ax[1].scatter(xa,ya,s=10)
ax[1].set_title("Delay embedding of stable orbit")
ax[1].set_xlabel("x(n)")
ax[1].set_ylabel("x(n+1)")
ax[1].grid()

plt.tight_layout()
plt.savefig("plots/stable_orbit.png")
plt.close()

# Plotting the r2 = 3.5 i.e. periodic orbit 

fig,ax = plt.subplots(2,1,figsize=(10,10))

ax[0].plot(v2)
ax[0].set_title("Stable orbit for (r=2.5)")
ax[0].set_xlabel("Iteration")
ax[0].set_ylabel("Value")
ax[0].grid()

ax[1].scatter(xb,yb,s=10)
ax[1].set_title("Delay embedding of periodic orbit")
ax[1].set_xlabel("x(n)")
ax[1].set_ylabel("x(n+1)")
ax[1].grid()

plt.tight_layout()
plt.savefig("plots/periodic_orbit.png")
plt.close()

# Plotting r3 = 3.9 i.e choas orbit

fig, ax = plt.subplots(2,1,figsize=(10,10))

ax[0].plot(v3)
ax[0].set_title("Choas orbit for (r=3.5)")
ax[0].set_xlabel("Iteration")
ax[0].set_ylabel("Values")
ax[0].grid()

ax[1].scatter(xc,yc,s=10)
ax[1].set_title("Delay embedding of choas orbit")
ax[1].set_xlabel("x(n)")
ax[1].set_ylabel("x(n+1)")
ax[1].grid()

plt.tight_layout()
plt.savefig("plots/choas_orbit.png")
plt.close()

# plot after removing transient for all three plot 

xat , yat = delay_embedding(v1[100:])
xbt , ybt = delay_embedding(v2[100:])
xct , yct = delay_embedding(v3[100:])

fig,ax = plt.subplots(3,1,figsize=(10,10))

ax[0].scatter(xat,yat,s=10)
ax[0].set_title("stable orbit after removing transient part")
ax[0].set_xlabel("x(n)")
ax[0].set_ylabel("x(n+1)")
ax[0].grid()

ax[1].scatter(xbt,ybt,s=10)
ax[1].set_title("periodic orbit after removing transient part")
ax[1].set_xlabel("x(n)")
ax[1].set_ylabel("x(n+1)")
ax[1].grid()

ax[2].scatter(xct,yct,s=10)
ax[2].set_title("choas orbit after removing transient part")
ax[2].set_xlabel("x(n)")
ax[2].set_ylabel("x(n+1)")
ax[2].grid()

plt.tight_layout()
plt.savefig("plots/delay_embedding_removing_transient.png")
plt.close()

# Noise 

noise = np.random.normal(0,0.02,200)

v3 = np.array(v3)
noisy_choas= noise + v3

# Delay embedding of noise: 

xn,yn = delay_embedding(noise)
xnc,ync=delay_embedding(noisy_choas)

#plotting the figure 

fig,ax = plt.subplots(4,1,figsize = (10,16))

ax[0].plot(noise)
ax[0].set_title("Noisy Signal")
ax[0].set_xlabel("Iteration")
ax[0].set_ylabel("Value")
ax[0].grid()

ax[1].plot(noisy_choas)
ax[1].set_title("Noisy + Choas Siagnal")
ax[1].set_xlabel("Iteration")
ax[1].set_ylabel("Value")
ax[1].grid()

ax[2].scatter(xn,yn,s=10)
ax[2].set_title("Delay embedding of noisy singal")
ax[2].set_xlabel("x(n)")
ax[2].set_ylabel("x(n+1)")
ax[2].grid()

ax[3].scatter(xnc,ync,s=10)
ax[3].set_title("Delay embedding of choas noisy singal")
ax[3].set_xlabel("x(n)")
ax[3].set_ylabel("x(n+1)")
ax[3].grid()

plt.tight_layout()
plt.savefig("plots/Noise_Choas_signal.png")
plt.close()