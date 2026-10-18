# **Monte Carlo Python Code**
## Computing Pi
* Code to compute the value of pi - uses the number of random points placed in a unit square that fall within
a quarter of a circle with radius equal to the length of the square 

## Ising model
* Code to track the energy states generated when simulating the 2D Ising model, details of which are below.

### Ising Model Hamiltonian:

```math
H = -\varepsilon \sum_{\langle i,j \rangle} S_i S_j - B \sum_{i} S_i
```
 
where:
 
* $`S_i = \pm \frac{1}{2}`$ is the spin at site $`i`$
* $`\varepsilon`$ is the coupling constant between neighbouring spins
* $`B`$ is the external magnetic field
* $`\langle i,j \rangle`$ denotes a sum over nearest-neighbour pairs, each pair counted once

### Energy change from a single spin flip:
 
Flipping spin $`S_k \to -S_k`$ changes the energy by
 
```math
\Delta E = 2 S_k \left( \varepsilon \sum_{j \in \mathrm{nn}(k)} S_j + B \right)
```
 
### Metropolis acceptance probability of the ergodic perturbation (single spin flip):
 
```math
P_{\mathrm{accept}} = \min\left(1, e^{-\Delta E / T}\right)
```
Equivalently,

```math
P_{\mathrm{accept}} = \begin{cases}
  1, & \text{if } \Delta E \le 0 \\
  e^{-\Delta E / T}, & \text{if } \Delta E > 0
\end{cases}
```
