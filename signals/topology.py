import numpy as np 
import gudhi
import matplotlib.pyplot as plt 

def delay_embedding(signal, tau = 5): 
    x = signal.x 
    return np.column_stack([x[:-tau],x[tau:]])

def persistence_diagram(signal,tau=5,max_edge_length=2.0,max_dimension=2):
    points = delay_embedding(signal,tau=tau)
    rips = gudhi.RipsComplex(points=points,max_edge_length=max_edge_length)
    simplex_tree = rips.create_simplex_tree(max_dimension = max_dimension)
    simplex_tree.compute_persistence()

    return simplex_tree.persistence()

def h1_features(diagram):
    h1=[]

    for dim,pair in diagram: 
        if dim == 1: 
            birth,death= pair

            if death != float("inf"):
                h1.append(death-birth)

    if len(h1) == 0:
        return {"num_loops":0,
                "largest_persistence":0}
    
    return {
        "num_loops":len(h1),
        "largest_persistence":max(h1)
    }

def plot_embedding(points,title):
    plt.figure(figsize=(10,10))
    plt.scatter(points[:,0],points[:,1])
    plt.xlabel('x(t)')
    plt.ylabel('x(t+τ)')
    plt.title(title)
    plt.show()
    plt.close()

def plot_persistence_diagram(persistence,title): 
    plt.figure(figsize=(10,10))
    gudhi.plot_persistence_diagram(persistence)
    plt.title(title)
    plt.show()
    plt.close()