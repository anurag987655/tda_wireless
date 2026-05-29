# Persistent Homology: 

## Q1) Define filtration in your own words?
Filtration is a process of step by step construction of higher complexes where we start from simple objects(points) and gradually add higher dimensional simplices (edge,  traingle, etc) such that each stage contains all the previous structure. In more abstract terms 
$k_0 \subseteq k_1 \subseteq \dots \subseteq k_n$ which literally means each complex is obtained from previous one by adding simplices. Generally it is governed by rule in this case the distance. As distance parameter increases the structure grows from points to edges, loops, higher dimensional filled region while preserving the shape. 

## Q2) Why persistence matters?
Persistence keeps track of : 
- When topological features appear(birth)
- When it disappear(death)

More abstractly: 
$persistent=b-d$

In practical application say in signal analysis noises generally tend to produce features that appear and disappear quickly resulting in very low persistence. Whereas meaningful signal tend to have higher persistence. So it is tool for identifying underlying noise in communication channel. 