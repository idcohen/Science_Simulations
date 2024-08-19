# complex solar system.py
from solarsystem import SolarSystem, Sun, Planet
solar_system = SolarSystem(width=1400, height=900)
sun = Sun(solar_system, mass=1000)
planets = (
    Planet(
        solar_system,
        mass=10,
        position=(-500, 0),
        velocity=(0,1.),
    ),
    # moon
    Planet(
        solar_system,
        mass=0.03,
        position=(-520, 0),
        velocity=(0.3, 0.3),
    ),
    Planet(
        solar_system,
        mass=5,
        position=(-200, 0),
        velocity=(0.0,2),
    ),
        Planet(
        solar_system,
        mass=1,
        position=(-50, 0),
        velocity=(0.0,5),
    ),

)
while True:
   solar_system.calculate_all_body_interactions()
   solar_system.update_all()
   