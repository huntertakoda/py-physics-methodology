import numpy as np
import matplotlib.pyplot as plt

# simulate the resistance of a material approaching absolute zero

def simulate_resistance(temperature, critical_temperature):
    return np.where(temperature < critical_temperature, 0, (temperature - critical_temperature)**2)

temperature = np.linspace(0, 300, 1000)  # temperatures in kelvin
critical_temperature = 90  # critical temperature for yttrium barium copper oxide in kelvin
resistance = simulate_resistance(temperature, critical_temperature)

plt.plot(temperature, resistance)
plt.title('resistance vs. temperature for a superconductor')
plt.xlabel('temperature (k)')
plt.ylabel('resistance (ohms)')
plt.grid()
plt.show()
