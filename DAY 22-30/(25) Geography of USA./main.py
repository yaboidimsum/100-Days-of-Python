import turtle
import pandas as pd
ALIGNMENT = "center"
FONT = ("Courier", 7, "normal")

df = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.setup(width=1080, height=1080)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name").title()
    list_states = df["state"].tolist()
    if answer_state == "Exit":
        missing_states = []
        for state in list_states:
            if state not in guessed_states:
                missing_states.append(state)

        if list_states not in guessed_states:
            states_missing = {
                "Missing States": missing_states
            }
        missing_state_data = pd.DataFrame(states_missing)
        missing_state_data.to_csv("missing_states.csv")
        break
    if answer_state in list_states and answer_state not in guessed_states:
        current_list = df[df.state == answer_state]
        t = turtle.Turtle()
        t.color("Black")
        t.penup()
        t.hideturtle()
        t.goto(int(current_list.x), int(current_list.y))
        t.write(f"{answer_state}", align=ALIGNMENT, font=FONT)
        guessed_states.append(answer_state)
