'''pseudocode:
    1. define variables/parameters e.g. epsilon, B, temp, grid size
    2. initialise grid of points with +/- 1/2 spin
    3. define hamiltonian for the system
    4. propose ergodic perturbation (single spin flip)
    5. compute change in energy of proposed state
    6. reject or accept perturbation based on Metropolis algorithm
    7. keep track of all spin states after each choice or after inteval of choices
    8. present as simultation?
    9. plot energy of states as histogram?

'''
import numpy as np
import matplotlib.pyplot as plt

T = 1.0
B = 1.0
epsilon = 1.0
L = 10
num_perturb = 100000

spins = np.random.choice([0.5, -0.5], size=(L, L))

def hamiltonian_term1(spins):
    energy = 0
    for i in range(L):
        for j in range(L):
            S = spins[i, j]
            nn = spins[(i+1)%L, j] + spins[i, (j+1)%L] + spins[(i-1)%L, j] + spins[i, (j-1)%L]
            energy += -nn * S *epsilon
    return energy / 2

def hamiltonian_term2(spins):
    energy = - np.sum(spins * B)
    return energy

def energy_difference(spins, i, j):
    S = spins[i, j]
    nn = spins[(i+1)%L, j] + spins[i, (j+1)%L] + spins[(i-1)%L, j] + spins[i, (j-1)%L]
    dE = 2 * (nn * S *epsilon + B * S)
    return dE

starting_energy = hamiltonian_term1(spins) + hamiltonian_term2(spins)
energies = np.zeros(num_perturb + 1)
energies[0] = starting_energy

for n in range(num_perturb):
    i, j = np.random.randint(0, L, 2)
    dE = energy_difference(spins, i, j)
    k = 0
    if dE < 0:
        spins[i, j] *= -1
        k = 1
    else:
        if np.random.rand() < np.exp(-dE / T):
            spins[i, j] *= -1
            k = 1

    if k == 1:
        energies[n+1] = energies[n] + dE
    else:
        energies[n+1] = energies[n]

perturbs = np.arange(num_perturb + 1)
plt.plot(perturbs, energies)

plt.figure(figsize=(8, 6), dpi = 120)
plt.hist(energies, bins=100)
plt.xlabel('Energy')
plt.ylabel('Frequency')
plt.title('Distribution of Energy States')
plt.show()




