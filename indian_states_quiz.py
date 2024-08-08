import turtle
from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("States Quiz")
image = "blank_indian_map.gif"
screen.addshape(image)
turtle.shape(image)


def write_name(state_name, x, y, turt):
    turt.hideturtle()
    turt.penup()
    turt.goto(x, y)
    turt.write(arg=f"{state_name}", align="center", font=("ariel", 8, "normal"))


data = pd.read_csv("state_list.csv")
data["x"] = data["x"].astype(int)
data["y"] = data["y"].astype(int)
guessed_states = []
remaining_states = data["states"].tolist()

turtle_write = Turtle()
turtle_write.speed(10)

while len(remaining_states):
    name = screen.textinput(title=f"{len(guessed_states)}/{len(data)} correct states",
                            prompt="Guess next state.").title()

    if (name in remaining_states) and (name not in guessed_states):
        guessed_states.append(name)
        remaining_states.remove(name)

        values = data[data["states"] == name].values.ravel()
        print(values[1], values[2], values[3])
        write_name(name, values[2], values[3], turtle_write)

if len(guessed_states) == len(data):
    turtle_write.goto(0, 0)
    turtle_write.write("Wohoo! You guessed them all.", align="center", font=("ariel", 30, "normal"))
else:
    remaining_states_frame = pd.DataFrame(remaining_states)
    remaining_states_frame.to_csv("states_remain.csv")


turtle.mainloop()
