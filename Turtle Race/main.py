# <--------------- Turtle Race --------------->
import random

is_game_on = False
screen.setup(width=500, height=400)
user_bet= screen.textinput(title="Make your bet",prompt=" Which turtle will win the race? Enter a color: ")
colors = ["red","blue","green","yellow","orange","purple"]
y_positions = [-70,-40,-10,20,50,80]
all_turtles = []

for index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet.lower():
                print(f"You've won, the winning turtle is {wining_color}")
            else:
                print(f"You've lost, the winning turtle was {wining_color}")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
screen.exitonclick()
