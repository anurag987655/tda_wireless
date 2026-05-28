# Day 17 Thoery of Betti Numbers 

## Introduction 
Betti numbers is used to quantify the numbers of independent holes in topological space in every dimension.

## Betti 0 and Betti 1 : 
- Betti 0 counts the number of connected components. 
- Betti 1 counts the number of independent holes(loops).

## Question 1 : What would increase betti 0 ?
While analyzing the point cloud if we take the minimum threshold distance between two vertices $i$ and $j$ less we see more and more disconnected components which will ultimately increase the betti 0. So in general as  $\epsilon$ decreases the betti 0 increases in point cloud.

## Question 2 : What would increase betti 1 ?
As $\epsilon$ increases more components becomes connected, which ultimately leads to forming loops as a result betti 1 increases. Later when the void fills, upon further increasing $\epsilon$, the betti 1 decreases eventually.