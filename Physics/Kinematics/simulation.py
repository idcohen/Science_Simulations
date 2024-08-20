import math
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

def simulate_projectile_motion(v0, angle, g=9.81, dt=0.01):
    # Convert angle to radians
    angle_rad = math.radians(angle)
    
    # Initial velocity components
    v0x = v0 * math.cos(angle_rad)
    v0y = v0 * math.sin(angle_rad)
    
    # Initial positions
    x = 0
    y = 0
    
    # Lists to store trajectory data
    x_vals = []
    y_vals = []
    
    # Time variable
    t = 0
    
    while y >= 0:
        # Append current position to lists
        x_vals.append(x)
        y_vals.append(y)
        
        # Update time
        t += dt
        
        # Update positions
        x = v0x * t
        y = v0y * t - 0.5 * g * t**2
        
    return x_vals, y_vals

def plot_trajectory(x_vals, y_vals):
    plt.plot(x_vals, y_vals)
    plt.title("Projectile Motion")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid(True)
    plt.show()

def run_simulation():
    try:
        v0 = float(velocity_entry.get())
        angle = float(angle_entry.get())
        x_vals, y_vals = simulate_projectile_motion(v0, angle)
        plot_trajectory(x_vals, y_vals)
    except ValueError:
        result_label.config(text="Please enter valid numbers.", fg="red")

# Create the main window
root = tk.Tk()
root.title("Projectile Motion Simulator")

# Create and place the velocity label and entry
velocity_label = ttk.Label(root, text="Initial Velocity (m/s):")
velocity_label.grid(column=0, row=0, padx=10, pady=10)
velocity_entry = ttk.Entry(root)
velocity_entry.grid(column=1, row=0, padx=10, pady=10)

# Create and place the angle label and entry
angle_label = ttk.Label(root, text="Launch Angle (degrees):")
angle_label.grid(column=0, row=1, padx=10, pady=10)
angle_entry = ttk.Entry(root)
angle_entry.grid(column=1, row=1, padx=10, pady=10)

# Create and place the button to run the simulation
simulate_button = ttk.Button(root, text="Simulate", command=run_simulation)
simulate_button.grid(column=0, row=2, columnspan=2, pady=10)

# Label to display error messages or results
result_label = ttk.Label(root, text="")
result_label.grid(column=0, row=3, columnspan=2, pady=10)

# Run the application
root.mainloop()
