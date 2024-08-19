# solarsystem.py
import turtle

class SolarSystemBody(turtle.Turtle):
    ...
class Sun(SolarSystemBody):
    ...
class Planet(SolarSystemBody):
    ...
# Solar System
class SolarSystem:
    def __init__(self, width, height):
        self.solar_system = turtle.Screen()
        # see https://docs.python.org/3/library/turtle.html
        # tracer gives you more control over when items are drawn in the window.
        self.solar_system.tracer(0)
        # setup graphics windows by pixels
        self.solar_system.setup(width, height)
        # background color
        self.solar_system.bgcolor("black")
        # list of bodies
        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)
    def remove_body(self, body):
        self.bodies.remove(body)