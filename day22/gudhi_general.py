import numpy as np 
import matplotlib.pyplot as plt 
import gudhi 
import os 

np.random.seed(42)

os.makedirs("plots",exist_ok=True)

N = 100 

def compute_persistence(points,title):
    rips = gudhi.RipsComplex(points=points) # ASsigning points to create a simplex using vistor ripsl
    simplex_tree = rips.create_simplex_tree(max_dimension=2)

    #Printing the number of simplices;
    print(title)
    print("Number of simplices",simplex_tree.num_simplices())

    # computing persistence : 

    persistence = simplex_tree.persistence()

    print("Persistence pairs:")

    for pair in persistence: 
        print(pair)

    gudhi.plot_persistence_diagram(persistence)
    plt.title(title)
    plt.savefig(f'plots/persistence_{title}.png')



theta = np.linspace(0,2 *np.pi , N)

circle = np.column_stack([np.cos(theta),np.sin(theta)])  


plt.figure(figsize=(10,10))
plt.scatter(circle[:,0],circle[:,1])
plt.axis('equal')
plt.title("Perfect Circle")
plt.grid()
plt.savefig("plots/Perfect_cicle.png")

compute_persistence(circle,"perfect Circle")

## Generating noisy circle points

noise_strength= 0.08

noisy_cicle= np.column_stack([np.cos(theta) + noise_strength *np.random.randn(N),np.sin(theta) + noise_strength * np.random.randn(N)])

plt.figure(figsize=(10,10))
plt.scatter(noisy_cicle[:,0], noisy_cicle[:,1])
plt.axis('equal')
plt.title('Noisy Circle(Imperfect)')

plt.grid()
plt.savefig("plots/noisy_cicle.png")

compute_persistence(noisy_cicle,"Noisy Circle")