import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the dataset

file_path = "C:/puredata/physics_methodology_dataset.csv"  # adjust this path if needed
data = pd.read_csv(file_path)

# preview the data

print(data.head())

# function to calculate work done

def calculate_work_done(pressure, volume_change):
    return pressure * volume_change

# function to calculate heat transfer using specific heat capacity

def calculate_heat_transfer(mass, specific_heat, temperature_change):
    return mass * specific_heat * temperature_change

# function to calculate efficiency of a heat engine

def calculate_efficiency(heat_input, work_output):
    return (work_output / heat_input) * 100

# add columns for thermodynamic calculations
# assuming placeholder values for specific_heat and temperature_change for now

data['work_done'] = data.apply(lambda row: calculate_work_done(row['gravitational_acceleration'], row['distance_covered']), axis=1)
data['heat_transfer'] = data.apply(lambda row: calculate_heat_transfer(row['mass'], 4.18, 10), axis=1)  # specific_heat = 4.18, temperature_change = 10
data['efficiency'] = data.apply(lambda row: calculate_efficiency(row['heat_transfer'], row['work_done']), axis=1)

# save the updated dataset

output_path = "C:/puredata/thermodynamics_analysis_results.csv"
data.to_csv(output_path, index=False)

print(f"updated dataset saved to {output_path}")

# plot work done vs. heat transfer

plt.figure(figsize=(10, 6))
plt.scatter(data['work_done'], data['heat_transfer'], c='red', alpha=0.6, edgecolors='k')
plt.title('work done vs. heat transfer')
plt.xlabel('work done (J)')
plt.ylabel('heat transfer (J)')
plt.grid(True)
plt.show()
