import random
from turtle import Turtle, Screen

is_race_on = False

screen = Screen()
screen.setup(width=600, height=400)

user_bet = screen.textinput("Pick a Racer", '''Pick the racer you think it\'s going to win.

You can choose one of the following options by writing their initial:

Leonardo : "L" / Donatello : "D" / Raphael : "R" / Michelangelo : "M"
Master Splinter : "MS" / April : "A" / Shredder : "S" / Krang : "K"
''').strip().lower()

names = ["leonardo", "donatello", "raphael", "michelangelo", "master_splinter", "april", "shredder", "krang"]
colors = ["blue", "purple", "red", "orange", "brown", "gold", "grey", "pink"]
initials = ["l", "d", "r", "m", "ms", "a", "s", "k"]

characters = []

start_x = -280
start_y = 180
spacing = 50

for i in range(len(names)):
    turtle = Turtle()
    turtle.color(colors[i])
    turtle.name = names[i].replace("_", " ").title()
    turtle.initial = initials[i]

    if names[i] == "master_splinter" or names[i] == "april":
        turtle.shape("triangle")
    elif names[i]  == "shredder":
        turtle.shape("square")
    elif names[i]  == "krang":
        turtle.shape("circle")
    else:
        turtle.shape("turtle")

    turtle.penup()
    turtle.goto(start_x, start_y - (i * spacing))

    characters.append(turtle)

if user_bet:
    is_race_on = True

winner = ""
winner_name = ""
winner_color = ""

while is_race_on:
    for char in characters:
        if char.xcor() > 280:
            is_race_on = False
            winner = char.initial
            winner_name = char.name
            winner_color = char.pencolor()
            if user_bet == winner:
                print(f"🎉 Congratulations! You chose correctly. The winner is {winner_name} with the {winner_color} color.")
            else:
                print(f"🏁 The winner is {winner_name} with the {winner_color} color. Better luck next time!")
            break

    if not is_race_on:
        break

    for char in characters:
        random_distance = random.randint(0, 10)
        char.forward(random_distance)


screen.exitonclick()