import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the dataset

file_path = "C:/puredata/physics_methodology_dataset.csv"  # adjust this path if needed
data = pd.read_csv(file_path)

# preview the data

print(data.head())

# function to calculate electric field strength

def calculate_electric_field(charge, distance):
    k = 8.9875517923e9  # coulomb's constant in N·m²/C²
    return k * charge / (distance ** 2)

# function to calculate magnetic force

def calculate_magnetic_force(charge, velocity, magnetic_field):
    return charge * velocity * magnetic_field

# function to calculate potential energy in an electric field

def calculate_potential_energy(charge, electric_field, distance):
    return charge * electric_field * distance

# add columns for electromagnetism calculations
# assuming placeholder values for charge, distance, velocity, and magnetic_field

data['electric_field'] = data.apply(lambda row: calculate_electric_field(1e-6, row['distance_covered']), axis=1)  # charge = 1 microcoulomb
data['magnetic_force'] = data.apply(lambda row: calculate_magnetic_force(1e-6, row['initial_velocity'], 0.01), axis=1)  # magnetic_field = 0.01 T
data['potential_energy'] = data.apply(lambda row: calculate_potential_energy(1e-6, row['electric_field'], row['distance_covered']), axis=1)

# save the updated dataset

output_path = "C:/puredata/electromagnetism_simulation_results.csv"
data.to_csv(output_path, index=False)

print(f"updated dataset saved to {output_path}")

# plot electric field strength vs. distance covered

plt.figure(figsize=(10, 6))
plt.scatter(data['distance_covered'], data['electric_field'], c='green', alpha=0.6, edgecolors='k')
plt.title('distance covered vs. electric field strength')
plt.xlabel('distance covered (m)')
plt.ylabel('electric field strength (N/C)')
plt.grid(True)
plt.show()