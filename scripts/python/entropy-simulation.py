import numpy as np
import matplotlib.pyplot as plt

# simulate entropy change in a system undergoing heat transfer

def simulate_entropy_change(heat_transferred, temperature):
    return heat_transferred / temperature

heat_transferred = np.linspace(-5000, 5000, 1000)  # heat transfer in joules
temperature = 300  # constant temperature in kelvin
entropy_change = simulate_entropy_change(heat_transferred, temperature)

plt.plot(heat_transferred, entropy_change)
plt.title('entropy change vs. heat transferred')
plt.xlabel('heat transferred (j)')
plt.ylabel('entropy change (j/k)')
plt.grid()
plt.show()
