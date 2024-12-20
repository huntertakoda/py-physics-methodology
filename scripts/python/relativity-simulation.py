import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the dataset

file_path = "C:/puredata/physics_methodology_dataset.csv"  # adjust this path if needed
data = pd.read_csv(file_path)

# preview the data

print(data.head())

# function to calculate time dilation

def calculate_time_dilation(proper_time, velocity, speed_of_light):
    return proper_time / np.sqrt(1 - (velocity ** 2 / speed_of_light ** 2))

# function to calculate relativistic energy

def calculate_relativistic_energy(mass, velocity, speed_of_light):
    gamma = 1 / np.sqrt(1 - (velocity ** 2 / speed_of_light ** 2))
    return mass * speed_of_light ** 2 * gamma

# function to calculate length contraction

def calculate_length_contraction(proper_length, velocity, speed_of_light):
    return proper_length * np.sqrt(1 - (velocity ** 2 / speed_of_light ** 2))

# add columns for relativity calculations
# assuming placeholder values for proper_time and proper_length

data['time_dilation'] = data.apply(lambda row: calculate_time_dilation(1, row['initial_velocity'], 3e8), axis=1)  # proper_time = 1 s, speed_of_light = 3e8 m/s
data['relativistic_energy'] = data.apply(lambda row: calculate_relativistic_energy(row['mass'], row['initial_velocity'], 3e8), axis=1)
data['length_contraction'] = data.apply(lambda row: calculate_length_contraction(1, row['initial_velocity'], 3e8), axis=1)  # proper_length = 1 m

# save the updated dataset

output_path = "C:/puredata/relativity_simulation_results.csv"
data.to_csv(output_path, index=False)

print(f"updated dataset saved to {output_path}")

# plot relativistic energy vs. velocity

plt.figure(figsize=(10, 6))
plt.scatter(data['initial_velocity'], data['relativistic_energy'], c='orange', alpha=0.6, edgecolors='k')
plt.title('velocity vs. relativistic energy')
plt.xlabel('velocity (m/s)')
plt.ylabel('relativistic energy (J)')
plt.grid(True)
plt.show()
