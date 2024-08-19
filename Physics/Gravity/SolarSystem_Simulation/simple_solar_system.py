# simple_solar_system.py
import turtle

from solarsystem import SolarSystem, Sun
solar_system = SolarSystem(width=1400, height=900)
sun = Sun(solar_system, mass=10_000,position=(0,0),velocity=(2, 1))
sun.draw()

# Turtle done() method keeps the display window open
# turtle.done()

while True:
    solar_system.update_all()