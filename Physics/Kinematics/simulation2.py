import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
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
    x_vals = [x]
    y_vals = [y]
    
    # Time variable
    t = 0
    
    while y >= 0:
        # Update time
        t += dt
        
        # Update positions
        x = v0x * t
        y = v0y * t - 0.5 * g * t**2
        
        # Store positions
        x_vals.append(x)
        y_vals.append(y)
    
    return x_vals, y_vals

def animate_trajectory(x_vals, y_vals, interval=2):
    fig, ax = plt.subplots()
    ax.set_xlim(0, max(x_vals) * 1.1)
    ax.set_ylim(0, max(y_vals) * 1.1)
    
    line, = ax.plot([], [], lw=2)

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        line.set_data(x_vals[:frame], y_vals[:frame])
        return line,

    ani = FuncAnimation(fig, update, frames=len(x_vals), init_func=init, blit=True, interval=interval, repeat=False)
    plt.title("Real-Time Projectile Motion")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid(True)
    plt.show()

def run_simulation():
    try:
        v0 = float(velocity_entry.get())
        angle = float(angle_entry.get())
        x_vals, y_vals = simulate_projectile_motion(v0, angle)
        animate_trajectory(x_vals, y_vals)
    except ValueError:
        result_label.config(text="Please enter valid numbers.", fg="red")

# Create the main window
root = tk.Tk()
root.title("Real-Time Projectile Motion Simulator")

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
