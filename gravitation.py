import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to compute the gravitational wave strain
def compute_gravitational_wave(mass1, mass2, distance, time):
    G = 6.67430e-11  # gravitational constant
    c = 299792458    # speed of light
    
    # Simplified formula for the purpose of visualization
    # Amplitude of gravitational wave strain
    A = (4 * G**2 * mass1 * mass2 / (c**4 * distance)) * np.sin(2 * np.pi * time)
    
    return A

# Get user input with validation
def get_input(prompt, min_val, max_val):
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a numeric value in scientific notation (e.g., 2e10).")

mass1 = get_input("Enter the mass of the first body (in kg, e.g., 2e30): ", 1e22, 1e35)
mass2 = get_input("Enter the mass of the second body (in kg, e.g., 2e30): ", 1e22, 1e35)
distance = get_input("Enter the distance between the bodies (in meters, e.g., 1e11): ", 1e6, 1e22)
duration = get_input("Enter the duration of the animation (in seconds): ", 1, 100)

# Time array
time = np.linspace(0, duration, 1000)

# Compute the gravitational wave strain over time
strain = compute_gravitational_wave(mass1, mass2, distance, time)

# Create the figure and axis for the animation
fig, ax = plt.subplots()
line, = ax.plot(time, strain)

# Set the limits for the axis
ax.set_xlim(0, duration)
ax.set_ylim(np.min(strain), np.max(strain))

# Function to update the animation
def update(frame):
    new_strain = compute_gravitational_wave(mass1, mass2, distance, time[:frame])
    line.set_ydata(new_strain)
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(time), blit=True, repeat=False)

# Show the animation
plt.xlabel('Time (s)')
plt.ylabel('Gravitational Wave Strain')
plt.title('Gravitational Wave Animation')
plt.show()
