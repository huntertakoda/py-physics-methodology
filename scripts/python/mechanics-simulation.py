import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the dataset

file_path = "C:/puredata/physics_methodology_dataset.csv"  # adjust this path if needed
data = pd.read_csv(file_path)

# preview the data

print(data.head())

# function to calculate maximum height

def calculate_max_height(velocity, angle, g):
    angle_rad = np.radians(angle)
    return (velocity ** 2 * np.sin(angle_rad) ** 2) / (2 * g)

# function to calculate range

def calculate_range(velocity, angle, g):
    angle_rad = np.radians(angle)
    return (velocity ** 2 * np.sin(2 * angle_rad)) / g

# function to calculate time of flight

def calculate_time_of_flight(velocity, angle, g):
    angle_rad = np.radians(angle)
    return (2 * velocity * np.sin(angle_rad)) / g

# apply mechanics calculations to dataset

data['max_height'] = data.apply(lambda row: calculate_max_height(row['initial_velocity'], row['angle_of_projection'], row['gravitational_acceleration']), axis=1)
data['projectile_range'] = data.apply(lambda row: calculate_range(row['initial_velocity'], row['angle_of_projection'], row['gravitational_acceleration']), axis=1)
data['calculated_time_of_flight'] = data.apply(lambda row: calculate_time_of_flight(row['initial_velocity'], row['angle_of_projection'], row['gravitational_acceleration']), axis=1)

# save the updated dataset for further analysis

output_path = "C:/puredata/mechanics_simulation_results.csv"
data.to_csv(output_path, index=False)

print(f"updated dataset saved to {output_path}")

# plot the relationship between initial velocity and projectile range

plt.figure(figsize=(10, 6))
plt.scatter(data['initial_velocity'], data['projectile_range'], c='blue', alpha=0.6, edgecolors='k')
plt.title('initial velocity vs. projectile range')
plt.xlabel('initial velocity (m/s)')
plt.ylabel('projectile range (m)')
plt.grid(True)
plt.show()

