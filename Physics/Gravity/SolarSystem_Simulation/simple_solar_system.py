# simple_solar_system.py
import turtle

from solarsystem import SolarSystem, Sun, Planet
solar_system = SolarSystem(width=1400, height=900)
sun = Sun(solar_system, mass=10_000,position=(0,0),velocity=(0, 0))
#sun.draw()

planet = Planet(
    solar_system,
    mass=1,
    position=(-350, 0),
    velocity=(0, 3)
)

# Turtle done() method keeps the display window open
# turtle.done()

while True:
    solar_system.accelerate_due_to_gravity(sun, planet)
    solar_system.check_collision(sun, planet)
    solar_system.update_all()