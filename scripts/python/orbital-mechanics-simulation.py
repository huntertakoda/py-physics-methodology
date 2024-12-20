import matplotlib.pyplot as plt
import numpy as np

def simulate_orbit(mass_central, initial_radius, initial_velocity, time_steps):
    G = 6.67430e-11
    positions = []
    velocity = np.array([0, initial_velocity])
    position = np.array([initial_radius, 0])
    for t in range(time_steps):
        force = -G * mass_central / np.linalg.norm(position)**2
        acceleration = force * position / np.linalg.norm(position)
        velocity += acceleration
        position += velocity
        positions.append(position.copy())
    return np.array(positions)

mass_central = 5.972e24  # earth's mass in kg
initial_radius = 7e6  # 7000 km from center
initial_velocity = 7.12e3  # circular orbit velocity in m/s
time_steps = 1000

positions = simulate_orbit(mass_central, initial_radius, initial_velocity, time_steps)
plt.plot(positions[:, 0], positions[:, 1])
plt.title('orbital mechanics simulation')
plt.xlabel('x position (m)')
plt.ylabel('y position (m)')
plt.grid()
plt.axis('equal')
plt.show()