import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import ttk

def simulate_projectile_motion(v0, angle, initial_height, g=9.81, dt=0.05):
    # Convert angle to radians
    angle_rad = math.radians(angle)
    
    # Initial velocity components
    v0x = v0 * math.cos(angle_rad)
    v0y = v0 * math.sin(angle_rad)
    
    # Initial positions
    x = 0
    y = initial_height
    
    # Lists to store trajectory and velocity data
    x_vals = [x]
    y_vals = [y]
    vx_vals = [v0x]
    vy_vals = [v0y]
    
    # Time variable
    t = 0
    
    while y >= 0:
        # Update time
        t += dt
        
        # Update positions
        x = v0x * t
        y = initial_height + v0y * t - 0.5 * g * t**2
        
        # Update velocity components
        vy = v0y - g * t
        vx = v0x
        
        # Store positions and velocities
        x_vals.append(x)
        y_vals.append(y)
        vx_vals.append(vx)
        vy_vals.append(vy)
    
    return x_vals, y_vals, vx_vals, vy_vals

def animate_trajectory(x_vals, y_vals, vx_vals, vy_vals, xlim, ylim, 
                       initial_height, interval=2):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
    
    # Set up the first plot (Projectile motion)
    ax1.set_xlim(0, max(x_vals) * 1.1)
    ax1.set_ylim(0,ylim*1.1)
    #ax1.set_ylim(0, max(y_vals) * 1.1)
    ax1.set_xlabel("Distance (m)")
    ax1.set_ylabel("Height (m)")
    ax1.set_title("Projectile Motion")
    ax1.grid(True)
    
    line1, = ax1.plot([], [], lw=2)

    # Set up the second plot (Velocity)
    ax2.set_xlim(0, max(x_vals) * 1.1)
    ax2.set_ylim(min(vy_vals)*1.1, max(vy_vals) * 1.1)
    ax2.set_xlabel("Distance (m)")
    ax2.set_ylabel("Velocity (m/s)")
    ax2.set_title("Projectile Velocity")
    ax2.grid(True)
    
    line2, = ax2.plot([], [], lw=2, color='orange')

    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        return line1, line2

    def update(frame):
        line1.set_data(x_vals[:frame], y_vals[:frame])
        line2.set_data(x_vals[:frame], vy_vals[:frame])
        return line1, line2

    ani = FuncAnimation(fig, update, frames=len(x_vals), init_func=init, blit=True, 
                        interval=interval, repeat=False)
    plt.tight_layout()
    plt.show()

def run_simulation():
    try:
        v0 = float(velocity_entry.get())
        angle = float(angle_entry.get())
        ylim = int(y_range_entry.get())
        initial_height = float(init_height_entry.get())
        x_vals, y_vals, vx_vals, vy_vals = simulate_projectile_motion(v0, angle,initial_height)
        animate_trajectory(x_vals, y_vals, vx_vals, vy_vals,xlim=False,
                           ylim=ylim, initial_height=initial_height)
    except ValueError:
        result_label.config(text="Please enter valid numbers.", fg="red")

# Create the main window
root = tk.Tk()
root.configure(background="white")
root.title("Real-Time Projectile Motion Simulator with Velocity Display")


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

x_range_label = ttk.Label(root, text="x plot limit")
x_range_label.grid(column=0, row=2, padx=10, pady=10)
x_range_entry = ttk.Entry(root)
x_range_entry.grid(column=1, row=2, padx=10, pady=10)

y_range_label = ttk.Label(root, text="y plot limit")
y_range_label.grid(column=0, row=3, padx=10, pady=10)
y_range_entry = ttk.Entry(root)
y_range_entry.grid(column=1, row=3, padx=10, pady=10)

init_height_label = ttk.Label(root, text="Initial Height (m)")
init_height_label.grid(column=0, row=4, padx=10, pady=10)
init_height_entry = ttk.Entry(root)
init_height_entry.grid(column=1, row=4, padx=10, pady=10)

# Create and place the button to run the simulation
simulate_button = ttk.Button(root, text="Simulate", command=run_simulation)
simulate_button.grid(column=0, row=5, columnspan=2, pady=10)

# Label to display error messages or results
result_label = ttk.Label(root, text="")
result_label.grid(column=0, row=6, columnspan=2, pady=10)

# Run the application
root.mainloop()
