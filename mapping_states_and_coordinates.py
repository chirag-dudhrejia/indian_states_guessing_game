import turtle
from turtle import Screen

import numpy as np
import pandas as pd

screen = Screen()
screen.title("mapping states and co_ordinates")
image = "blank_indian_map.gif"
screen.addshape(image)
turtle.shape(image)


state_list = []
x_list = []
y_list = []


def coord(x, y):
    name = screen.textinput(title="state name", prompt="Name : ").title()
    global state_list
    global x_list
    global y_list

    if name == "Done":
        state_dict = {"states": state_list,
                      "x": x_list,
                      "y": y_list}
        data = pd.DataFrame(data=state_dict)
        data.to_csv("state_list.csv")

    state_list.append(name)
    x_list.append(x)
    y_list.append(y)
    print(state_list, x_list, y_list)


turtle.onscreenclick(coord)


turtle.mainloop()
