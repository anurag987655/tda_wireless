# Day-22 Observation : 
Today I made a clean circle by plotting the value of $(\cos(\theta), \sin(\theta))$ to check how the persistence diagram looks and afterward I added the noise which is generated randomly to see how the persistence diagram evolves when the noise is added. 

## Perfect Circle Result: 
- One $H_1$ feature loop borns at $b\approx 0.063$  and dies at $d\approx 1.732$ with a persistence $p \approx 1.67$

## Noisy Circle Result: 
- Multiple $H_1$ feature loop exists and the feature loop with highest persistence borns at $b\approx 0.252$  and dies at $d\approx 1.539$ with a persistence $p \approx 1.268$
- Other persistence loop quickly vanishes which are seen near diagonal line. 

## Indication: 
- Noise adds short lived $H_1$ features near the diagonal. So in a way persistence homology helps separate structure from noise.