from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Corrida das tartaruga', prompt='Escolha uma cor? ')

rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
all_turtles = []
start_yposition = -130
for color in rainbow_colors:
    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(-230, start_yposition + 30)
    start_yposition = new_turtle.ycor()
    all_turtles.append(new_turtle)


leo = Turtle()
leo.shape('turtle')
leo.penup()
leo.color('black')
leo.goto(-230, start_yposition + 30)

def go():
    leo.forward(5)

screen.listen()

if user_bet:
    is_race_on = True

while is_race_on:
    screen.onkey(fun=go, key='space')
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_turtle = turtle.pencolor()
            if winner_turtle == turtle.pencolor():
                print('Ganhou')
            else:
                print('Perdeu')
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
