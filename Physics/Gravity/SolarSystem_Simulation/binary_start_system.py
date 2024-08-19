# binary star system.py
from solarsystem import SolarSystem, Sun, Planet
solar_system = SolarSystem(width=1400, height=900)

suns = (
    Sun(solar_system, mass=7000, position=(-200, 0), velocity=(0, 2)),
    Sun(solar_system, mass=5000, position=(200, 0), velocity=(0, -2)),
)
planets = (
    Planet(solar_system, mass=20, position=(50, 50), velocity=(5, 5)),
    #Planet(solar_system, mass=3, position=(-350, 0), velocity=(0, -8)),
    #Planet(solar_system, mass=1, position=(0, 200), velocity=(-2, -4)),
)

while True:
   solar_system.calculate_all_body_interactions()
   solar_system.update_all()