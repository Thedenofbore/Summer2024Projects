import numpy as np
from scipy.integrate import solve_ivp
import pandas as pd

# Gravitational constant and mass of the Sun
G = 6.67430e-11
M = 1.989e30
mu = G * M
alpha = 1.1e-8  # Example relativistic correction factor

# Planetary initial conditions [x0, y0, vx0, vy0] (placeholders)
planets = {
    'Mercury': [5.79e10, 0, 0, 4.79e4],
    'Venus': [1.082e11, 0, 0, 3.50e4],
    'Earth': [1.4710e11, 0, 0, 3.0287e4],
    'Mars': [2.279e11, 0, 0, 2.41e4],
    'Jupiter': [7.785e11, 0, 0, 1.307e4],
    'Saturn': [1.4335e12, 0, 0, 9.69e3],
    'Uranus': [2.8725e12, 0, 0, 6.81e3],
    'Neptune': [4.4951e12, 0, 0, 5.43e3],
    'Pluto': [5.9064e12, 0, 0, 4.74e3]  # Not a planet, but often included for completeness
}


def relativistic_orbit(t, y, mu, alpha):
    r = np.sqrt(y[0]**2 + y[1]**2)
    r3 = r**3
    ax = -mu * y[0] / r3 * (1 + alpha / r**2)
    ay = -mu * y[1] / r3 * (1 + alpha / r**2)
    return [y[2], y[3], ax, ay]

def simulate_orbit(planet, initial_conditions):
    t_span = (0, 3.154e7)  # One year in seconds
    t_eval = np.linspace(t_span[0], t_span[1], 1000)
    solution = solve_ivp(relativistic_orbit, t_span, initial_conditions, args=(mu, alpha), t_eval=t_eval, rtol=1e-6)
    return solution.t, solution.y

def save_data():
    for planet, initial_conditions in planets.items():
        times, data = simulate_orbit(planet, initial_conditions)
        df = pd.DataFrame(data.T, columns=['x', 'y', 'vx', 'vy'])
        df['time'] = times
        df = df[['time', 'x', 'y', 'vx', 'vy']]
        df.to_csv(f'{planet}_motion.csv', index=False)
        print(f"Data saved for {planet} to '{planet}_motion.csv'.")

save_data()
