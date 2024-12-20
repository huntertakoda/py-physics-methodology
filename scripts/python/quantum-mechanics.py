import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the dataset

file_path = "C:/puredata/physics_methodology_dataset.csv"  # adjust this path if needed
data = pd.read_csv(file_path)

# preview the data

print(data.head())

# function to calculate energy of a photon

def calculate_photon_energy(frequency):
    h = 6.62607015e-34  # planck's constant in J·s
    return h * frequency

# function to calculate de broglie wavelength

def calculate_de_broglie_wavelength(mass, velocity):
    h = 6.62607015e-34  # planck's constant in J·s
    return h / (mass * velocity)

# function to calculate uncertainty in position using heisenberg's principle

def calculate_uncertainty_in_position(mass, velocity_uncertainty):
    h = 6.62607015e-34  # planck's constant in J·s
    return h / (4 * np.pi * mass * velocity_uncertainty)

# add columns for quantum mechanics calculations
# assuming placeholder values for frequency, velocity_uncertainty

data['photon_energy'] = data.apply(lambda row: calculate_photon_energy(1e14), axis=1)  # frequency = 1e14 Hz
data['de_broglie_wavelength'] = data.apply(lambda row: calculate_de_broglie_wavelength(row['mass'], row['initial_velocity']), axis=1)
data['position_uncertainty'] = data.apply(lambda row: calculate_uncertainty_in_position(row['mass'], 0.01), axis=1)  # velocity_uncertainty = 0.01 m/s

# save the updated dataset

output_path = "C:/puredata/quantum_mechanics_results.csv"
data.to_csv(output_path, index=False)

print(f"updated dataset saved to {output_path}")

# plot de broglie wavelength vs. mass

plt.figure(figsize=(10, 6))
plt.scatter(data['mass'], data['de_broglie_wavelength'], c='purple', alpha=0.6, edgecolors='k')
plt.title('mass vs. de broglie wavelength')
plt.xlabel('mass (kg)')
plt.ylabel('de broglie wavelength (m)')
plt.grid(True)
plt.show()