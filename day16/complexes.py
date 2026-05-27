import matplotlib.pyplot as plt 
import numpy as np 

from itertools import combinations 
from matplotlib.widgets import Slider

np.random.seed(42)

N = 30


theta = np.linspace(0,2*np.pi,N)

noise = np.random.randn(N)

x = np.cos(theta) + noise
y = np.sin(theta) + noise 


fig, ax = plt.subplots(figsize=(7,7))
plt.subplots_adjust(0.2)

epsilon_not = 0.35

def draw_complex(epsilon):

    ax.clear()

    # Draw points
    ax.scatter(x, y)


    for i in range(N):
        for j in range(i+1, N):

            distance = np.sqrt(
                (x[i]-x[j])**2 +
                (y[i]-y[j])**2
            )

            if distance < epsilon:

                ax.plot(
                    [x[i], x[j]],
                    [y[i], y[j]]
                )



    for i, j, k in combinations(range(N), 3):

        dij = np.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
        dik = np.sqrt((x[i]-x[k])**2 + (y[i]-y[k])**2)
        djk = np.sqrt((x[j]-x[k])**2 + (y[j]-y[k])**2)

        if dij < epsilon and dik < epsilon and djk < epsilon:

            ax.fill(
                [x[i], x[j], x[k]],
                [y[i], y[j], y[k]],
                alpha=0.3
            )

    ax.set_title(f"Simplicial Complex (ε = {epsilon:.2f})")

    ax.axis('equal')

draw_complex(epsilon_not)

slider_ax = plt.axes([0.2, 0.05, 0.6, 0.03])

epsilon_slider = Slider(
    slider_ax,
    'ε',
    0.05,
    1.0,
    valinit=epsilon_not
)

def update(val):

    epsilon = epsilon_slider.val

    draw_complex(epsilon)

    fig.canvas.draw_idle()

epsilon_slider.on_changed(update)



plt.show()