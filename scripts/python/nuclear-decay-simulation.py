import numpy as np
import matplotlib.pyplot as plt

def simulate_radioactive_decay(initial_atoms, decay_constant, time_steps):
    atoms_remaining = initial_atoms
    decay_data = []
    for t in range(time_steps):
        decayed = np.random.binomial(atoms_remaining, decay_constant)
        atoms_remaining -= decayed
        decay_data.append(atoms_remaining)
    return decay_data

initial_atoms = 1000
decay_constant = 0.1
time_steps = 50

data = simulate_radioactive_decay(initial_atoms, decay_constant, time_steps)
plt.plot(data)
plt.title('Radioactive Decay Over Time')
plt.xlabel('Time Steps')
plt.ylabel('Remaining Atoms')
plt.grid()
plt.show()