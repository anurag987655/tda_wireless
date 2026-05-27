# Day 16 Observation

- Today I generated a point cloud for a noisy circle, and then I computed pairwise distances. For every distance between two vertices, say $i$ and $j$, if the value $d_{ij} < \epsilon$, I connected those two points. Later, I extended this concept to the triangle for filling in the hole. I made an interactive slider so that for every $\epsilon$ change from 0.35 to 1, I observed how the holes were filled.
