from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()
screen.listen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.back(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def reset_screen():
    screen.resetscreen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="r", fun=reset_screen)

screen.exitonclick()
