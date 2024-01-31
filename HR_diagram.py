import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
df = pd.read_csv('Cluster_data - Sheet1.csv')

# Extracting relevant columns
temperature = df['Temperature (K)']
luminosity = df['Luminosity(Solar)']

# reversing the temperature axis for HR diagrams
# temperature = temperature[::-1]

# Creating HR diagram
plt.figure(figsize=(10, 6))
plt.scatter(temperature, luminosity, c='seagreen', marker='o', s=10, label='Stars')

# Customizing plot
plt.title('Hertzsprung-Russell Diagram')
plt.xlabel('Temperature (K)')
plt.ylabel('Luminosity (Solar)')
plt.xscale('log')  # Temperature is plotted on a logarithmic scale
plt.yscale('log')  # Luminosity is plotted on a logarithmic scale
plt.gca().invert_xaxis()  # Reverse the temperature axis (optional)

# Add grid and legend
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()

# Show plot
plt.show()

