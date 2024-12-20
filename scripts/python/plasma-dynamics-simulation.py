import matplotlib.pyplot as plt
import numpy as np

# simulate electron motion in a magnetic field

def simulate_electron_motion(charges, masses, velocities, magnetic_field, time_steps):
    positions = []
    for charge, mass, velocity in zip(charges, masses, velocities):
        position = [0]
        for t in range(time_steps):
            acceleration = (charge * magnetic_field) / mass
            velocity += acceleration
            position.append(position[-1] + velocity)
        positions.append(position)
    return positions

charges = np.random.uniform(-1.6e-19, 1.6e-19, 10)
masses = np.random.uniform(9.1e-31, 1.0e-30, 10)
velocities = np.random.uniform(1e5, 1e6, 10)
magnetic_field = 0.01
time_steps = 100

positions = simulate_electron_motion(charges, masses, velocities, magnetic_field, time_steps)
for pos in positions:
    plt.plot(pos)
plt.title('electron motion in a magnetic field')
plt.xlabel('time steps')
plt.ylabel('position (m)')
plt.grid()
plt.show()