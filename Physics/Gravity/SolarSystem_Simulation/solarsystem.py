# solarsystem.py
import turtle
import math
import itertools # use cycle to iterate through planet colors

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
    min_display_size = 10
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
        # Turtle method that clears the previous drawing before redrawing the body
        self.clear()         
        self.dot(self.display_size)

    # move() method to SolarSystemBody. 
    # Any movement is made up of a component along the x-axis and another along the 
    # y-axis. There are two pairs of turtle methods that will be useful:

    # setx() and sety() change the x– and y-coordinates of the Turtle object
    # xcor() and ycor() return the current x– and y-coordinates of the Turtle object
    def move(self):
        self.setx(self.xcor() + self.velocity[0])
        self.sety(self.ycor() + self.velocity[1])

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
    colours = itertools.cycle(["red", "green", "blue","orange"])
    def __init__(
            self,
            solar_system,
            mass,
            position=(0, 0),
            velocity=(0, 0),
    ):
        super().__init__(solar_system, mass, position, velocity)
        self.color(next(Planet.colours))


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
        self.solar_system.title('Solar System Simulation')
        # list of bodies
        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)

    def remove_body(self, body):
        self.body.clear() # remove image
        self.bodies.remove(body)

    # The update_all() method goes through all the solar system bodies 
    # stored in the bodies attribute. It moves and draws them all. 
    # Finally, it calls the 

    def update_all(self):
        for body in self.bodies:
            body.move()
            body.draw()
    # Turtle update() redraws all items on the screen.  
        self.solar_system.update()
       # self.solar_system.exitonclick()

#    Gravitational Pull

    @staticmethod
    def accelerate_due_to_gravity(
            first: SolarSystemBody,
            second: SolarSystemBody,
    ):
        # Turtle method distance in pixels
        force = first.mass * second.mass / first.distance(second) ** 2
        # Turtle methods returns angle in degress
        angle = first.towards(second)
        # The acceleration changes sign between the two bodies as the bodies 
        # accelerate towards each other. 
        # The reverse variable achieves this.

        reverse = 1
        for body in first, second:
            # acceleration measred in pixels/frames**2
            acceleration = force / body.mass
            acc_x = acceleration * math.cos(math.radians(angle))
            acc_y = acceleration * math.sin(math.radians(angle))
            # velocity measured in pixels/frame
            body.velocity = (
                body.velocity[0] + (reverse * acc_x),
                body.velocity[1] + (reverse * acc_y),
            )
            reverse = -1

    # check for collisions - remove object
    def check_collision(self, first, second):
        # if two planets overlap
        if isinstance(first, Planet) and isinstance(second, Planet):
            return
        if first.distance(second) < first.display_size/2 + second.display_size/2:
            for body in first, second:
                if isinstance(body, Planet):
                    self.remove_body(body)

# You can loop through the list stored in the solar system’s bodies attribute. 
# For each body in this list, you can account for the interaction between this 
# body and all the bodies that come after it in the list. By only considering 
# interactions with bodies that come later on in the list, you’re ensuring you 
# don’t account for the same interactions twice:

# You’re creating a copy of self.bodies since the method check_collision() 
# can remove items from the list, and therefore, you shouldn’t iterate through 
# a list that can change while the loop is running. In the inner loop, you’re 
# iterating through the part of the list that comes after the current item 
# using the slice [idx + 1:].

    def calculate_all_body_interactions(self):
        bodies_copy = self.bodies.copy()
        for idx, first in enumerate(bodies_copy):
            for second in bodies_copy[idx + 1:]:
                self.accelerate_due_to_gravity(first, second)
                self.check_collision(first, second)