# solarsystem.py
import turtle
import math


# Displaying the bodies
# Now, you can create another method to draw the sun or planet. 
# To keep things straightforward, you can determine the display size 
# of each body directly from its mass. 
# However, you’ll need to make a couple of adjustments. 
# Suns are much heavier than planets, so it’s best if you use a 
# logarithmic scale to convert from mass to display size. Y
# ou also want to set a minimum display size. Otherwise, bodies that 
# are not very heavy will not be visible. You can achieve both of 
# these by creating and defining a display_size attribute and 
# two class attributes called min_display_size and display_log_base:

# Solar System Bodies
class SolarSystemBody(turtle.Turtle):
    min_display_size = 20
    display_log_base = 1.1
    def __init__(
            self,
            solar_system,
            mass,
            position=(0, 0),
            velocity=(0, 0),
    ):
        super().__init__()
        self.mass = mass
        # Turtle method setposition() to place the body at a particular set of coordinates 
        self.setposition(position) # x,y tuple defaults to center of screen
        self.velocity = velocity # x,y tuple default to stationary
        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size,
        )
        # Turtle method penup() ensures the body doesn’t draw any lines as it moves 
        self.penup()
        # Turtle method hideturtle() hides the object that does the drawing.
        self.hideturtle()
        # Whenever you create a SolarSystemBody,
        #  you’re always making sure it’s linked to the solar system it belongs to.
        solar_system.add_body(self)
    
    # The draw() method uses dot() from the turtle module to draw a dot of the 
    # required size.
    def draw(self):
        self.dot(self.display_size)


# draw the sun
class Sun(SolarSystemBody):
    def __init__(
            self,
            solar_system,
            mass,
            position=(0, 0),
            velocity=(0, 0),
    ):
        super().__init__(solar_system, mass, position, velocity)
        # Turtle method to set color of Sun
        self.color("yellow")

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


