import turtle
from turtle import Screen, Turtle
import pandas as pd

screen = Screen()
screen.title('EUA STATES')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
states = data.state
guessed_list = []

while len(guessed_list) < 50:
    answer = screen.textinput(title=f"Guess the State ({len(guessed_list)}/50)",
                              prompt="What's another state?")
    chosen = data[data.state == answer.title()]
    try:
        place_name = Turtle()
        place_name.penup()
        place_name.hideturtle()
        place_name.goto(int(chosen.x.item()), int(chosen.y.item()))
        place_name.write(chosen.state.item())
        guessed_list.append(answer.title())
        print(guessed_list)
    except TypeError:
        pass
    except ValueError:
        pass