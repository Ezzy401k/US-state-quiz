import turtle
import pandas as pd
import fetch_name

data = pd.read_csv('50_states.csv')
data_list = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
answers = []
count = 0

while game_is_on:
    answer_state = screen.textinput(title=f"{count}/50 States Correct", prompt="whats another state name?").title()

    if answer_state == "Exit":
        break
    if answer_state in data_list:

        if answer_state not in answers:
            answers.append(answer_state)
            count += 1
            row = data[data.state == answer_state]
            x = row.x.iloc[0]
            y = row.y.iloc[0]
            name = fetch_name.FetchName(answer_state, x, y)

study = []
for state in data_list:
    if state not in answers:
        study.append(state)

study_df = pd.DataFrame(study)
study_df.to_csv("revise.csv")
