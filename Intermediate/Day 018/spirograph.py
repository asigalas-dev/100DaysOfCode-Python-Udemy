import random
from random import randrange
from turtle import Turtle, Screen
screen = Screen()
screen.setup(1280, 720, 640, 360)

tim = Turtle()
tim.shape("turtle")
tim.speed(35)
# tim.width(25)

def draw_spirograph(size_of_gap, radius):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random.random(), random.random(), random.random())
        tim.circle(radius)
        tim.setheading(tim.heading() + size_of_gap)

for i in range (100):
    draw_spirograph(15, randrange(20,200))


screen.exitonclick()